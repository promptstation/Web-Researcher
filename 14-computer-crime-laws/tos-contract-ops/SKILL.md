---
name: tos-contract-ops
description: Track every target's terms and negotiate access like a professional. Use when the user asks to review website terms of service; track ToS changes; negotiate API access; browsewrap vs clickwrap; document scraping positions.
compatibility: Counsel for positions; change detection; relationship owners per target.
metadata:
  author: Promptstation
  version: 1.0.0
  category: cyber-law
---

# ToS Contract Ops

Treat terms as relationships. You read clauses critically, track versions with alerts, catch changes fast, negotiate APIs and agreements professionally, and document comply/negotiate/avoid positions with counsel.

Optimize simultaneously for:

- read terms
- tracked versions
- caught changes
- signed deals
- filed positions

Positions need counsel on gray; never deception to manufacture acceptance. Not legal advice.

## Use Cases

### New target

Trigger: user says 'scrape site X' or 'review terms'

Steps:

1. Read + extract
2. Position memo
3. Comply/negotiate
4. Track live

Result: Governed target.

### ToS change

Trigger: user says 'terms updated' or 'alert fired'

Steps:

1. Diff clauses
2. Assess impact
3. Adjust/negotiate
4. File decision

Result: Adapted relationship.

### Deal path

Trigger: user says 'they offer API' or 'partner instead'

Steps:

1. Compare build/buy
2. Negotiate terms
3. Paper agreement
4. Migrate

Result: Licensed access.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- ToS register
- Clause extracts
- Version history
- Change alerts
- Position memos
- Negotiation log
- Agreements filed
- Review dates

Never ignore ToS changes or fake acceptance to dodge terms.

## Phase 1 — Read Critically

Scraping, API, rate, IP, termination clauses.

Enforceability notes per regime.

Risk-tier the target.

## Phase 2 — Track Versions

Register with `scripts/tos_register.py`.

Snapshot + diff on schedule.

Alert owners on change.

## Phase 3 — Position

Comply / negotiate / avoid with reasons.

Counsel signs gray.

File memo; review dated.

## Phase 4 — Negotiate

API/data deal playbook.

Paper signed agreements.

Migrate off scraping where dealt.

## Examples

### Example 1: Deal won

User says: "ToS bans scraping, need data."

Actions:

1. Negotiated API tier
2. Cheaper than fight
3. Signed + migrated
4. Relationship warm

Result: Licensed win.

### Example 2: Change caught

User says: "Terms updated silently?"

Actions:

1. Diff in 24h
2. New API clause
3. Adjusted + memo'd
4. No incident

Result: Watched terms.

## Troubleshooting

### ToS ambiguous

Cause: Vague automation clauses

Fix:

1. Ask for clarity
2. Counsel memo
3. Conservative read
4. Negotiate

### Target hostile

Cause: Cease-and-desist

Fix:

1. Pause immediately
2. Counsel responds
3. Negotiate or exit
4. Log all

### Deal stalls

Cause: No owner or leverage

Fix:

1. Assign owner
2. Build/buy memo
3. Escalate value
4. Decide dated

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Read.
- Watch.
- Relate.

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

Avoid ToS-blind scraping; track-free terms; alert-free changes; memo-free positions; negotiation-free reds; escalation-first hostility.

## Bundled References

Read `references/tos-governance.md` when reviewing or negotiating terms.
Run `scripts/tos_register.py` as a ToS register.
Copy `assets/checklists.md` into every delivery.
