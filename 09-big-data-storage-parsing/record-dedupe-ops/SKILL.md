---
name: record-dedupe-ops
description: Dedupe corpora exactly and nearly, with ruled merges and proof. Use when the user asks to dedupe scraped records; find near-duplicate listings; design record IDs; merge duplicate entities; measure duplication rates.
compatibility: Python 3.10+; datasketch optional for MinHash at scale; ledger store per volume.
metadata:
  author: Promptstation
  version: 1.0.0
  category: data-engineering
---

# Record Dedupe Ops

Keep every record once. You derive stable IDs, dedupe exactly at write, hunt near-dupes with shingles, merge by survivorship rules with audits, and prove cleanliness with measured rates.

Optimize simultaneously for:

- stable IDs
- exact cleanliness
- found near-dupes
- ruled merges
- proven rates

Merge only by written survivorship rules with audit trails; never auto-merge across entity types.

## Use Cases

### Dirty corpus

Trigger: user says 'duplicates everywhere' or 'clean this dataset'

Steps:

1. Derive IDs
2. Exact pass
3. Near pass sampled
4. Merge ruled

Result: Clean corpus.

### Cross-run dupes

Trigger: user says 'dupes after resume' or 're-crawl doubles'

Steps:

1. Ledger gate writes
2. Conditional upserts
3. Reconcile
4. Prove zero

Result: Idempotent corpus.

### Entity merge

Trigger: user says 'same product twice' or 'merge listings'

Steps:

1. Score pairs
2. Apply rules
3. Audit merges
4. Review edge cases

Result: Merged entities.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- ID spec
- Exact-dedupe proof
- Near-dup method
- Survivorship rules
- Merge audit log
- Dup dashboard
- Threshold tuning
- Backfill report

Never merge without rules and audits, and never claim clean without measured rates.

## Phase 1 — Derive IDs

Canonical input plus version, hashed.

Test stability and uniqueness.

Index IDs everywhere.

## Phase 2 — Dedupe Exactly

Ledger-gate every write.

Run `scripts/dedupe_scan.py --in corpus.jsonl --key record_id`.

Reconcile counts.

## Phase 3 — Hunt Near-Dupes

Shingle titles/descriptions; Jaccard threshold.

Sample pairs for review.

Tune threshold by precision.

## Phase 4 — Merge Ruled

Newest/complete wins per field.

Audit every merge.

Human-review low-confidence.

## Examples

### Example 1: Listing cleanup

User says: "30 percent dup listings."

Actions:

1. IDs plus exact pass to 8
2. Near pass to 1.5
3. Ruled merges
4. Rate dashboard live

Result: Clean catalog.

### Example 2: Resume safety

User says: "Re-crawls double rows."

Actions:

1. Ledger gates
2. Upserts
3. Kill-test proven
4. Dupes zero

Result: Idempotent growth.

## Troubleshooting

### IDs unstable

Cause: Volatile derivation inputs

Fix:

1. Canonicalize inputs
2. Pin versions
3. Rebuild once
4. Test stability

### Near-dup noise

Cause: Threshold too loose

Fix:

1. Raise threshold
2. Add blocking keys
3. Review samples
4. Tune precision

### Merge regret

Cause: Rules too aggressive

Fix:

1. Tighten rules
2. Restore from audit
3. Human-review band
4. Re-verify

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- ID.
- Clean.
- Keep.

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

Avoid ID-free corpora; gate-free writes; threshold-free near-dupes; rule-free merges; audit-free dedupe; rate-blind claims.

## Bundled References

Read `references/dedupe-methods.md` when deduping corpora or merging entities.
Run `scripts/dedupe_scan.py` to find exact and shingle near-duplicates.
Copy `assets/checklists.md` into every delivery.
