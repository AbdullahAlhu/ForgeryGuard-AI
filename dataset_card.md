# ForgeryGuard AI — Dataset Card

## Dataset summary

ForgeryGuard AI uses MSCOCO-derived authentic images paired with DEFACTO
Copy-Move manipulated images and corresponding tampering masks. The project is
limited to copy-move manipulation. Restricted source images and masks are not
redistributed in this repository.

## Dataset lineage

| Stage | Source pairs | Train | Validation | Test | Purpose |
|---|---:|---:|---:|---:|---|
| Initial M1 manifest | 18,194 | 12,735 | 2,729 | 2,730 | Original source-group split |
| Corrected M1 manifest | 18,193 | 12,735 | 2,729 | 2,729 | One cross-split near-duplicate source group excluded |
| Phase 2 effective set | 18,189 | 12,733 | 2,728 | 2,728 | Four identical-pixel label-conflict groups excluded |

The corrected M1 manifest SHA-256 is
`42d9c01f7588366ed5e2a327da4c2cca5253ea0a4989167827ec8df386f0a9c6`.
The near-duplicate remediation excluded source group `000000396188`. Phase 2
also excluded source groups `000000417134`, `000000537055`, `000000448046`, and
`000000469870`, because each contained an authentic/forged pair with identical
decoded pixels and contradictory labels.

## Audits

- Full M1 decode audit: 54,582 / 54,582 expected image, forged-image, and mask
  files decoded successfully; no dimension issues were reported.
- Perceptual near-duplicate audit: 64-bit pHash with Hamming distance ≤ 5
  produced five manually reviewed candidates. One related pair crossed splits
  and was remediated by excluding its test source group.
- Leakage check: no source group or retained exact-content hash crosses the
  corrected splits.
- Human label/mask audit: a stratified sample of 100 pairs (70 train, 15
  validation, 15 test) recorded 0 errors. The Wilson 95% interval for the error
  rate was approximately 0%–3.70%; this does not prove that the full dataset is
  error-free.
- Phase 2 automated annotation audit: 18,189 forged images, masks, and box rows
  were decoded and structurally validated. A displayed manual sample was also
  reviewed before training.

## Privacy and licensing

DEFACTO access was reported as approved for academic research by the project
team. Underlying authentic images originate from MSCOCO/Flickr and remain
subject to their respective rights. The individual DEFACTO agreement and image
redistribution permissions require final verification.

A separate 100-pair privacy sample flagged 30 unique pairs for additional
review, including visible faces, vehicle details, documents/screens, and one
potentially sensitive case. No claim of full privacy compliance is made.

## Intended and prohibited use

The dataset supports academic detection and localisation of copy-move image
manipulation. Results are indicators for human review and are not legal proof
of fraud or forgery. The dataset must not be used for surveillance, identity
decisions, or automated punitive decisions.

## Known limitations

- The content distribution follows MSCOCO/DEFACTO and may not generalise to
  Saudi listing images or other manipulation families.
- Small manipulated regions remain difficult for the detector.
- Privacy screening is sample-based rather than exhaustive.
- The final redistribution scope and DEFACTO agreement terms remain pending.
