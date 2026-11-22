# ForgeryGuard AI — Phase 1 correction evidence

This directory is an additive correction record. It preserves the original
Phase 1 submission and documents the changes made in response to the grader's
feedback.

## Included evidence

- `M1_Correction_Evidence.md` and `m1_correction_evidence.json` — full decode
  audit, perceptual near-duplicate review, leakage remediation, and final M1
  checkpoint.
- `dataset_split_portable_corrected.csv` — corrected source-group manifest.
- `M2_Correction_Evidence.md` and `M3_Correction_Evidence.md` — completed
  per-class metrics, calibration interpretation, and failure analysis.
- `Phase1_Reproducibility_Evidence.md` plus CSV/JSON comparisons — primary and
  independent rerun evidence.
- `Phase1_Correction_Matrix.csv` — grader comment-to-evidence mapping.
- `ForgeryGuard_AI_Phase1_Correction_Report.pdf` — concise correction report.

## M1 corrected checkpoint

| Check | Result |
|---|---:|
| Full decoded files | 54,582 / 54,582 |
| Decode errors | 0 |
| pHash candidate pairs (64-bit, Hamming ≤ 5) | 5 |
| Cross-split related candidates | 1 |
| Excluded source group | `000000396188` |
| Effective source pairs | 18,193 |
| Train / validation / test pairs | 12,735 / 2,729 / 2,729 |
| Remaining source-group leakage | 0 |
| Corrected manifest SHA-256 | `42d9c01f7588366ed5e2a327da4c2cca5253ea0a4989167827ec8df386f0a9c6` |

Privacy review and the final DEFACTO agreement/redistribution verification remain
pending and are not represented as completed.

## Evidence limitation

The executed M2/M3 primary and reproduction notebooks are retained in the
original evidence archive. The executed M1 correction notebook was not saved
from the Kaggle session. The M1 evidence here therefore consists of the
corrected manifest, structured audit exports, verified console results, and the
correction report. This limitation is stated explicitly rather than replacing
the missing raw notebook with reconstructed evidence.
