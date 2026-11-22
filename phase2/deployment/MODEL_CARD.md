# ForgeryGuard AI — Model Card

## Model details
- System: YOLO11n copy-move region detector followed by a ResNet18 U-Net crop segmenter.
- Version: Phase 2 official run.
- Dataset: DEFACTO Copy-Move forged images with MSCOCO originals; corrected source-group split.
- Effective source pairs: 18,189.

## Intended use
Academic study and human-reviewed screening of possible copy-move manipulation in digital images.

## Out-of-scope use
Legal proof of fraud, autonomous enforcement, surveillance, identity decisions, or manipulation types outside the evaluated copy-move scope.

## Test results
- M4 mAP50: 0.676394
- M4 mAP50–95: 0.482602
- M4 recall at confidence 0.20: 0.604370
- M5 Dice at threshold 0.40: 0.880575
- M5 mean IoU: 0.806444
- Crop-level mask AP50: 0.938335
- Crop-level mask mAP50–95: 0.657022
- End-to-end p95 latency: 52.589 ms
- End-to-end throughput: 30.791 images/s

## Decision
- Decision: NO_GO_FOR_AUTONOMOUS_USE
- Failed criteria: m4_test_map50, m4_test_recall, onnx_parity
- Permitted release posture: academic demonstration and assisted screening with human review.

## Limitations
Small or visually subtle manipulated regions may be missed. The crop segmenter depends on detector proposals, and performance may shift under new compression, editing tools, image sources, or manipulation types.

## Privacy and licensing
The dataset may include identifiable people and personal content. Dataset access and redistribution rights remain subject to DEFACTO, MSCOCO, upstream image-owner, and institutional terms. Restricted images are not included in the repository or release archive.

## Ethical statement
The output is an indicator of possible manipulation, not proof of forgery or fraud. Human review is required for consequential decisions.
