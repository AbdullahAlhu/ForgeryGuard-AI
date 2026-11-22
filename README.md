# ForgeryGuard AI

ForgeryGuard AI is an AI251P Applied Computer Vision capstone for detecting and
localising copy-move image manipulation. The repository contains the Phase 1
data/classification work and the Phase 2 object-detection, segmentation, and
FastAPI integration work.

## Repository map

- `forgeryguard-ai-m1 (1).ipynb` — Phase 1 data-foundation notebook.
- `ForgeryGuard_AI_M2_M3_Final_Reviewed.ipynb` — Phase 1 classification notebook.
- `phase1_corrections/` — additive correction evidence following the Phase 1 feedback.
- `phase2/ForgeryGuard_AI_Phase2_M4_M5_M8.ipynb` — executed Phase 2 notebook.
- `phase2/results/` — locked evaluation summaries and human-review records.
- `phase2/deployment/` — FastAPI module, Model Card, and deployment documentation.
- `phase2/RUN_INSTRUCTIONS.md` — verified local and Kaggle instructions.

Restricted DEFACTO/MSCOCO images and masks are not committed or redistributed.

## Phase 2 verified results

| Milestone | Metric | Test result |
|---|---|---:|
| M4 | mAP50 | 0.676394 |
| M4 | mAP50–95 | 0.482602 |
| M4 | Recall | 0.604370 |
| M5 | Dice | 0.880575 |
| M5 | Mean IoU | 0.806444 |
| M5 | Mask AP50 | 0.938335 |
| M5 | Mask mAP50–95 | 0.657022 |
| M8 | p95 latency, Tesla T4 | 52.589 ms |
| M8 | Throughput, Tesla T4 | 30.791 images/s |

The selected validation operating points were detector confidence `0.20`, NMS
IoU `0.50`, and segmentation threshold `0.40`. M4 was evaluated at `640 px` and
M5 at `256 px` crops. The strict ONNX parity target was missed narrowly
(`0.001099` maximum absolute difference versus `0.001`), and the recorded system
decision is `NO_GO_FOR_AUTONOMOUS_USE`.

## Links

- [Phase 2 W&B run](https://wandb.ai/mkajrfi-kaust/ForgeryGuard-AI-Phase2/runs/ze3ur823)
- [Phase 2 release](https://github.com/AbdullahAlhu/ForgeryGuard-AI/releases/tag/phase2-v1)
- [Phase 2 run instructions](phase2/RUN_INSTRUCTIONS.md)
- [Model Card](phase2/deployment/MODEL_CARD.md)
- [Dataset Card](dataset_card.md)

The FastAPI service is an academic demonstration and a human-review aid. Its
output is not legal proof of forgery.
