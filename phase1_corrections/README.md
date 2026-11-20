# ForgeryGuard AI — Complete Phase 1 Correction Evidence

This package separates the correction evidence by milestone:

- `M1/`: decode audit, near-duplicate audit, leakage remediation, corrected split, and final checkpoint.
- `M2_M3/`: corrected classification reporting, calibration interpretation, false-negative analysis, W&B links, and independent reproduction comparison.
- `notebooks/`: both complete executed Clean V2 Kaggle notebooks.
- `Phase1_Correction_Matrix.csv`: grader observation-to-evidence mapping.

## Evidence status

M2 and M3 include their executed notebooks and therefore have raw output evidence in this package. M1 currently includes a structured report reconstructed from the verified console outputs supplied by the team. Add the executed M1 corrections notebook and its exported artifact folder/ZIP to the repository to make the M1 evidence equally complete.

The generated `requirements.txt` from the primary Clean V2 output must also be committed to the repository. Its creation is visible in notebook code, but the actual exported file was not attached to this package.
