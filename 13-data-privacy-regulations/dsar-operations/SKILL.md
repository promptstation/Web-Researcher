---
name: dsar-operations
description: Handle access and erasure requests on time, completely, provably. Use when the user asks to handle a DSAR; respond to data access requests; verify requester identity; search all systems for personal data; meet GDPR response deadlines.
compatibility: System inventory; case tracker; redaction capability; counsel for refusals.
metadata:
  author: Promptstation
  version: 1.0.0
  category: privacy-law
---

# DSAR Operations

Honor rights on the clock. You intake with SLA timers, verify identity proportionately, search every system including vendors and backups, redact third parties, and respond with evidence — refusing only with memos.

Optimize simultaneously for:

- clean intakes
- fair verification
- complete searches
- safe packs
- met SLAs

SLA clocks start at receipt; no request lost; refusals reasoned and appealable.

## Use Cases

### Access request

Trigger: user says 'DSAR arrived' or 'subject wants data'

Steps:

1. Intake + clock
2. Verify + search
3. Redact + pack
4. Respond + file

Result: Timely complete response.

### Erasure request

Trigger: user says 'delete my data' or 'right to be forgotten'

Steps:

1. Verify + scope
2. Delete all + vendors
3. Verify absent
4. Confirm + file

Result: Honored erasure.

### Volume scale

Trigger: user says 'DSARs growing' or 'automate responses'

Steps:

1. Runbook first
2. Automate search
3. Human QA
4. SLA held

Result: Scaled rights.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Intake channel
- Case tracker
- ID policy
- System inventory
- Search runbooks
- Redaction guide
- Response templates
- SLA dashboard

Never miss SLA silently or disclose third-party data in responses.

## Phase 1 — Intake Fast

Log receipt; start SLA clock.

Track with `scripts/dsar_tracker.py`.

Acknowledge within days.

## Phase 2 — Verify Fair

Proportionate to sensitivity.

No new PII hoards for verification.

Document method.

## Phase 3 — Search All

Prod + backups + logs + vendors.

Runbook per system.

Evidence of completeness.

## Phase 4 — Respond Safe

Redact third parties + privileged.

Pack with what/kept-basis.

File; review misses.

## Examples

### Example 1: First DSAR

User says: "Never handled one."

Actions:

1. Intaked day 0
2. Searched 12 systems
3. Responded day 18
4. Process kept

Result: Calm compliance.

### Example 2: Erasure e2e

User says: "Delete across vendors too."

Actions:

1. Scoped 3 vendors
2. Deleted + verified
3. Confirmed with proof
4. SLA met

Result: Complete erasure.

## Troubleshooting

### System missed

Cause: Shadow stores

Fix:

1. Inventory all
2. Scan for strays
3. Add runbook
4. Re-verify

### SLA slip

Cause: Vendor lag or complexity

Fix:

1. Extend lawfully + notify
2. Escalate vendor
3. Parallelize
4. Postmortem

### Over-disclosure

Cause: Weak redaction

Fix:

1. Two-eye review
2. Redaction guide
3. Tool assist
4. Apologize + fix

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Take.
- Find.
- Give.

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

Avoid clock-free intakes; verify-by-hoarding; system-missing searches; redact-free packs; SLA-missing responses; memo-free refusals.

## Bundled References

Read `references/dsar-runbook.md` when fulfilling rights requests.
Run `scripts/dsar_tracker.py` as a DSAR case tracker.
Copy `assets/checklists.md` into every delivery.
