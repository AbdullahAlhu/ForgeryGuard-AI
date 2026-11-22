# ForgeryGuard AI — Phase 2 (M4, M5, M8)

Phase 2 adds manipulated-region detection (M4), pixel-level segmentation (M5),
and an integrated FastAPI inference service with export and performance evidence
(M8).

## Structure

- `ForgeryGuard_AI_Phase2_M4_M5_M8.ipynb` — executed Phase 2 notebook.
- `deployment/` — FastAPI module, Model Card, local verification, and artifact notes.
- `results/` — locked test metrics, failure analyses, benchmark, and checklist.
- `reproducibility/` — configuration and exact Kaggle environment record.
- `RUN_INSTRUCTIONS.md` — verified API and notebook instructions.
- `requirements.txt` — portable API environment tested with Python 3.13.

Large trained artifacts are distributed through the `phase2-v1` GitHub release
and the Blackboard source archive. Restricted DEFACTO/MSCOCO images and masks
are not redistributed.

## Locked results

| Milestone | Metric | Test result |
|---|---|---:|
| M4 | mAP50 | 0.676394 |
| M4 | mAP50–95 | 0.482602 |
| M4 | Recall | 0.604370 |
| M5 | Dice | 0.880575 |
| M5 | Mean IoU | 0.806444 |
| M5 | Mask AP50 | 0.938335 |
| M5 | Mask mAP50–95 | 0.657022 |
| M8 | ONNX maximum absolute difference | 0.001099 |
| M8 | p95 latency, Tesla T4 | 52.589 ms |
| M8 | Throughput, Tesla T4 | 30.791 images/s |

M5 and the M8 performance targets passed. M4 mAP50, M4 recall, and the strict
ONNX parity target were not met. The final decision is therefore
`NO_GO_FOR_AUTONOMOUS_USE` while retaining the service as an academic prototype
and human-review aid.

## Links

- [W&B Phase 2 run](https://wandb.ai/mkajrfi-kaust/ForgeryGuard-AI-Phase2/runs/ze3ur823)
- [Portable release](https://github.com/AbdullahAlhu/ForgeryGuard-AI/releases/tag/phase2-v1)
- [Run instructions](RUN_INSTRUCTIONS.md)
- [Model Card](deployment/MODEL_CARD.md)
