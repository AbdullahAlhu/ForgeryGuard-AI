# ForgeryGuard AI — Phase 1 Reproducibility Evidence

## Scope

Two team members independently executed the complete Clean V2 M2/M3 notebook on Kaggle. Both runs completed training, validation-based model selection, held-out test evaluation, error analysis, W&B logging, and artifact export.

The comparison uses held-out test results at **224×224 input resolution** and a **0.50 classification threshold**. The team-defined reproducibility tolerance is an absolute difference of **0.03** for Accuracy and Macro-F1; this is not a course-specified threshold.

## Provenance checks

| Check | Primary | Reproduction | Result |
|---|---|---|---|
| Data ID | `70d923b1c24c20cb72301ebaaf461eadd962723d7229be8d94b8da325a2db4d1` | `70d923b1c24c20cb72301ebaaf461eadd962723d7229be8d94b8da325a2db4d1` | MATCH |
| Config hash | `d6214e9b52eabf9897af8702e6a42ff5fbe3a331ae4f6206d5ff5552708c17de` | `d6214e9b52eabf9897af8702e6a42ff5fbe3a331ae4f6206d5ff5552708c17de` | MATCH |
| GPU | Tesla T4 | Tesla T4 | MATCH |
| Python | 3.13.15 | 3.13.16 | DIFFERENT PATCH VERSION |
| PyTorch | 2.11.0+cu128 | 2.11.0+cu130 | DIFFERENT CUDA BUILD |

## Held-out test comparison

| Model | Primary Accuracy | Reproduction Accuracy | Δ Accuracy | Primary Macro-F1 | Reproduction Macro-F1 | Δ Macro-F1 | Status |
|---|---:|---:|---:|---:|---:|---:|---|
| M2_CNN | 0.500733 | 0.500367 | 0.000366 | 0.480995 | 0.475235 | 0.005760 | PASS |
| M3_ResNet18_frozen | 0.524194 | 0.524194 | 0.000000 | 0.524173 | 0.524175 | 0.000002 | PASS |
| M3_ResNet18_finetuned | 0.501283 | 0.574047 | 0.072764 | 0.457928 | 0.571949 | 0.114021 | OUTSIDE TOLERANCE |

## Interpretation

The M2 CNN and the official primary-selected model, **M3 ResNet18 Frozen**, reproduced within the predeclared tolerance. The frozen model was especially stable: the test Accuracy difference was **0.000000** and the Macro-F1 difference was **0.000002**.

The fine-tuned ResNet18 was outside tolerance and changed the validation-selected winner in the reproduction run. The primary run selected the frozen model, while the reproduction run selected the fine-tuned model. The runs used the same effective dataset and configuration hash, but their Python patch version and PyTorch CUDA build differed. These environment differences are documented; they do not by themselves prove the cause of the fine-tuning instability.

The official Phase 1 result remains the model selected by the primary run using validation Macro-F1 before test evaluation: **M3 ResNet18 Frozen**. Its independent reproduction was successful within tolerance. Fine-tuning sensitivity is retained as a reported limitation.

## W&B evidence

- Primary comparison run: https://wandb.ai/mkajrfi-kaust/ForgeryGuard-AI/runs/ggmh9kzb
- Independent reproduction comparison run: https://wandb.ai/mkajrfi-kaust/ForgeryGuard-AI/runs/r9f08w6k

## Files reviewed

- `forgeryguard-m2-m3-kaggle (5).ipynb` — primary execution.
- `forgeryguard-ai-m2-m3_reproduction(1).ipynb` — independent reproduction execution.
