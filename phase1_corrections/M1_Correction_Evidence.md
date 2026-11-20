# M1 — Data Foundations Correction Evidence

## Grader observations addressed

- A complete decode check was not reported.
- No near-duplicate check was reported despite near-identical MSCOCO scenes.
- The split method, ratio and seed were not stated clearly.
- The corrected split artifact was not committed or created by the submitted code.

## Full decode audit

| Measure | Result |
|---|---:|
| Source pairs | 18194 |
| Files attempted | 54582 |
| Files decoded successfully | 54582 |
| Decode errors | 0 |
| Dimension issue groups | 0 |

**Status:** Full decode audit passed.

## Perceptual near-duplicate audit

All 18,194 original images were hashed using a 64-bit perceptual hash. Candidate pairs used a Hamming-distance threshold of 5. Five candidate pairs were identified and visually reviewed. One candidate connected the training and test splits.

| Measure | Result |
|---|---:|
| Near-duplicate candidate pairs | 5 |
| Candidate components | 5 |
| Cross-split candidates before correction | 1 |
| Confirmed related scenes | 5 |
| Excluded source groups | `000000396188` |
| Remaining cross-split candidates | 0 |

The related test source group was excluded without deleting the raw files or reassigning the remaining source groups.

## Corrected leakage-safe split

| Split | Source pairs | Ratio |
|---|---:|---:|
| Train | 12,735 | 0.699995 |
| Validation | 2,729 | 0.150003 |
| Test | 2,729 | 0.150003 |
| Total | 18,193 | 1.000000 |

- Source-group leakage: **0**
- Remaining cross-split perceptual candidates: **0**
- Corrected manifest SHA-256: `42d9c01f7588366ed5e2a327da4c2cca5253ea0a4989167827ec8df386f0a9c6`
- Split seed: the original seed was not preserved in the earlier artifact. Exact assignments are reproduced by the corrected committed manifest; this limitation is disclosed rather than replaced with an invented seed.

## Final M1 checkpoint

- Technical status: **PASS**
- Classification images: **36,386**
- Decode errors: **0**
- Dimension issues: **0**
- Source-group leakage: **0**
- Privacy review: **PENDING — manual verification**
- License review: **PENDING — agreement verification**

## Evidence limitation

The executed M1 correction notebook and its exported output archive were not attached to this review package. The values above reproduce the verified console outputs supplied by the team. Add the original executed M1 correction notebook and exported artifacts to the repository to preserve raw evidence.
