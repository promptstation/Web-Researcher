---
name: cv-preprocessing
description: Preprocess and augment images with inspected, task-matched pipelines. Use when the user asks to preprocess images for training; design augmentation policy; normalize image inputs; inspect augmented samples; fix aspect ratio distortion.
compatibility: Python 3.10+; Pillow/torchvision/albumentations per stack; image viewer for inspection.
metadata:
  author: Promptstation
  version: 1.0.0
  category: computer-vision
---

# CV Preprocessing

Feed models clean varied pixels. You resize without distortion, normalize per model, augment only task-true invariances, inspect hundreds of samples by eye, and freeze eval transforms deterministic.

Optimize simultaneously for:

- safe geometry
- right normalization
- true augmentations
- inspected samples
- frozen eval

Augment only invariances the task truly has; inspect before training, always.

## Use Cases

### New pipeline

Trigger: user says 'prepare images' or 'augmentation for X'

Steps:

1. Design per task
2. Inspect 100+
3. Freeze eval
4. Document policy

Result: Trusted pipeline.

### Augment harm

Trigger: user says 'augmentation hurts' or 'weird crops'

Steps:

1. Inspect failures
2. Ablate each op
3. Keep winners
4. Re-verify

Result: Helping augmentations.

### Eval mismatch

Trigger: user says 'train/val gap odd' or 'eval unstable'

Steps:

1. Freeze eval fully
2. Diff transforms
3. Fix leakage
4. Verify stable

Result: Honest eval.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Transform spec
- Normalization values
- Augmentation policy
- Inspection samples
- Eval spec frozen
- Seed record
- Ablation notes
- Version pin

Never augment away task signal or train with uninspected transforms.

## Phase 1 — Design Transforms

Geometry safe for the task (pad vs stretch).

Normalize per model card.

Augment true invariances only.

## Phase 2 — Inspect Samples

Render 100+ augmented with labels.

Check signal survives each op.

Prototype geometry on PPM with `scripts/ppm_resize.py`.

## Phase 3 — Freeze Eval

Deterministic resize/center-crop/normalize.

No randomness, no augmentation.

Version with model.

## Phase 4 — Ablate

One op off at a time.

Keep measured winners.

Document policy.

## Examples

### Example 1: OCR rescue

User says: "Rotation aug kills OCR."

Actions:

1. Inspected: text unreadable
2. Limited to +-3 deg
3. Accuracy +9
4. Policy filed

Result: Task-true augmentation.

### Example 2: Aspect fix

User says: "Squished products misclassify."

Actions:

1. Stretch to pad
2. Error down 30 percent
3. Eval frozen
4. Shipped

Result: Geometry respected.

## Troubleshooting

### Train/val gap grows

Cause: Augmentation too strong or eval leaks

Fix:

1. Soften policy
2. Freeze eval
3. Ablate ops
4. Re-measure

### Color aug harms

Cause: Color is signal (ripeness, brand)

Fix:

1. Drop color jitter
2. Keep geometric
3. Verify
4. Document why

### Slow pipeline

Cause: CPU-bound transforms

Fix:

1. Cache decoded
2. Vectorize ops
3. Workers tuned
4. Profile hot path

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Design.
- See.
- Lock.

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

Avoid stretch-by-default; uninspected augmentation; signal-destroying ops; random eval; norm-guessing; ablation-free policies.

## Bundled References

Read `references/transform-policy.md` when designing transforms or augmentations.
Run `scripts/ppm_resize.py` to demo safe resize geometry on PPM.
Copy `assets/checklists.md` into every delivery.
