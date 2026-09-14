---
name: image-classification-ops
description: Ship calibrated image classifiers with stratified splits and sliced error analysis. Use when the user asks to train an image classifier; fine-tune a vision model; handle imbalanced classes; calibrate model probabilities; analyze classification errors.
compatibility: PyTorch or TF; pretrained backbones; experiment tracking (MLflow/Weights).
metadata:
  author: Promptstation
  version: 1.0.0
  category: computer-vision
---

# Image Classification Ops

Ship classifiers that earn trust. You split stratified with locked tests, fine-tune schedules that converge, fix imbalance properly, calibrate for thresholds, and slice errors into data fixes — shipping only on criteria.

Optimize simultaneously for:

- clean splits
- converged models
- fair classes
- honest probabilities
- fixed errors

Test set touched once for ship decision; no threshold without calibration.

## Use Cases

### New classifier

Trigger: user says 'classify product photos' or 'train model'

Steps:

1. Split stratified
2. Fine-tune baseline
3. Fix imbalance
4. Analyze and ship

Result: Shipped classifier.

### Rare class fails

Trigger: user says 'minority class ignored' or 'recall low'

Steps:

1. Measure per class
2. Sample and weight
3. Collect targeted
4. Verify lift

Result: Fair classifier.

### Threshold pick

Trigger: user says 'what threshold' or 'too many false alarms'

Steps:

1. Calibrate
2. Cost-tune threshold
3. Verify on test
4. Monitor live

Result: Cost-right threshold.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Split record seeded
- Training config
- Class metrics
- Calibration plot data
- Error slices
- Threshold rationale
- Model card
- Ship checklist

Never tune on test or ship uncalibrated thresholds.

## Phase 1 — Split Right

Stratify by class; seed and record.

Use `scripts/split_dataset.py --manifest m.jsonl` for splits.

Lock test; touch once.

## Phase 2 — Train Baseline

Pretrained backbone; LR finder; cosine schedule.

Early stop on val; track everything.

Reproduce best twice.

## Phase 3 — Fix Imbalance

Weighted sampling first; class weights; focal if needed.

Targeted collection for worst classes.

Report per-class always.

## Phase 4 — Calibrate and Ship

Temperature/ECE check; cost-tuned threshold.

Error slices to data fixes.

Ship on criteria; model card filed.

## Examples

### Example 1: Rare defect

User says: "Defect class recall 40 percent."

Actions:

1. Weighted sampling plus 500 targeted
2. Recall to 88
3. Shipped with monitor
4. Line trusts it

Result: Fair detector.

### Example 2: Threshold right

User says: "Too many false rejects."

Actions:

1. Calibrated, cost-tuned
2. False down 60, miss flat
3. Locked with card
4. Stable

Result: Cost-right ops.

## Troubleshooting

### Val oscillates

Cause: LR too high or tiny val

Fix:

1. Lower LR, longer warmup
2. Bigger val
3. EMA weights
4. Re-run seeded

### Overfits fast

Cause: Small data or huge head

Fix:

1. Freeze backbone longer
2. Stronger aug
3. Dropout/WD
4. More data targeted

### Calibrated on val, off live

Cause: Distribution shift

Fix:

1. Monitor live ECE
2. Recalibrate scheduled
3. Slice the shift
4. Adapt data

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Split.
- Train.
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

Avoid unstratified splits; test-peeking; accuracy-only; uncalibrated thresholds; slice-blind errors; criteria-free shipping.

## Bundled References

Read `references/classifier-ops.md` when training or shipping classifiers.
Run `scripts/split_dataset.py` to make stratified seeded splits.
Copy `assets/checklists.md` into every delivery.
