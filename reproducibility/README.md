# ForgeryGuard AI — M2/M3 Reproducibility Evidence

## Result

Abdullah independently reran the saved M2/M3 notebook using the same configuration and data pipeline. The validation, held-out test, and JPEG90 stress-test tables match Mishari’s reference notebook across all 21 columns for all three models. No metric mismatch exceeded the absolute tolerance of `1e-12`.

## Immutable provenance

- Reference operator: Mishari
- Reproduction operator: Abdullah
- Reference GitHub commit: `d31e5882a1252989379957e845137f25def52b6b`
- Reproduction GitHub commit: `9d8238aba5bfc146a307b8f5b6a6cc0c8cf644c1`
- Reference notebook SHA-256: `de62d0d24d6b77ce8b5eb227d980b979352a21363b90bd7111dc4e763fe1d40e`
- Reproduction notebook SHA-256: `69c1783c99c0348a0d9fd0939c4b91d5a80f19693e5001b96d749b69c47a7b9b`

## Comparison summary

| Evaluation | Shape | Columns | Mismatches (`atol=1e-12`) | Maximum numeric delta | Status |
|---|---:|---|---:|---:|---|
| Validation | 3 × 21 | Identical | 0 | 9.714e-17 | MATCH |
| Held-out test | 3 × 21 | Identical | 0 | 7.112e-17 | MATCH |
| JPEG90 stress test | 3 × 21 | Identical | 0 | 6.765e-17 | MATCH |

## Configuration and environment

- The complete `CFG` dictionaries extracted from both notebooks are exactly identical.
- Both saved runs report Python `3.13.15`, PyTorch `2.11.0+cu128`, CUDA device, and Tesla T4.
- The reference and reproduction use different W&B offline run identifiers, supporting that they are separate executions.

## Evidence source and limitation

The original standalone reference `config.json`, `environment.json`, and `experiment_report.json` were not retained. Their verifiable fields were extracted from the immutable reference notebook source and printed output. Package versions that were not printed are recorded as unavailable and were not guessed. The actual reproduction CSV exports are included unchanged.

## Files

- `provenance_and_comparison.json`: commits, notebook hashes, W&B run identifiers, and machine-readable comparison.
- `reference_*_extracted.json`: exact reference tables extracted from the saved notebook output.
- `reproduction_*.csv`: actual CSV exports from Abdullah’s rerun.
- `*_config_extracted.json`: exact notebook configurations.
- `environment_evidence.json`: only environment facts visible in saved output.
- `requirements.txt`: reconstructed, pinned target environment covering M1–M5 and M8; it is not represented as an original `pip freeze`.
