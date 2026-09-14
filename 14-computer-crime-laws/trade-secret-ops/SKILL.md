---
name: trade-secret-ops
description: Never touch others' secrets; guard your own with reasonable measures. Use when the user asks to trade secret policy; handle leaked confidential data; quarantine secrets found scraping; classify confidential documents; NDA best practices.
compatibility: Counsel for finds; classification scheme; quarantine store.
metadata:
  author: Promptstation
  version: 1.0.0
  category: cyber-law
---

# Trade Secret Ops

Keep secrets where they belong. You recognize markers, vet sources, quarantine accidental finds with no-use rules, guard your own with classification and controls, and paper NDAs — auditing everything.

Optimize simultaneously for:

- recognized markers
- vetted sources
- quarantined finds
- guarded secrets
- papered NDAs

Found secrets: stop, quarantine, counsel — never use, share, or publish. Not legal advice.

## Use Cases

### Leak found

Trigger: user says 'scraped internal docs' or 'looks confidential'

Steps:

1. Stop + quarantine
2. Counsel now
3. No-use + delete?
4. File memo

Result: Clean hands.

### Insider offer

Trigger: user says 'ex-employee offers data' or 'shortcut source'

Steps:

1. Refuse + document
2. Report apt
3. Source lawfully
4. Train team

Result: Refused taint.

### Own secrets

Trigger: user says 'protect our methods' or 'classify docs'

Steps:

1. Classify + mark
2. Control access
3. NDA parties
4. Audit yearly

Result: Guarded edge.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Classification scheme
- Marker list
- Quarantine log
- Counsel memos
- Access matrix
- NDA files
- Exit checklists
- Audit reports

Never use, keep, or share found secrets, and never accept tainted sources.

## Phase 1 — Recognize

Markers: confidential/internal-only/NDA watermarks.

Scan with `scripts/secret_finder.py --root data/`.

Train teams on tells.

## Phase 2 — Avoid

Vet sources for legitimacy.

Refuse insider offers in writing.

Prefer public/licensed.

## Phase 3 — Quarantine

Stop use; isolate; counsel same-day.

No-use rule; delete-or-return per counsel.

Memo + file.

## Phase 4 — Guard Own

Classify, mark, gate access.

NDAs + exit hygiene.

Audit yearly.

## Examples

### Example 1: Clean hands

User says: "Crawl hit internal wiki."

Actions:

1. Quarantined in 1h
2. Counsel: delete + notify?
3. Deleted + logged
4. Source blocked

Result: No taint.

### Example 2: Offer refused

User says: "Competitor data offered cheap."

Actions:

1. Refused written
2. Reported to counsel
3. Sourced lawfully
4. Team praised

Result: Integrity kept.

## Troubleshooting

### Taint spread

Cause: Found data already used

Fix:

1. Stop all use
2. Scope spread
3. Counsel remediate
4. Disclose apt

### Over-marking

Cause: Everything confidential

Fix:

1. Tiers + criteria
2. Re-classify
3. Train
4. Audit

### Exit leaks

Cause: No offboarding hygiene

Fix:

1. Checklist + revoke
2. Remind duties
3. Audit access
4. Enforce

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- See.
- Stop.
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

Avoid marker-blind crawling; find-keeping; tainted sourcing; unmarked secrets; NDA-free sharing; exit-hygiene-free.

## Bundled References

Read `references/secrets-handling.md` when handling confidences.
Run `scripts/secret_finder.py` to scan for secret markers.
Copy `assets/checklists.md` into every delivery.
