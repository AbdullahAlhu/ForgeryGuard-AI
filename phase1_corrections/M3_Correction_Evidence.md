# M3 — Transfer Learning Correction Evidence

## Official primary-selected model

**M3 ResNet18 Frozen**, selected using validation Macro-F1 before test evaluation.

## Held-out test metrics

| Metric | Value |
|---|---:|
| Accuracy | 0.524194 |
| Macro-F1 | 0.524173 |
| ECE | 0.037357 |

## Per-class held-out test metrics

| Class | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Original | 0.5245 | 0.5176 | 0.5210 | 2,728 |
| Forged | 0.5239 | 0.5308 | 0.5273 | 2,728 |

## Calibration interpretation

Approximately 94.34% of the official model confidence scores were between 0.50 and 0.65. Therefore, the low ECE must not be interpreted as evidence of a strong classifier; it reflects predictions concentrated near low confidence while overall discrimination remains limited.

## False-negative analysis

| Manipulated mask area | Forged images | False negatives | False-negative rate |
|---|---:|---:|---:|
| <1% | 1,414 | 686 | 0.4851 |
| 1–5% | 922 | 434 | 0.4707 |
| 5–15% | 332 | 132 | 0.3976 |
| ≥15% | 60 | 28 | 0.4667 |

The highest observed false-negative rate was associated with manipulated regions below 1% of image area. The proposed next experiment is mask-guided full-resolution cropping selected on validation data. Texture and subtle-edit causes are not claimed because they were not directly measured.

## Independent reproduction

The official frozen model reproduced with an Accuracy difference of **0.000000** and a Macro-F1 difference of **0.000002**. Fine-tuned ResNet18 was outside the predefined tolerance, so its instability is disclosed rather than hidden.

## W&B

- Primary: https://wandb.ai/mkajrfi-kaust/ForgeryGuard-AI/runs/ggmh9kzb
- Reproduction: https://wandb.ai/mkajrfi-kaust/ForgeryGuard-AI/runs/r9f08w6k
