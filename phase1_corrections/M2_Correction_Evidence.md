# M2 — Classification From Scratch Correction Evidence

## Grader observations addressed

- Per-class Precision, Recall and F1 were missing.
- Calibration was reported without interpretation.
- The error gallery did not represent the major false-negative failure mode.
- Proposed explanations were not supported with counts.

## Evaluation discipline

- Input resolution: **224×224**
- Classification threshold: **0.50**
- Model selection: **Validation Macro-F1 before test evaluation**
- Held-out test support: **2,728 Original + 2,728 Forged**

## M2 CNN held-out test results

| Metric | Primary | Independent reproduction | Absolute difference |
|---|---:|---:|---:|
| Accuracy | 0.500733 | 0.500367 | 0.000366 |
| Macro-F1 | 0.480995 | 0.475235 | 0.005760 |

The M2 CNN reproduced within the team-defined absolute tolerance of 0.03.

## Corrective outputs now present

The executed Clean V2 notebooks include learning curves, confusion matrices, per-class Precision/Recall/F1/support tables, calibration outputs, and restricted failure analysis. These outputs address the missing evidence categories even though the M2 CNN remained near chance performance.
