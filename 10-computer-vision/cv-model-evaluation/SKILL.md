---
name: cv-model-evaluation
description: Evaluate vision honestly with slices, robustness, fairness, and galleries. Use when the user asks to evaluate a vision model; slice model metrics; test robustness to corruption; audit model fairness; build error galleries.
compatibility: Locked test sets; slice metadata; fairness review with domain care.
metadata:
  author: Promptstation
  version: 1.0.0
  category: computer-vision
---

# CV Model Evaluation

Know exactly where models fail. You slice beyond headlines, calibrate for thresholds, probe corruptions and shifts, audit sensitive slices carefully, and gallery errors into data fixes — gating ships on all of it.

Optimize simultaneously for:

- sliced truth
- honest calibration
- known robustness
- audited fairness
- fixed errors

No ship without sliced eval; sensitive slices reviewed with domain and ethics care.

## Use Cases

### Ship review

Trigger: user says 'is this model ready' or 'eval this'

Steps:

1. Slice full
2. Calibrate check
3. Probe robust
4. Gate decision

Result: Honest ship call.

### Failure hunt

Trigger: user says 'where does it fail' or 'bad cases'

Steps:

1. Gallery errors
2. Cluster causes
3. Fix data top 3
4. Verify lift

Result: Targeted improvement.

### Fairness check

Trigger: user says 'works for everyone?' or 'bias audit'

Steps:

1. Slice sensitively
2. Measure gaps
3. Fix data/model
4. Re-audit

Result: Fairer model.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Slice plan
- Sliced metrics
- Calibration report
- Robustness scores
- Fairness review
- Error gallery
- Fix backlog
- Gate decision

Never ship on headline metrics or skip fairness review for people-facing models.

## Phase 1 — Slice Metrics

Class, size, source, lighting, geo, demographic.

Run `scripts/metrics_report.py --preds preds.csv` for base tables.

Worst-slice floors as gates.

## Phase 2 — Calibrate and Probe

ECE plus reliability by slice.

Corruptions: blur, noise, JPEG, light, occlude.

Shift sets where available.

## Phase 3 — Audit Fairly

Sensitive slices with consent-aware data.

Gaps measured with uncertainty.

Mitigate data-first.

## Phase 4 — Gallery and Gate

100-error galleries reviewed.

Top-3 fixes shipped and verified.

Gate decision recorded.

## Examples

### Example 1: Slice saved ship

User says: "92 percent accurate, ship it?"

Actions:

1. Sliced: dark-skin 74
2. Fixed data, re-eval 89
3. Gates passed
4. Shipped fairly

Result: Responsible ship.

### Example 2: Robustness known

User says: "Fails in rain?"

Actions:

1. Corruption probe answered
2. Limits documented
3. Fallback added
4. Deployed scoped

Result: Scoped deployment.

## Troubleshooting

### Slices too small

Cause: Rare buckets

Fix:

1. Report with CI
2. Pool carefully
3. Collect targeted
4. Gate on pooled

### Gallery ignored

Cause: No review ritual

Fix:

1. Weekly review
2. Owner per cluster
3. Fixes tracked
4. Verify lift

### Fairness data lacking

Cause: No consented attributes

Fix:

1. Proxy carefully or collect
2. State limits
3. External audit
4. Never guess-attributed

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Slice.
- Probe.
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

Avoid headline-only eval; slice-free ships; calibration-free thresholds; probe-free deploys; fairness-free people-models; gallery-free iteration.

## Bundled References

Read `references/vision-eval.md` when evaluating vision models.
Run `scripts/metrics_report.py` to report classification metrics.
Copy `assets/checklists.md` into every delivery.
