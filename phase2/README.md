# ForgeryGuard AI — Phase 2 (M4, M5, M8)

Phase 2 extends the project with manipulation-region detection, pixel-level
segmentation, and an integrated FastAPI inference service.

## Structure

- `notebooks/` — clean executable Phase 2 notebook.
- `deployment/` — FastAPI module and Model Card.
- `results/` — locked test metrics, failure analyses, benchmark and checklist.
- `reproducibility/` — configuration and exact Kaggle environment record.
- `RUN_INSTRUCTIONS.md` — standalone API and notebook instructions.

The full executed notebook and trained model artifacts are distributed in the
`ForgeryGuard_AI_Phase2_source.zip` release/submission archive. Restricted
DEFACTO/MSCOCO images and masks are not redistributed.

## Results

| Milestone | Metric | Result |
|---|---|---:|
| M4 | Test mAP50 | 0.676394 |
| M4 | Test mAP50–95 | 0.482602 |
| M4 | Test recall | 0.604370 |
| M5 | Test Dice | 0.880575 |
| M5 | Test mean IoU | 0.806444 |
| M5 | Mask AP50 | 0.938335 |
| M5 | Mask mAP50–95 | 0.657022 |
| M8 | ONNX maximum absolute difference | 0.001099 |
| M8 | p95 latency, Tesla T4 | 52.589 ms |
| M8 | Throughput, Tesla T4 | 30.791 images/s |

The M5 and system-performance targets passed. M4 mAP50, M4 recall, and the
strict ONNX parity target were not met. The system is therefore retained as an
academic prototype and human-review aid with a `NO_GO_FOR_AUTONOMOUS_USE`
decision.

## Experiment tracking

- [Phase 2 W&B run](https://wandb.ai/mkajrfi-kaust/ForgeryGuard-AI-Phase2/runs/ze3ur823)

## Deployment

The API code expects `m4_detector.pt` and `m5_segmenter.ts` beside
`deployment/phase2_api.py`. These artifacts are included in the Phase 2 source
archive. After copying them into `deployment/`, run:

```bash
pip install -r requirements.txt
cd deployment
uvicorn phase2_api:app --host 0.0.0.0 --port 8000
```

Open `http://127.0.0.1:8000/docs` and use `POST /predict` with a JPG or PNG.
