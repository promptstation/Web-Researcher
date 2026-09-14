---
name: evidence-preservation-ops
description: Preserve evidence admissibly with hashes, custody, and holds. Use when the user asks to preserve digital evidence; chain of custody log; hash evidence files; legal hold runbook; prepare evidence for court.
compatibility: Counsel direction; write-once store; trusted timestamping.
metadata:
  author: Promptstation
  version: 1.0.0
  category: cyber-law
---

# Evidence Preservation Ops

Make evidence court-ready. You collect write-once with runbooks, hash everything at capture, log every custody move immutably, timestamp trustworthily, and align holds narrowly — ready for expert scrutiny.

Optimize simultaneously for:

- clean collections
- honest hashes
- unbroken custody
- trusted times
- narrow holds

Counsel directs litigation evidence; never alter originals; spoliation is career-ending. Not legal advice.

## Use Cases

### Incident evidence

Trigger: user says 'preserve logs' or 'possible litigation'

Steps:

1. Freeze + collect
2. Hash + bag
3. Custody log
4. Hold scoped

Result: Admissible set.

### Scrape evidence

Trigger: user says 'prove page showed X' or 'capture for case'

Steps:

1. Forensic capture
2. Hash + time
3. Affidavit-ready notes
4. Store sealed

Result: Provable capture.

### Hold notice

Trigger: user says 'litigation hold' or 'preserve everything?'

Steps:

1. Scope narrow
2. Suspend deletes
3. Acknowledge all
4. Release loudly

Result: Compliant hold.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Collection runbook
- Method notes
- Hash manifests
- Custody log
- Timestamp proofs
- Hold notices
- Access log
- Verification reports

Never alter originals or break custody silence; never ignore hold notices.

## Phase 1 — Collect Clean

Runbook per source; method notes.

Write-once destination.

Bag with `scripts/evidence_bag.py --dir DIR`.

## Phase 2 — Hash and Time

sha256 at capture; manifest sealed.

Trusted timestamp (RFC3161 where apt).

Verify on receipt.

## Phase 3 — Custody Always

Every move logged: who/when/why.

Access least-privilege + logged.

Sealed storage; no silent copies.

## Phase 4 — Hold Narrow

Scope to matter; suspend deletes scoped.

Ack tracked; release loudly.

Counsel directs all.

## Examples

### Example 1: Logs saved

User says: "Breach may litigate."

Actions:

1. Frozen day 0
2. Bagged + custody
3. Hold scoped
4. Admitted cleanly

Result: Ready evidence.

### Example 2: Capture stands

User says: "Prove listing content."

Actions:

1. Forensic capture + hash
2. Timestamped
3. Notes affidavit-ready
4. Unchallenged

Result: Solid proof.

## Troubleshooting

### Originals touched

Cause: Live analysis

Fix:

1. Stop + document
2. Work copies only
3. Note deviation
4. Counsel assess

### Custody gap

Cause: Unlogged handoff

Fix:

1. Reconstruct now
2. Affidavit gap
3. Tighten process
4. Disclose honestly

### Hold overbroad

Cause: 'Keep everything'

Fix:

1. Narrow with counsel
2. Scope memo
3. Release rest
4. Review monthly

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Take.
- Seal.
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

Avoid original-touching; hash-free collections; custody gaps; timestamp-free claims; screenshot-only proof; hold-ignoring deletes.

## Bundled References

Read `references/evidence-handling.md` when preserving evidence.
Run `scripts/evidence_bag.py` to bag evidence folders.
Copy `assets/checklists.md` into every delivery.
