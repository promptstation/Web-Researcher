---
name: object-detection-ops
description: Ship detectors with consistent boxes, clean COCO, and sliced mAP. Use when the user asks to annotate bounding boxes; validate COCO dataset; train object detector; interpret mAP scores; detect small objects.
compatibility: COCO-format tools; CVAT/Label Studio for annotation; mmdet/Ultralytics per stack.
metadata:
  author: Promptstation
  version: 1.0.0
  category: computer-vision
---

# Object Detection Ops

Detect with discipline. You write guidelines annotators can follow, validate every COCO file, train baselines that converge, slice mAP by size and class, and fix small and dense objects with targeted data.

Optimize simultaneously for:

- consistent boxes
- clean COCO
- converged baselines
- honest mAP
- fixed hard cases

No training on unvalidated annotations; no ship on single-number mAP.

## Use Cases

### New detector

Trigger: user says 'detect products on shelves' or 'train YOLO'

Steps:

1. Guideline plus pilot
2. Annotate with QA
3. Validate COCO
4. Train and slice

Result: Shipped detector.

### Small misses

Trigger: user says 'misses small items' or 'far objects lost'

Steps:

1. Slice mAP-small
2. Tile and augment
3. Raise resolution
4. Verify lift

Result: Small found.

### Box chaos

Trigger: user says 'annotators disagree' or 'noisy boxes'

Steps:

1. Tighten guideline
2. Measure agreement
3. Adjudicate
4. Re-validate

Result: Consistent boxes.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Box guideline
- Agreement scores
- COCO validation
- Training config
- Sliced mAP
- NMS settings
- Error gallery
- Ship checklist

Never train on disagreed boxes or report mAP without size/class slices.

## Phase 1 — Guide Annotators

Tightness, occlusion, truncation, crowd rules with pictures.

Pilot 200; agreement over 0.85 IoU.

Adjudicate splits.

## Phase 2 — Validate COCO

Run `scripts/boxes_audit.py --coco ann.json` before every train.

Bounds, areas, dupes, orphans fixed.

Splits decontaminated.

## Phase 3 — Train Baseline

Pretrained detector; sane schedule.

NMS tuned on val.

Reproduce best twice.

## Phase 4 — Slice and Fix

mAP by size (S/M/L) and class.

Tile/augment/collect for gaps.

Ship on sliced criteria.

## Examples

### Example 1: Shelf detector

User says: "10k shelf SKUs to detect."

Actions:

1. Guideline plus QA
2. Clean COCO
3. mAP 0.62 sliced
4. Small fixed with tiles

Result: Deployed detector.

### Example 2: Agreement rescue

User says: "Boxes all over the place."

Actions:

1. Guideline rewritten
2. Agreement 0.6 to 0.9
3. mAP +12
4. Process kept

Result: Quality annotations.

## Troubleshooting

### mAP plateaus low

Cause: Noisy boxes or wrong priors

Fix:

1. Audit boxes
2. Check anchors/strides
3. Fix labels first
4. Then tune model

### Dense crowds merge

Cause: NMS too aggressive

Fix:

1. Soften NMS
2. Tune per class
3. Verify on crowds
4. Document settings

### Val/test gap

Cause: Scene leakage across splits

Fix:

1. Split by scene/video
2. Decontaminate
3. Re-eval honestly
4. Lock procedure

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Guide.
- Data.
- Ship.

## Decision Heuristic

Before adding complexity, ask:

1. What outcome requires this step?
2. What evidence justifies it?
3. What happens when it fails?
4. What is the cheaper alternative?
5. What proves quality did not regress?
6. What must be logged for audit?
7. What is the rollback plan?

If the main justification is "more", prove the outcome needs it first.

## Anti-Patterns

Avoid guideline-free annotation; unvalidated COCO; random-frame splits; single-number mAP; size-blind eval; agreement-blind QA.

## Bundled References

Read `references/detection-ops.md` when annotating or training detectors.
Run `scripts/boxes_audit.py` to validate COCO annotations.
Copy `assets/checklists.md` into every delivery.
