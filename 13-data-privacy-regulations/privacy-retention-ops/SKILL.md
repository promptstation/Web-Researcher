---
name: privacy-retention-ops
description: Enforce retention with automated deletion and absence proofs. Use when the user asks to schedule data retention; automate GDPR deletion; align backups with erasure; verify data deletion; manage legal holds.
compatibility: Delete access per store; backup cooperation; verification search tooling.
metadata:
  author: Promptstation
  version: 1.0.0
  category: privacy-law
---

# Privacy Retention Ops

Keep nothing past its time. You schedule per purpose, automate deletion with dry-runs, align backups, verify absence by search, and file proofs — with holds dated and rare.

Optimize simultaneously for:

- scheduled stores
- running deletes
- aligned backups
- proven absence
- filed packs

No retention without legal sign-off; no deletion claim without verification.

## Use Cases

### Schedule live

Trigger: user says 'set retention' or 'storage limitation'

Steps:

1. Schedule signed
2. Automate deletes
3. Verify + file
4. Report quarterly

Result: Compliant lifecycle.

### Erasure proof

Trigger: user says 'prove deletion' or 'DSAR evidence'

Steps:

1. Delete scoped
2. Verify absent
3. Pack proof
4. Respond

Result: Believed deletion.

### Hold control

Trigger: user says 'litigation hold' or 'freeze deletes'

Steps:

1. Scope narrow
2. Date + owner
3. Suspend scoped
4. Release loudly

Result: Controlled hold.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Retention table signed
- Delete jobs
- Dry-run logs
- Backup policy
- Verification reports
- Proof packs
- Hold register
- Quarterly report

Never delete without dry-run review or claim deletion unverified.

## Phase 1 — Schedule Signed

Per store per purpose; legal signs.

Holds as dated exceptions.

Review yearly.

## Phase 2 — Automate Deletes

Jobs with dry-run first.

Approve-then-run for bulk.

Log every run.

## Phase 3 — Align Backups

Purge cycles or crypto-shred.

Restore-tests respect deletes.

Vendor backups included.

## Phase 4 — Verify and File

Search absence with `scripts/purge_prover.py --subject X`.

Sample-verify bulk purges.

File proof packs.

## Examples

### Example 1: Auto-clean

User says: "Logs pile forever."

Actions:

1. 90-day schedule
2. Auto-delete live
3. Verified quarterly
4. Footprint down 80

Result: Self-cleaning estate.

### Example 2: Proof accepted

User says: "Auditor doubts deletion."

Actions:

1. Search + samples shown
2. Backup cycle proven
3. Accepted
4. Template kept

Result: Trusted deletion.

## Troubleshooting

### Deletes fail

Cause: FK constraints or permissions

Fix:

1. Order deletes
2. Fix perms
3. Alert on fail
4. Re-run verified

### Backups resurrect

Cause: Unaligned restores

Fix:

1. Purge-cycle policy
2. Restore checklists
3. Crypto-shred keys
4. Test restores

### Hold creep

Cause: Forgotten holds

Fix:

1. Monthly review
2. Auto-expire
3. Owner nag
4. Release loudly

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Plan.
- Run.
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

Avoid schedule-free hoarding; dry-run-free deletes; backup-blind erasure; verify-free claims; hold-forever freezes; pack-free purges.

## Bundled References

Read `references/deletion-proof.md` when deleting or proving erasure.
Run `scripts/purge_prover.py` to verify subject absence in files.
Copy `assets/checklists.md` into every delivery.
