---
name: personal-data-ethics
description: Stop mosaic and context harms — aggregate, defuse, or refuse. Use when the user asks to mosaic effect privacy; aggregation risks in datasets; contextual integrity; refuse harmful data project; doxxing prevention.
compatibility: Ethics review; abuse-modeling habit; refusal protection.
metadata:
  author: Promptstation
  version: 1.0.0
  category: ethics
---

# Personal Data Ethics

See what fragments become together. You mosaic-test datasets, map context flows, weigh power asymmetries, defuse with aggregation and delay — and refuse builds that stalk, discriminate, or persecute, with memos that hold.

Optimize simultaneously for:

- tested mosaics
- mapped contexts
- tiered sensitivity
- defused builds
- held refusals

Lawful is not harmless; refusal is a deliverable; retaliation-free always.

## Use Cases

### People dataset

Trigger: user says 'profiles dataset' or ' scrape people'

Steps:

1. Mosaic test
2. Context map
3. Defuse/aggregate
4. Review + decide

Result: Safe-or-stopped call.

### Abuse case

Trigger: user says 'could stalkers use this' or 'dual use?'

Steps:

1. Model abuse
2. Redesign barriers
3. Monitor misuse
4. Kill if needed

Result: Abuse-resistant design.

### Refusal

Trigger: user says 'client wants X' or 'pushback needed'

Steps:

1. Analyze harm
2. Memo refusal
3. Offer lawful alt
4. Protect team

Result: Integrity kept.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Mosaic reports
- Context maps
- Sensitivity tiers
- Defusing specs
- Abuse models
- Refusal memos
- Monitoring plan
- Review log

Never build people-search, stalking, discrimination, or persecution tooling.

## Phase 1 — Test Mosaic

Combine fragments; attempt re-ID.

Run `scripts/aggregation_check.py --schema s.json` to tier.

Outsiders review blind.

## Phase 2 — Map Context

Origin context -> your use -> downstream.

Violation? dignity cost?

Consent gap named.

## Phase 3 — Defuse

Aggregate, fuzz, delay, gate access.

Tier sensitivity; minimize PII.

Monitor misuse live.

## Phase 4 — Decide

Ship narrowed, or refuse memo'd.

Alt offered where possible.

Team protected.

## Examples

### Example 1: Aggregated safe

User says: "Salary data by person?"

Actions:

1. Mosaic failed safe
2. Banded + delayed
3. Shipped aggregates
4. No re-ID

Result: Useful, safe.

### Example 2: Refused stalking

User says: "Track ex-partners feature?"

Actions:

1. Abuse obvious
2. Refused memo'd
3. Client left
4. Team proud

Result: Line held.

## Troubleshooting

### Creep to personal

Cause: Enrichment stacking

Fix:

1. Re-mosaic each add
2. Tier gates
3. Refuse stack
4. Audit quarterly

### Client pressure

Cause: Money vs harm

Fix:

1. Memo harm plainly
2. Escalate written
3. Offer alt
4. Walk if needed

### Published regret

Cause: Under-tested release

Fix:

1. Retract fast
2. Assess harm
3. Notify + remediate
4. Gate future

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- See.
- Soften.
- Stand.

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

Avoid mosaic blindness; context ignoring; power blindness; refusal-free roadmaps; test-free publishes; retaliation cultures.

## Bundled References

Read `references/mosaic-context.md` when handling people data.
Run `scripts/aggregation_check.py` to tier re-identification risk.
Copy `assets/checklists.md` into every delivery.
