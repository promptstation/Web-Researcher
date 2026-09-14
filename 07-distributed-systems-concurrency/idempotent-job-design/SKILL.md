---
name: idempotent-job-design
description: Turn at-least-once delivery into exactly-once effects. Use when the user asks to dedupe pipeline outputs; design idempotency keys; prevent duplicate records; add a transactional outbox; prove exactly-once processing.
compatibility: Python 3.10+; SQLite/Postgres for ledgers; no frameworks required.
metadata:
  author: Promptstation
  version: 1.0.0
  category: distributed-systems
---

# Idempotent Job Design

Make replays boring. You derive stable keys, keep ledgers that survive crashes, write conditionally, outbox side effects, and prove exactly-once with kill tests and reconciliation.

Optimize simultaneously for:

- stable keys
- durable ledgers
- convergent writes
- once-only side effects
- proofs filed

No handler ships without key, ledger check, and kill-test proof.

## Use Cases

### Duplicate records

Trigger: user says 'dupes after resume' or 'double writes'

Steps:

1. Derive keys
2. Add ledger gate
3. Make writes conditional
4. Prove with replay

Result: Convergent pipeline.

### Notify once

Trigger: user says 'double alerts' or 'webhook twice'

Steps:

1. Outbox the intent
2. Relay with keys
3. Dedupe downstream
4. Verify once

Result: Once-only side effects.

### Reconciliation

Trigger: user says 'prove completeness' or 'audit a run'

Steps:

1. Count inputs, outputs, ledger
2. Diff the three
3. Explain every gap
4. File the report

Result: Audited run.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Key derivation spec
- Ledger schema plus TTL
- Conditional-write map
- Outbox design
- Kill-test evidence
- Reconciliation report
- Version policy
- Replay runbook

Never emit without keys or side-effect without outbox.

## Phase 1 — Derive Keys

Key = hash(canonical input + extractor version).

Document derivation with examples.

Test stability across runs.

## Phase 2 — Gate with Ledger

Use `scripts/idempotency_ledger.py` for seen-key gating.

Check-then-write atomically where possible.

Set TTLs by retention need.

## Phase 3 — Condition Writes

Upserts on keys; conditional puts.

Outbox for notifications and webhooks.

Relay idempotently downstream.

## Phase 4 — Prove It

Kill -9 mid-run; replay; count.

Reconcile inputs, outputs, ledger.

File the proof.

## Examples

### Example 1: Resume dupes

User says: "Resumes double 5 percent of rows."

Actions:

1. Keys derived, ledger gated
2. Upserts replaced inserts
3. Kill-test clean 3x
4. Dupes zero

Result: Exactly-once resume.

### Example 2: Double webhooks

User says: "Partners complain of duplicates."

Actions:

1. Outboxed intents
2. Relay with keys
3. Downstream dedupe
4. Complaints ended

Result: Once-only delivery.

## Troubleshooting

### Keys unstable across runs

Cause: Volatile fields in derivation

Fix:

1. Canonicalize inputs
2. Pin extractor version
3. Test stability
4. Rebuild ledger once

### Ledger grows forever

Cause: No TTL or retention

Fix:

1. Set TTL by need
2. Compact routinely
3. Archive cold keys
4. Monitor size

### Check-then-write races

Cause: Non-atomic gate

Fix:

1. Use conditional writes
2. Serialize per key
3. Accept rare dup + reconcile
4. Measure residual

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Keys.
- Gate.
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

Avoid keyless handlers; volatile keys; insert-only writes; direct side effects; unproven exactly-once; ledger-free replays.

## Bundled References

Read `references/idempotency-patterns.md` when designing keys, ledgers, or outboxes.
Run `scripts/idempotency_ledger.py` as a seen-key gate over sqlite.
Copy `assets/checklists.md` into every delivery.
