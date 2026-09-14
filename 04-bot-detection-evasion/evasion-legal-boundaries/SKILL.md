---
name: evasion-legal-boundaries
description: Spot legal-risk patterns, escalate early, and log restraint (not legal advice). Use when the user asks to review scraping legal risks; read terms for automation bans; decide public versus gated data; brief counsel on scraping; log scraping decisions.
compatibility: Any OS; plan documents as input; qualified counsel for actual advice; this skill is informational only.
metadata:
  author: Promptstation
  version: 1.0.0
  category: bot-management
---

# Evasion Legal Boundaries

Keep scraping inside defensible bounds. You spot risk patterns early, map terms honestly, separate public from gated, brief counsel crisply, and log decisions that show restraint at every step.

Optimize simultaneously for:

- spotted risks
- mapped terms
- classified data
- briefed counsel
- logged restraint

Informational only, never legal advice; escalate to qualified counsel before any gray-area collection.

## Use Cases

### Plan review

Trigger: user says 'review this scraping plan' or 'risks here?'

Steps:

1. Spot risk patterns
2. Map terms per target
3. Classify data sources
4. Recommend proceed, permission, or stop

Result: Risk-graded plan.

### Gray-area call

Trigger: user says 'is this allowed' or 'edge case'

Steps:

1. Freeze the scope
2. Draft counsel brief
3. Define stop triggers
4. Log the decision

Result: Counsel-ready pause.

### Audit trail

Trigger: user says 'prove we were careful' or 'compliance review'

Steps:

1. Compile decision logs
2. Show reviews and stops
3. Note counsel consults
4. File the pack

Result: Restraint on record.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Risk register per plan
- Terms maps with quotes
- Public-vs-gated verdicts
- Counsel briefs where gray
- Stop triggers
- Decision logs
- Review dates
- No-advice disclaimer

Never give legal conclusions, and never green-light gray-area collection without counsel.

## Phase 1 — Spot Risks

Run `scripts/compliance_checklist_gen.py --plan plan.md` to scaffold the review.

Flag barriers, gates, accounts, and bans.

Grade red, amber, green per source.

## Phase 2 — Map Terms

Quote automation and account clauses.

Note enforcement history if known.

Record jurisdiction signals.

## Phase 3 — Classify Data

Apply the public-vs-gated test per dataset.

Freeze amber and red scopes.

Brief counsel on gray with tight memos.

## Phase 4 — Log Decisions

Record proceed, permission-first, or stop per source.

Set review dates.

File logs immutably.

## Examples

### Example 1: Plan triage

User says: "Review before we build."

Actions:

1. Graded 8 sources: 5 green, 2 amber, 1 red
2. Amber to counsel, red stopped
3. Built green with logs
4. Zero surprises

Result: Defensible build.

### Example 2: Gray freeze

User says: "Edge case on one source."

Actions:

1. Froze scope same day
2. Briefed counsel in one page
3. Answer: permission-first
4. Logged and complied

Result: Clean escalation.

## Troubleshooting

### Terms ambiguous

Cause: Vague automation language

Fix:

1. Treat as amber
2. Ask operator for clarity
3. Brief counsel
4. Default to stop

### Public but rate-walled

Cause: Public data with technical friction

Fix:

1. Respect the friction
2. Seek API or permission
3. Never defeat the wall
4. Log the call

### Jurisdiction unclear

Cause: Global targets, local team

Fix:

1. Note both home and target regimes
2. Brief counsel on conflict
3. Apply stricter interim rule
4. Review annually

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Spot.
- Terms.
- Log.

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

Avoid legal conclusions without counsel; gray areas self-cleared; terms unread; barriers reframed as public; decision logs skipped; advice disclaimers missing.

## Bundled References

Read `references/risk-patterns.md` when grading plans or briefing counsel (informational).
Run `scripts/compliance_checklist_gen.py` to scaffold plan reviews and decision logs.
Copy `assets/checklists.md` into every delivery.
