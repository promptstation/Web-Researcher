---
name: scraping-incident-ethics
description: Stop fast, disclose honestly, remediate beyond minimum. Use when the user asks to scraping incident response; when to stop a crawl; disclose data over-collection; remediate scraping harm; kill-switch design.
compatibility: Kill-switch authority; disclosure channels; amends budget.
metadata:
  author: Promptstation
  version: 1.0.0
  category: ethics
---

# Scraping Incident Ethics

Meet incidents with courage. You set stop criteria in advance, halt instantly on trigger, triage harm fast, disclose to affected duly, remediate beyond minimum with amends, and review blamelessly into prevention.

Optimize simultaneously for:

- set criteria
- fast stops
- true triage
- due disclosure
- real amends

People over pipelines: stop first, analyze second; cover-ups never.

## Use Cases

### Over-collection

Trigger: user says 'grabbed too much' or 'PII spilled'

Steps:

1. Stop + quarantine
2. Assess harm
3. Disclose + delete?
4. Prevent

Result: Contained + owned.

### Exposure

Trigger: user says 'published sensitive' or 'data leaked'

Steps:

1. Retract fast
2. Notify affected
3. Amends
4. Harden

Result: Harm minimized.

### Drill

Trigger: user says 'test incident' or 'tabletop ethics'

Steps:

1. Inject scenario
2. Run stop
3. Grade + fix
4. Re-drill

Result: Ready team.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Stop criteria
- Kill runbook
- Triage guide
- Disclosure templates
- Amends log
- Review docs
- Trust metrics
- Drill calendar

Never keep collecting through harm signals or bury incidents.

## Phase 1 — Set Criteria

Triggers: PII spill, ToS breach, harm report, block wave.

Authority + kill-switch tested.

Decide with `scripts/stop_decision.py` in drills.

## Phase 2 — Stop Fast

Halt scope in minutes.

Quarantine suspect data.

Notify chain instantly.

## Phase 3 — Triage Harm

Who, how bad, spreading, evidence.

Counsel + ethics looped.

Memo within 24h.

## Phase 4 — Disclose and Mend

Affected notified duly; public apt.

Delete/retract/remediate + amends.

Blameless review -> prevention.

## Examples

### Example 1: Spill owned

User says: "PII in public dataset!"

Actions:

1. Stopped + retracted 2h
2. Notified + deleted
3. Amends + audit
4. Trust dented, kept

Result: Owned fast.

### Example 2: Drill paid

User says: "Real incident felt easy?"

Actions:

1. Drilled quarterly
2. Muscle memory worked
3. Clean response
4. Kept drilling

Result: Prepared team.

## Troubleshooting

### Slow stop

Cause: No kill-switch

Fix:

1. Build + test
2. Authority clear
3. Drill
4. Time it

### Disclosure dread

Cause: Reputation fear

Fix:

1. Disclose anyway
2. Own fully
3. Amends real
4. Trust compounds

### Repeat incidents

Cause: Review rot

Fix:

1. Owner + date all
2. Verify shipped
3. Re-drill
4. Report trend

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Ready.
- Act.
- Mend.

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

Avoid criteria-free ops; switch-free pipelines; triage-free panic; disclosure-free incidents; amends-free fixes; drill-free teams.

## Bundled References

Read `references/incident-ethics.md` when handling scraping incidents.
Run `scripts/stop_decision.py` to drill stop decisions.
Copy `assets/checklists.md` into every delivery.
