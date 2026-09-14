---
name: visual-privacy-ops
description: Find and redact visual PII with verified coverage and consent records. Use when the user asks to blur faces in images; redact license plates; audit images for PII; verify redaction coverage; manage photo consent.
compatibility: Face/plate detectors (OpenCV/DNN/cloud); redaction at ingest; consent store.
metadata:
  author: Promptstation
  version: 1.0.0
  category: computer-vision
---

# Visual Privacy Ops

Protect every pixel of identity. You detect faces, plates, and screens; redact matched to risk; verify with sampling and re-detection; record consent; and purge on schedule — with drills for exposures.

Optimize simultaneously for:

- found PII
- risk-matched redaction
- verified coverage
- recorded consent
- minimal retention

When in doubt, redact; identifiable images need consent or exclusion, never hope.

## Use Cases

### Dataset scrub

Trigger: user says 'faces in training data' or 'scrub this set'

Steps:

1. Detect all PII
2. Redact by risk
3. Verify sampled
4. Log coverage

Result: Safe dataset.

### Street imagery

Trigger: user says 'map photos' or 'dashcam frames'

Steps:

1. Faces plus plates
2. Blackout high-risk
3. Re-detect verify
4. Publish safe

Result: Publishable imagery.

### Exposure drill

Trigger: user says 'leaked unredacted' or 'PII drill'

Steps:

1. Contain copies
2. Assess scope
3. Notify per duty
4. Harden pipeline

Result: Handled exposure.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- PII inventory
- Detector eval
- Redaction policy
- Coverage report
- Consent records
- Retention schedule
- Access log
- Drill record

Never publish identifiable images without consent or claim redaction without verification.

## Phase 1 — Detect PII

Faces, plates, screens, badges, documents.

Eval detector recall on samples.

Inventory per image.

## Phase 2 — Redact by Risk

Blur for low, blackout for high risk.

Demo mechanics on PPM with `scripts/blur_boxes_ppm.py`.

Redact at ingest, keep originals locked.

## Phase 3 — Verify Coverage

Sample 5-10 percent by eye.

Re-run detector on redacted.

Fix gaps; re-verify.

## Phase 4 — Govern

Consent records; minimal retention.

Access logged; purges scheduled.

Drill exposures yearly.

## Examples

### Example 1: Scrubbed set

User says: "10k event photos to publish."

Actions:

1. Detected 3k faces
2. Blurred, verified 10 percent
3. Consents filed
4. Published safe

Result: Safe publication.

### Example 2: Gap caught

User says: "Are we fully redacted?"

Actions:

1. Re-detection found 2 percent
2. Fixed detector gap
3. Re-verified clean
4. Monitor added

Result: Proven coverage.

## Troubleshooting

### Detector misses

Cause: Profile/occluded/small faces

Fix:

1. Lower thresholds
2. Second detector
3. Sample harder
4. State residual risk

### Blur reversible

Cause: Light blur on high-res

Fix:

1. Blackout high-risk
2. Heavy pixelate min 16px
3. Test reversal
4. Policy by risk

### Consent gaps

Cause: Crowd or archival images

Fix:

1. Exclude or redact
2. Document basis
3. Legal review
4. Never assume

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Find.
- Hide.
- Prove.

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

Avoid detect-free publishing; reversible blur; verify-free redaction; consent-free faces; retention-free originals; drill-free teams.

## Bundled References

Read `references/visual-pii.md` when detecting or redacting visual PII.
Run `scripts/blur_boxes_ppm.py` to demo box redaction on PPM.
Copy `assets/checklists.md` into every delivery.
