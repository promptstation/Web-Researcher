---
name: mining-measurement-ethics
description: Keep web mining honest with audits, bias checks, and open methods. Use when the user asks to audit dataset bias; measure corpus representativeness; publish mining methodology; review scraping ethics; correct published analysis.
compatibility: Reference populations for audits; ethics review for sensitive mining; versioned methods.
metadata:
  author: Promptstation
  version: 1.0.0
  category: data-mining
---

# Mining Measurement Ethics

Mine truthfully. You audit representativeness, measure bias, respect consent boundaries, publish methods with limits, and correct errors openly — earning trust for every claim.

Optimize simultaneously for:

- audited coverage
- measured bias
- respected consent
- open methods
- owned errors

No claim beyond what the sample supports; no mining past consent boundaries.

## Use Cases

### Bias audit

Trigger: user says 'is our data biased' or 'check representativeness'

Steps:

1. Define population
2. Measure gaps
3. Fix or disclose
4. Report

Result: Known bias posture.

### Publish study

Trigger: user says 'publish analysis' or 'share findings'

Steps:

1. Document method
2. State limits
3. Share repro
4. Invite scrutiny

Result: Credible publication.

### Correction

Trigger: user says 'we were wrong' or 'data error found'

Steps:

1. Scope error
2. Fix + disclose
3. Notify affected
4. Prevent repeat

Result: Trust preserved.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Population definition
- Coverage audit
- Bias metrics
- Consent record
- Methodology doc
- Limit statement
- Repro package
- Correction log

Never generalize beyond the sample or hide methods, limits, or errors.

## Phase 1 — Audit Coverage

Run `scripts/coverage_audit.py --known urls.txt --crawled fetched.txt`.

Gaps by segment explained.

Fix or disclose each.

## Phase 2 — Measure Bias

Selection vs population.

Algorithmic skew in outputs.

Report with uncertainty.

## Phase 3 — Respect Boundaries

Consent, ToS, privacy reviewed.

Sensitive mining ethics-approved.

PII minimized/redacted.

## Phase 4 — Publish and Correct

Method + limits + repro.

Corrections logged openly.

Review before publish.

## Examples

### Example 1: Gap owned

User says: "Study questioned on sample."

Actions:

1. Audit showed skew
2. Disclosed + weighted
3. Credibility kept
4. Method improved

Result: Honest science.

### Example 2: Error fixed

User says: "Bug in published numbers."

Actions:

1. Scoped in a day
2. Corrected openly
3. Notified users
4. Checks added

Result: Trust intact.

## Troubleshooting

### Population unknown

Cause: No reference stats

Fix:

1. Triangulate sources
2. State assumptions
3. Limit claims
4. Improve iteratively

### Consent gray

Cause: Novel mining use

Fix:

1. Pause and review
2. Legal + ethics
3. Document decision
4. Proceed or stop

### Repro fails

Cause: Undocumented steps

Fix:

1. Package code+data+seeds
2. Test fresh clone
3. Fix gaps
4. Publish v2

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Audit.
- Bound.
- Share.

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

Avoid sample-blind claims; bias-blind mining; consent-gray proceeding; method-hiding; limit-free conclusions; correction-free errors.

## Bundled References

Read `references/honest-mining.md` when auditing or publishing mining.
Run `scripts/coverage_audit.py` to audit crawl coverage.
Copy `assets/checklists.md` into every delivery.
