# Detection Ops

Guidelines: tight boxes (2-5px margin), occluded = visible extent + flag, truncated at edge flagged, crowds as crowd boxes (no per-instance fiction), tiny (<10px) flagged or excluded by policy. Pictures per rule; pilot 200; agreement mean-IoU over 0.85.

COCO validation: boxes inside image, w/h positive, area sane, no exact dupes, category ids valid, image ids resolve, no orphan annotations, splits scene-disjoint. Fail training on any error.

Training: pretrained backbones (COCO-pretrained start); input size matched to smallest object (>= 32px after scaling ideally); tiling for tiny/dense; NMS IoU 0.5 + score threshold tuned on val per class. Report mAP@[.5:.95] plus mAP-S/M/L plus per-class AP.

Splits: by scene/video/source, never random frames; dedupe near-identical frames across splits; lock test. Ship: mAP-S floor for small-critical tasks, worst-class floor, latency budget, error gallery reviewed by domain eyes.
