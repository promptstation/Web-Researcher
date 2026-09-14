---
name: incremental-collection
description: Fetch, compare, and emit only what changed — provably complete. Use when the user asks to incremental scraping; detect changed pages only; emit delta updates; track crawl high-water marks; reduce re-crawl costs.
compatibility: Python 3.10+; state store (SQLite) for hashes and watermarks; source change signals where offered.
metadata:
  author: Promptstation
  version: 1.0.0
  category: data-engineering
---

# Incremental Collection

Stop paying full price for unchanged data. You check cheap signals first, hash normalized content, watermark every source, emit pure deltas, detect deletes, and reconcile every increment to prove completeness.

Optimize simultaneously for:

- cheap checks
- stable hashes
- kept watermarks
- pure deltas
- proven completeness

Every increment reconciled; deletes detected, never assumed; full re-crawl path always available.

## Use Cases

### Cost cut

Trigger: user says 're-crawl everything nightly' or 'cut fetch cost'

Steps:

1. Add change signals
2. Hash and compare
3. Emit deltas
4. Verify savings

Result: Delta-priced freshness.

### Delete detection

Trigger: user says 'removed listings linger' or 'find deletes'

Steps:

1. Track seen sets
2. Confirm absences
3. Emit deletes
4. Verify precision

Result: Accurate catalog.

### Freshness proof

Trigger: user says 'prove we are current' or 'audit increments'

Steps:

1. Reconcile counts
2. Show lag
3. List gaps
4. File report

Result: Audited currency.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Signal map per source
- Normalization spec
- Hash store
- Watermark table
- Delta format
- Reconciliation report
- Backfill bounds
- Cost tracking

Never skip reconciliation or treat absence-once as deletion.

## Phase 1 — Signal First

Etag, lastmod, sitemap, HEAD before GET.

Skip unchanged with logged proof.

Measure skip rate.

## Phase 2 — Hash Compare

Normalize (strip volatile regions).

Run `scripts/delta_emit.py --in new.jsonl --state hashes.db`.

Changed-only downstream.

## Phase 3 — Watermark

Per-source high-water marks.

Resume from marks.

Alert on stuck marks.

## Phase 4 — Reconcile

Inputs vs emitted vs skipped.

Deletes confirmed 2x.

File the report.

## Examples

### Example 1: 80 percent cut

User says: "Nightly full crawl bankrupting us."

Actions:

1. Signals plus hashing
2. Fetches down 80
3. Freshness same
4. Savings tracked

Result: Cheap freshness.

### Example 2: Deletes right

User says: "Dead listings persist."

Actions:

1. Seen-set tracking
2. 2x confirm deletes
3. Precision 99
4. Catalog true

Result: Living catalog.

## Troubleshooting

### Hash churn

Cause: Volatile regions unnormalized

Fix:

1. Normalize timestamps/ads
2. Re-baseline hashes
3. Verify stability
4. Monitor churn

### Missed changes

Cause: Weak signals trusted blindly

Fix:

1. Periodic full verify
2. Hash spot-checks
3. Fix signal gaps
4. Reconcile always

### Watermark stuck

Cause: Poison item blocks advance

Fix:

1. Skip with quarantine
2. Advance past
3. Alert loudly
4. Fix and replay

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Signal.
- Compare.
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

Avoid full-crawl-by-default; signal-free refetch; volatile hashing; mark-free resumes; absence-once deletes; reconciliation-free increments.

## Bundled References

Read `references/incremental-design.md` when building delta pipelines.
Run `scripts/delta_emit.py` to emit deltas against a hash state.
Copy `assets/checklists.md` into every delivery.
