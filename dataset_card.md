# ForgeryGuard AI — Dataset Card

## 1. Dataset Overview

**Project:** ForgeryGuard AI — Image Forgery Detection and Localization  
**Course:** AI251P — Applied Computer Vision  
**Task:** Binary Image Classification (Authentic vs. Manipulated)  
**Dataset Sources:** DEFACTO Copy-Move and MS COCO

This dataset supports the development and evaluation of deep learning models for detecting image manipulation, particularly copy-move forgery.

It contains authentic images and their corresponding manipulated versions. The dataset is used for academic research, image classification, and future forgery localization experiments.

## 2. Data Sources

The project uses two data sources:

- **MS COCO:** Provides authentic source images.
- **DEFACTO Copy-Move:** Provides manipulated images and associated forgery annotations.

The project team obtained permission to access and use the DEFACTO dataset for academic research through email correspondence with the dataset owners. The approval was shared with the team by Mishari.

No new images were collected by the project team.

## 3. Dataset Composition

| Property | Value |
|---|---|
| Authentic images | 18,194 |
| Manipulated images | 18,194 |
| Initial total images | 36,388 |
| Total image pairs | 18,194 |
| Number of classes | 2 |
| Class labels | Authentic, Manipulated |
| Manipulation type | Copy-Move Forgery |

Each pair contains an original image and its corresponding manipulated version.

During M2–M3 dataset preparation, four conflicting source groups (eight images) were excluded, leaving 36,380 images for the classification experiments.

## 4. Dataset Splitting

A source-grouped splitting strategy was used to reduce data leakage.

| Split | Initial image pairs |
|---|---:|
| Training | 12,735 |
| Validation | 2,729 |
| Test | 2,730 |
| **Total** | **18,194** |

Original and manipulated images from the same source group were assigned to the same split.

This prevents corresponding image pairs from appearing across different subsets.

The table shows the initial split before the eight-image exclusion in M2–M3.

## 5. Data Preparation and Quality Checks

Dataset preparation included:

- Image and file validation.
- Duplicate and source-group consistency checks.
- Classification-label verification.
- Visual inspection of manipulation masks and bounding boxes.
- Source-grouped splitting to reduce data leakage.

### Human Label Audit

A stratified sample of 100 image pairs was manually reviewed:

| Split | Reviewed pairs |
|---|---:|
| Training | 70 |
| Validation | 15 |
| Test | 15 |
| **Total** | **100** |

**Audit results:**

- Observed classification-label errors: 0.
- Observed error rate: 0%.
- Wilson 95% confidence interval: approximately 0%–3.70%.

No classification-label errors were identified in the reviewed sample.

These findings do not guarantee that the entire dataset is error-free.

## 6. Annotations and Visual Review

The dataset provides:

- Image-level authenticity labels.
- Pixel-level forgery segmentation masks.
- Bounding-box annotations identifying manipulated regions.

A visual inspection of 12 displayed examples was conducted during M2–M3 review.

**Observations:**

- The displayed manipulated images were visually consistent with their forgery labels.
- Masks and bounding boxes generally aligned with the visible manipulation regions.
- Some manipulated regions were small or near image boundaries.
- No obvious annotation mismatch was identified in the reviewed examples.

The visual review covers only the displayed examples and is not a complete annotation audit.

Phase 1 focuses on binary image classification. Bounding boxes and segmentation masks support future localization experiments.

## 7. Privacy Assessment

A separate preliminary privacy audit was conducted on 100 image pairs.

**Results:**

- Reviewed pairs: 100.
- Pairs flagged for further assessment: 30.
- Privacy mitigation: Pending further verification.

The identified cases require additional review before unrestricted redistribution.

The project does not claim that all privacy risks have been eliminated.

## 8. Known Limitations

- The dataset focuses on copy-move image forgery and does not represent all manipulation techniques.
- Some manipulated regions are visually subtle or small.
- Models trained on this dataset may not generalize to all real-world images.
- Human label and privacy audits were conducted on samples rather than the complete dataset.
- Visual annotation review was limited to selected examples.
- Dataset access and redistribution remain subject to the applicable permissions and licensing terms.

## 9. Licensing and Usage Restrictions

### DEFACTO Copy-Move

The project team obtained permission to access and use the DEFACTO Copy-Move dataset for academic research through email correspondence with the dataset owners.

The approval was shared with the project team by Mishari.

The permission supports the authorized academic use of the dataset. It does not automatically establish permission to redistribute the original images, manipulated images, or other restricted dataset materials.

The approval correspondence is retained by the project team as supporting documentation.

### MS COCO

The COCO annotations are distributed under CC BY 4.0. Copyrights for the underlying images remain with their respective rights holders.

### Redistribution Policy

The GitHub repository contains project code, documentation, and permitted metadata rather than redistributing the complete image datasets.

Users seeking access to the underlying datasets should obtain them through the appropriate sources and comply with the applicable conditions.

## 10. Reproducibility

The project provides Jupyter Notebooks covering:

- M1: Dataset preparation, quality checks, splitting, and auditing.
- M2: CNN classification model trained from scratch.
- M3: Transfer learning using ResNet18 with frozen and fine-tuned configurations.
- Model evaluation, comparison, and error analysis.

The experiments use separate training, validation, and test datasets.

The complete training pipeline requires authorized access to the underlying datasets and the software dependencies documented in the project repository.

## 11. Intended Use

The dataset is intended for:

- Academic computer vision research.
- Binary image forgery classification.
- Training and comparison of deep learning architectures.
- Image manipulation detection research.
- Future object detection and segmentation experiments.

The dataset and resulting models are not intended to provide conclusive forensic evidence.

The current classification models have limited generalization and should not be considered validated for unrestricted real-world deployment.

## 12. Dataset Availability

**Dataset name:** ForgeryGuard AI  
**Platform:** Kaggle  
**Dataset page:** https://www.kaggle.com/datasets/mkajrfi/forgeryguard-ai

Access to the Kaggle dataset may require authentication and appropriate permissions.

The complete image collection is not redistributed through the GitHub repository.

---

## 13. Documentation Status

| Item | Status |
|---|---|
| Dataset preparation | Completed |
| Source-grouped splitting | Completed |
| Classification-label sample audit | Completed |
| Selected mask and bounding-box visual review | Completed |
| Preliminary privacy screening | Completed |
| Privacy mitigation follow-up | Pending |
| DEFACTO academic-use permission | Obtained through email |
| Unrestricted redistribution permission | Not established |
| M2–M3 classification experiments | Completed |

---

*This dataset card documents the dataset preparation, validation procedures, access permissions, and known limitations of ForgeryGuard AI during Phase 1 of the AI251P Applied Computer Vision Capstone Project.*
