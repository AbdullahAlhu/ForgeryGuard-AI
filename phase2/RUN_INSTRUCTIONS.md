# ForgeryGuard AI — Phase 2 run instructions

## Standalone FastAPI service

The deployment directory already contains the trained detector, the TorchScript
segmenter, and the API module. The original DEFACTO/MSCOCO dataset is not needed
for inference.

Recommended environment: Python 3.11–3.13. A CUDA GPU is optional; CPU inference
is supported but may be slower.

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
cd M8_deployment
uvicorn phase2_api:app --host 0.0.0.0 --port 8000
```

macOS/Linux:

```bash
source .venv/bin/activate
pip install -r requirements.txt
cd M8_deployment
uvicorn phase2_api:app --host 0.0.0.0 --port 8000
```

Open `http://127.0.0.1:8000/docs`, select `POST /predict`, upload a JPG or PNG,
and execute the request. Health check: `http://127.0.0.1:8000/health`.

Example:

```bash
curl -X POST "http://127.0.0.1:8000/predict" -F "file=@test.jpg"
```

The service loads these relative artifacts automatically:

- `M8_deployment/m4_detector.pt`
- `M8_deployment/m5_segmenter.ts`
- `M8_deployment/m4_detector.onnx` (export/parity evidence)

## Full notebook reproduction

1. Open `ForgeryGuard_AI_Phase2_M4_M5_M8_Executed.ipynb` in Kaggle.
2. Attach the project manifest/originals input and the authorized DEFACTO
   Copy-Move forged-image/mask input.
3. Enable a GPU and Internet.
4. Add `WANDB_API_KEY` through Kaggle Secrets if a new online run is required.
5. Run cells in order and complete the documented human-review fields from the
   displayed evidence.

The exact Kaggle package versions are stored in `requirements-kaggle.txt`, and
the executed environment is recorded in `environment_manifest.json`.

## Scope

The final decision is `NO_GO_FOR_AUTONOMOUS_USE`. The service is an academic
demonstration and a human-review aid; it is not legal proof of forgery.
