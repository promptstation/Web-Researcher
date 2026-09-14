---
name: scraping-ethics-foundations
description: Decide every scrape by stakeholders, harms, and consent — in writing. Use when the user asks to is scraping this ethical; stakeholder analysis for data project; harm analysis template; ethical review for scraping; beyond legal compliance.
compatibility: Review partners; ethics references; decision log.
metadata:
  author: Promptstation
  version: 1.0.0
  category: ethics
---

# Scraping Ethics Foundations

Put ethics before extraction. You map every stakeholder, name harms honestly, weigh benefits against least-harm alternatives, climb consent ladders, and decide in writing with dissent welcomed.

Optimize simultaneously for:

- mapped stakes
- named harms
- weighed benefits
- sought consent
- reviewable calls

Legality is the floor; ethics decides the ceiling; dissent never punished.

## Use Cases

### Project review

Trigger: user says 'should we scrape this' or 'ethics check'

Steps:

1. Map + harms
2. Alternatives
3. Consent?
4. Memo decision

Result: Principled call.

### Harm found

Trigger: user says 'this could hurt X' or 'worried about'

Steps:

1. Name harm
2. Redesign least-harm
3. Re-weigh
4. Decide/document

Result: Harm reduced.

### Dissent raised

Trigger: user says 'I object' or 'uncomfortable'

Steps:

1. Hear fully
2. Address in memo
3. Decide + record
4. Protect dissenter

Result: Healthy culture.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Stakeholder maps
- Harm analyses
- Alt-path log
- Consent record
- Decision memos
- Dissent log
- Review dates
- Training record

Never treat legal as sufficient or punish ethical dissent.

## Phase 1 — Map Stakes

Subjects, sites, users, public, team.

Scaffold with `scripts/stakeholder_map.py --project NAME`.

Power and vulnerability noted.

## Phase 2 — Name Harms

Privacy, economic, autonomy, dignitary, ecosystem.

Likelihood x severity, honestly.

Worst-case written plainly.

## Phase 3 — Weigh and Climb

Benefits real and evidenced.

Least-harm alternatives first.

Consent ladder climbed.

## Phase 4 — Memo and Review

Decision + reasons + dissent filed.

Review dated; revisit on change.

Publish aptly.

## Examples

### Example 1: Redesigned scrape

User says: "Scrape support forum?"

Actions:

1. Harms: distress, exposure
2. Aggregated-only redesign
3. Approved narrow
4. No complaints

Result: Careful collection.

### Example 2: Stopped project

User says: "Profitable but creepy?"

Actions:

1. Harm outweighed
2. Memo'd no-go
3. Leadership backed
4. Trust earned

Result: Principled stop.

## Troubleshooting

### Ethics theater

Cause: Checkbox memos

Fix:

1. Real review partners
2. Dissent welcomed
3. Decisions binding
4. Audit memos

### Harm blindness

Cause: No affected voices

Fix:

1. Consult proxies
2. Read complaints
3. Adversarial review
4. Slow down

### Consent impossible

Cause: Scale vs asking

Fix:

1. Climb ladder
2. Proxy + transparency
3. Minimize + aggregate
4. Document bind

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- See.
- Choose.
- Own.

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

Avoid legal-equals-ethical; stakeholder blindness; harm hand-waving; consent-skipping; memo-free calls; dissent-punishing.

## Bundled References

Read `references/ethics-framing.md` when reviewing scraping projects.
Run `scripts/stakeholder_map.py` to scaffold stakeholder analyses.
Copy `assets/checklists.md` into every delivery.
