# ForgeryGuard AI

**AI251P — Applied Computer Vision Capstone | Phase 1 (M1–M3)**

ForgeryGuard AI studies **image forgery detection**, focusing on distinguishing authentic images from copy-move manipulated images. Phase 1 covers dataset preparation and validation (M1), a CNN trained from scratch (M2), and transfer learning with frozen and fine-tuned ResNet18 models (M3). Image localization is planned for subsequent phases and is **not** a completed Phase 1 output.

## Data

The academic experiments use MS COCO-derived authentic images and corresponding DEFACTO Copy-Move manipulated images. The initial manifest contains **18,194 image pairs (36,388 images)**. Four conflicting source groups (eight images) were excluded during the M2–M3 preparation, leaving **36,380 classification images**. Original and manipulated versions are kept in the same source-group split to reduce leakage.

Initial grouped splits: **12,735** training pairs, **2,729** validation pairs, **2,730** test pairs. See [`dataset_card.md`](dataset_card.md) for the audit methods, privacy limitations, licensing, and permitted use.

**Dataset access:** https://www.kaggle.com/datasets/mkajrfi/forgeryguard-ai (may require authorization). DEFACTO access for academic use was granted by the dataset owners via email correspondence shared with the project team. This does **not** imply permission to redistribute the images. No raw DEFACTO/MS COCO images should be committed to this repository.

## Notebooks

- **M1:** dataset preparation, integrity and label audits, group-safe splits, and dataset documentation.
- **M2–M3:** scratch CNN, frozen ResNet18, fine-tuned ResNet18, experiment tracking, validation/test evaluation and error analysis.

The `.ipynb` notebooks in this repository contain saved outputs from a previous Kaggle run. Saved outputs are evidence of that run, **not** a claim of successful independent rerun in a new environment. The M2–M3 notebook also contains a subsequent visual-review annotation; the earlier saved `PENDING` outputs may therefore remain visible.

## Phase 1 results

Results recorded in the M2–M3 notebook on the test set:

| Model | Accuracy | Macro-F1 | ROC-AUC |
|---|---:|---:|---:|
| CNN from scratch | 0.4996 | 0.4968 | 0.502 |
| Frozen ResNet18 | 0.5185 | 0.4948 | 0.535 |
| Fine-tuned ResNet18 | **0.5883** | **0.5783** | **0.634** |

The fine-tuned model performed best in these experiments but detected only approximately **43.46% of manipulated test images** at the recorded decision threshold. It is **not** validated for conclusive forensic decisions or real-world deployment.

## Reproducibility

1. Open the M1 and M2–M3 notebooks on Kaggle with authorized datasets attached.
2. Consult the M2–M3 notebook's `CFG` dictionary for the actual experimental configuration: seed `251`, image size `224`, batch size `32`, class threshold `0.5`, and up to `8` epochs per training configuration.
3. Use a GPU for training. The recorded execution used **Python 3.13.15, PyTorch 2.11.0+cu128, and an NVIDIA Tesla T4**.
4. See [`requirements.txt`](requirements.txt) for the dependencies identified in the notebook. Exact versions of several dependencies were not captured in the supplied saved outputs and must be verified from the original Kaggle environment before claiming fully pinned reproducibility.
5. The W&B notebook configuration uses offline logging; synchronized runs and project visibility should be verified using the corresponding Forge project.

**Data paths:** Some paths in the notebooks are Kaggle-specific. Adjust dataset mounts if running elsewhere. Training requires access to the source images and saved split manifests. Avoid rerunning training solely to reproduce the stored presentation outputs.

## Research integrity and limitations

The dataset card documents the 100-pair label audit (0 observed errors; Wilson 95% error-rate interval approximately 0%–3.70%), preliminary privacy screening, and limited image/mask visual review. These audits do not establish complete dataset correctness or eliminate privacy risk. The original image datasets are not redistributed here.

## Project resources

- [Dataset card](dataset_card.md)
- [Kaggle dataset](https://www.kaggle.com/datasets/mkajrfi/forgeryguard-ai)
- W&B / Forge: add the **verified instructor-accessible** project URL to the Phase 1 report.

## Academic context

Course: **AI251P — Applied Computer Vision**. Project: **ForgeryGuard AI — Image Forgery Detection and Localization**. Phase 1 covers **M1–M3**; detection, segmentation, and deployment are subsequent work.
