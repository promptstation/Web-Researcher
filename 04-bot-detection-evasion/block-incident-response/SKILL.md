---
name: block-incident-response
description: Monitor block waves and run incident response to prevention-shipped postmortems. Use when the user asks to monitor scraping block rates; alert on bot-defense waves; run a block incident; write a scraping postmortem; build block dashboards.
compatibility: Any OS with Python 3.10+; pipeline logs; incident channel and on-call rotation.
metadata:
  author: Promptstation
  version: 1.0.0
  category: bot-management
---

# Block Incident Response

Turn block waves into practiced routine. You dashboard signals, alert on signatures, run incidents with clear roles and timelines, contain fast, and close with postmortems whose prevention items actually ship.

Optimize simultaneously for:

- live dashboards
- signature alerts
- roled incidents
- fast containment
- shipped prevention

Containment first, diagnosis second; never trade postmortem honesty for narrative comfort.

## Use Cases

### Live wave

Trigger: user says 'blocks spiking' or 'incident now'

Steps:

1. Confirm signature
2. Declare and role
3. Contain per playbook
4. Recover staged

Result: Controlled incident, clean recovery.

### Dashboard build

Trigger: user says 'visibility into blocks' or 'fleet health'

Steps:

1. Wire signals per domain
2. Set signature alerts
3. Tune to rare-and-real
4. Review weekly

Result: Trusted visibility.

### Postmortem

Trigger: user says 'never again' or 'review last outage'

Steps:

1. Timeline the incident
2. Name causes without blame
3. Commit prevention items
4. Track to shipped

Result: Learning that lands.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Dashboard links
- Alert rules with tests
- Incident log with timeline
- Containment record
- Recovery charts
- Postmortem doc
- Prevention items tracked
- Review date

Never skip postmortems for contained incidents, and never close prevention items unshipped.

## Phase 1 — Dashboard Signals

Wire block, challenge, 429, and auth-failure rates per domain and pool.

Run `scripts/block_triage.py --logs jobs.jsonl` on demand for instant scope.

Review dashboards weekly even when green.

## Phase 2 — Alert on Signatures

Define wave, decay, and single-domain signatures.

Require multi-signal confirmation.

Test alerts with replayed incidents.

## Phase 3 — Run the Incident

Declare, assign commander, comms, fix.

Contain: freeze, park, diagnose, canary, ramp.

Timeline everything in the channel.

## Phase 4 — Postmortem to Prevention

Write causes without blame in 48h.

Commit dated prevention items.

Track to shipped; report back.

## Examples

### Example 1: Weekend wave

User says: "Saturday spike, on-call paged."

Actions:

1. Signature confirmed in 6 minutes
2. Contained via playbook
3. Canary Sunday, full Monday
4. Postmortem shipped 3 preventions

Result: Textbook incident.

### Example 2: Slow decay

User says: "Success eroding for weeks."

Actions:

1. Dashboard showed pool decay
2. Incident declared, pool rehabbed
3. Rates restored
4. Egress scoring added

Result: Decay converted to system.

## Troubleshooting

### Alerts fire on noise

Cause: Single-signal thresholds

Fix:

1. Require confirmation signals
2. Add hysteresis
3. Backtest on history
4. Re-tune quarterly

### Incidents drag

Cause: No roles or unclear authority

Fix:

1. Pre-assign rotations
2. Commander decides
3. Timebox diagnosis
4. Contain first always

### Postmortems ignored

Cause: No owners or dates

Fix:

1. Owner plus date per item
2. Track visibly
3. Report monthly
4. Tie to planning

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Watch.
- Run.
- Learn.

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

Avoid unwatched fleets; single-signal paging; roleless incidents; diagnosis before containment; blameless-in-name-only reviews; prevention items unshipped.

## Bundled References

Read `references/incident-ops.md` when running or reviewing incidents.
Run `scripts/block_triage.py` to scope live block incidents from logs.
Copy `assets/checklists.md` into every delivery.
