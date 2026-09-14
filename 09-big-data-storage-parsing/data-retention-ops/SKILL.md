---
name: data-retention-ops
description: Govern dataset lifecycles with retention, archival, and provable deletion. Use when the user asks to set data retention policy; archive old datasets; prove GDPR deletion; handle erasure requests; restore from cold archive.
compatibility: Cold storage (S3 Glacier, tape, offline disk); backup alignment; legal sign-off on schedules.
metadata:
  author: Promptstation
  version: 1.0.0
  category: data-engineering
---

# Data Retention Ops

End every byte's life on purpose. You schedule retention from need, archive cold with tested restores, delete with manifest proof, handle erasure end to end, and pack evidence for every audit.

Optimize simultaneously for:

- scheduled retention
- tested archives
- proven deletes
- handled DSARs
- packed evidence

No data kept past schedule without exception; no deletion claimed without proof.

## Use Cases

### Retention live

Trigger: user says 'too much old data' or 'set retention'

Steps:

1. Schedule per dataset
2. Automate sweeps
3. Prove deletes
4. Report quarterly

Result: Lean compliant estate.

### Erasure request

Trigger: user says 'delete my data' or 'DSAR arrived'

Steps:

1. Find all copies
2. Delete plus backups
3. Verify absence
4. Respond with proof

Result: Honored erasure.

### Audit evidence

Trigger: user says 'prove lifecycle' or 'regulator asks'

Steps:

1. Pull schedules
2. Show proofs
3. List exceptions
4. File pack

Result: Passed audit.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Retention table
- Archive manifests
- Restore-test log
- Deletion proofs
- DSAR log
- Backup policy
- Exception register
- Evidence packs

Never keep past schedule silently or claim deletion without verification.

## Phase 1 — Schedule

Per dataset: hot, warm, cold, delete ages.

Legal sign-off; review yearly.

Dry-run with `scripts/retention_sweep.py --root data/ --older-than 365 --dry-run`.

## Phase 2 — Archive Cold

Manifest plus checksums.

Restore-test quarterly.

Track retrieval cost.

## Phase 3 — Delete Provably

Drop partitions; diff manifests.

Verify absence (search + sample).

File proof with dates.

## Phase 4 — Serve DSARs

Find across layers plus backups.

Delete and verify.

Respond within SLA with proof.

## Examples

### Example 1: Estate diet

User says: "Storage bill scary."

Actions:

1. Scheduled all
2. Archived cold 70 percent
3. Deleted 20 provably
4. Bill down 60

Result: Lean estate.

### Example 2: DSAR honored

User says: "Erasure request Friday."

Actions:

1. Found 14 copies
2. Deleted all + backups
3. Verified absent
4. Responded Monday with proof

Result: Trusted handling.

## Troubleshooting

### Restore fails

Cause: Untested archives

Fix:

1. Test restores quarterly
2. Fix format drift
3. Document steps
4. Alert on fail

### Copies missed

Cause: Shadow stores

Fix:

1. Inventory all stores
2. Centralize writes
3. Scan for strays
4. Prevent recurrence

### Exceptions rot

Cause: Undated holds

Fix:

1. Date every hold
2. Owner each
3. Review monthly
4. Expire loudly

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Plan.
- Run.
- Serve.

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

Avoid schedule-free hoarding; untested archives; proof-free deletes; backup-blind erasure; SLA-free DSARs; exception rot.

## Bundled References

Read `references/lifecycle-governance.md` when scheduling retention or serving erasure.
Run `scripts/retention_sweep.py` to dry-run retention sweeps.
Copy `assets/checklists.md` into every delivery.
