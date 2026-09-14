---
name: data-minimization-ops
description: Keep every pipeline minimal by design, default, and proof. Use when the user asks to review data necessity; minimize PII collection; allowlist scraped fields; aggregate personal data; prove data minimization.
compatibility: Schema control per flow; review ritual; audit access to stores.
metadata:
  author: Promptstation
  version: 1.0.0
  category: privacy-law
---

# Data Minimization Ops

Collect the least that works. You necessity-review every field, allowlist collection, aggregate early, delete by default, and prove minimal with audits and shrinking metrics.

Optimize simultaneously for:

- reviewed fields
- guarded flows
- early aggregates
- deleting defaults
- proven minimal

Fields guilty until proven necessary; PII dropped at the earliest point possible.

## Use Cases

### Flow diet

Trigger: user says 'collecting too much' or 'trim this flow'

Steps:

1. Review fields
2. Drop unneeded
3. Guard allowlist
4. Verify minimal

Result: Lean flow.

### PII scrub

Trigger: user says 'PII everywhere' or 'reduce exposure'

Steps:

1. Find PII
2. Drop/mask/aggregate
3. Verify gone
4. Monitor

Result: Smaller footprint.

### Audit proof

Trigger: user says 'prove minimal' or 'regulator asks'

Steps:

1. Pull reviews
2. Show metrics
3. Explain holds
4. File pack

Result: Evidenced minimal.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Field inventory
- Necessity decisions
- Allowlist configs
- Aggregation specs
- Delete defaults
- Hold register
- Min metrics
- Audit reports

Never collect just-in-case fields or keep PII past necessity.

## Phase 1 — Review Fields

Every field: purpose link or drop.

Run `scripts/field_audit.py --schema s.json` to scaffold.

Decide keep/drop/mask/aggregate.

## Phase 2 — Guard Flows

Allowlist fields in code.

PII guards at ingest.

Break builds on new PII.

## Phase 3 — Aggregate Early

Detail only where needed.

Anonymize with tested methods.

Document residual risk.

## Phase 4 — Delete Default

TTL everywhere; holds dated.

Prove with scans.

Trend metrics down.

## Examples

### Example 1: Flow halved

User says: "60 fields, most unused."

Actions:

1. Reviewed: 28 kept
2. Allowlisted
3. Usage verified
4. Footprint halved

Result: Minimal flow.

### Example 2: Exposure cut

User says: "Emails in 5 stores."

Actions:

1. Dropped 4, masked 1
2. Verified absent
3. Breach radius shrunk
4. Monitored

Result: Safer estate.

## Troubleshooting

### Just-in-case pressure

Cause: Future-use hoarding

Fix:

1. Decide on purpose now
2. Re-collect later if based
3. Log refusal
4. Hold the line

### Anonymization theater

Cause: Weak de-identification

Fix:

1. Test re-identification
2. Strengthen properly
3. State residual
4. Expert review

### Hold sprawl

Cause: Undated legal holds

Fix:

1. Date every hold
2. Owner each
3. Review monthly
4. Release loudly

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Review.
- Guard.
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

Avoid just-in-case fields; collect-all extractors; review-free schemas; hold sprawl; theater anonymization; metric-free minimal.

## Bundled References

Read `references/minimization-proof.md` when minimizing or auditing.
Run `scripts/field_audit.py` to scaffold field necessity reviews.
Copy `assets/checklists.md` into every delivery.
