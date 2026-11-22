from io import BytesIO
from pathlib import Path
import base64
import math
import time

import numpy as np
from PIL import Image, ImageOps, ImageDraw
import torch
from torchvision.transforms import functional as TF
from torchvision.transforms import InterpolationMode
from ultralytics import YOLO
from fastapi import FastAPI, UploadFile, File, HTTPException

BASE_DIR = Path(__file__).resolve().parent
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
M4_IMAGE_SIZE = 640
M5_IMAGE_SIZE = 256
M4_CONFIDENCE = 0.2
M4_NMS_IOU = 0.5
M5_THRESHOLD = 0.4
M5_CROP_PADDING = 0.15
IMAGENET_MEAN = torch.tensor([0.485, 0.456, 0.406])[:, None, None]
IMAGENET_STD = torch.tensor([0.229, 0.224, 0.225])[:, None, None]

M4_MODEL = YOLO(str(BASE_DIR / "m4_detector.pt"))
M5_MODEL = torch.jit.load(str(BASE_DIR / "m5_segmenter.ts"), map_location=DEVICE).eval()

def encode_png_base64(array_uint8):
    buffer = BytesIO()
    Image.fromarray(array_uint8).save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode("ascii")

def segment_candidate(image, box):
    width, height = image.size
    xmin, ymin, xmax, ymax = [float(v) for v in box]
    pad_x = M5_CROP_PADDING * max(xmax - xmin, 1.0)
    pad_y = M5_CROP_PADDING * max(ymax - ymin, 1.0)
    left = max(0, int(math.floor(xmin - pad_x)))
    top = max(0, int(math.floor(ymin - pad_y)))
    right = min(width, int(math.ceil(xmax + pad_x)))
    bottom = min(height, int(math.ceil(ymax + pad_y)))
    crop = image.crop((left, top, right, bottom)).convert("RGB")
    tensor = TF.to_tensor(TF.resize(
        crop, [M5_IMAGE_SIZE, M5_IMAGE_SIZE],
        interpolation=InterpolationMode.BILINEAR, antialias=True,
    ))
    tensor = ((tensor - IMAGENET_MEAN) / IMAGENET_STD).unsqueeze(0).to(DEVICE)
    with torch.no_grad():
        probability = torch.sigmoid(M5_MODEL(tensor))[0, 0].cpu()
    resized = TF.resize(
        probability.unsqueeze(0), [bottom - top, right - left],
        interpolation=InterpolationMode.BILINEAR, antialias=True,
    )[0].numpy()
    return resized, (left, top, right, bottom)

def infer(image):
    image = ImageOps.exif_transpose(image).convert("RGB")
    width, height = image.size
    total_started = time.perf_counter()
    started = time.perf_counter()
    detection = M4_MODEL.predict(
        source=np.asarray(image), imgsz=M4_IMAGE_SIZE, conf=M4_CONFIDENCE,
        iou=M4_NMS_IOU, device=0 if DEVICE.type == "cuda" else "cpu", verbose=False,
    )[0]
    detection_ms = (time.perf_counter() - started) * 1000
    boxes = detection.boxes.xyxy.cpu().numpy() if detection.boxes is not None else np.empty((0, 4))
    confidences = detection.boxes.conf.cpu().numpy() if detection.boxes is not None else np.empty((0,))
    union_probability = np.zeros((height, width), dtype=np.float32)
    response_boxes = []
    started = time.perf_counter()
    for box, confidence in zip(boxes, confidences):
        probability, (left, top, right, bottom) = segment_candidate(image, box)
        union_probability[top:bottom, left:right] = np.maximum(
            union_probability[top:bottom, left:right], probability
        )
        response_boxes.append({
            "xyxy": [round(float(v), 3) for v in box],
            "confidence": round(float(confidence), 6),
        })
    segmentation_ms = (time.perf_counter() - started) * 1000
    started = time.perf_counter()
    binary_mask = (union_probability >= M5_THRESHOLD).astype(np.uint8) * 255
    annotated = image.copy()
    drawer = ImageDraw.Draw(annotated)
    for item in response_boxes:
        drawer.rectangle(item["xyxy"], outline="red", width=max(2, width // 300))
        drawer.text((item["xyxy"][0], item["xyxy"][1]), f"{item['confidence']:.3f}", fill="red")
    if binary_mask.any():
        overlay_array = np.zeros((height, width, 4), dtype=np.uint8)
        overlay_array[binary_mask > 0] = [255, 0, 0, 100]
        annotated = Image.alpha_composite(
            annotated.convert("RGBA"), Image.fromarray(overlay_array, mode="RGBA")
        ).convert("RGB")
    annotated_buffer = BytesIO()
    annotated.save(annotated_buffer, format="JPEG", quality=90)
    postprocessing_ms = (time.perf_counter() - started) * 1000
    return {
        "model_version": "ForgeryGuard_AI_Phase2",
        "verdict": "suspected_manipulation" if response_boxes and binary_mask.any() else "no_region_detected",
        "image_width": width,
        "image_height": height,
        "boxes": response_boxes,
        "mask_threshold": M5_THRESHOLD,
        "mask_positive_pixels": int((binary_mask > 0).sum()),
        "stage_latency_ms": {
            "detection": round(detection_ms, 3),
            "segmentation": round(segmentation_ms, 3),
            "postprocessing": round(postprocessing_ms, 3),
        },
        "total_latency_ms": round((time.perf_counter() - total_started) * 1000, 3),
        "mask_png_base64": encode_png_base64(binary_mask),
        "annotated_jpeg_base64": base64.b64encode(annotated_buffer.getvalue()).decode("ascii"),
    }

app = FastAPI(title="ForgeryGuard AI", version="2.0")

@app.get("/health")
def health():
    return {"status": "ok", "device": str(DEVICE)}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if file.content_type not in {"image/jpeg", "image/png"}:
        raise HTTPException(status_code=415, detail="Only JPG and PNG images are supported.")
    try:
        image = Image.open(BytesIO(await file.read()))
        image.load()
    except Exception as exc:
        raise HTTPException(status_code=400, detail=f"Invalid image: {type(exc).__name__}") from exc
    return infer(image)
