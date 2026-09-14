---
name: egress-incident-response
description: Contain egress incidents fast, recover cleanly, and learn permanently. Use when the user asks to respond to proxy ban wave; handle provider outage; runbook for credential leak; egress incident postmortem; drill egress failover.
compatibility: On-call rotation; runbooks checked in; comms channel; staging for drills.
metadata:
  author: Promptstation
  version: 1.0.0
  category: proxy-management
---

# Egress Incident Response

Turn egress incidents into routine. You detect in minutes, triage by severity, contain decisively, recover up ladders, communicate crisply, and postmortem every one into better runbooks.

Optimize simultaneously for:

- fast detection
- right triage
- clean containment
- full recovery
- filed learning

People and trust first; contain before diagnosing; never hide incidents from affected parties.

## Use Cases

### Ban wave

Trigger: user says 'success collapsing' or 'mass bans'

Steps:

1. Detect and triage
2. Quarantine and slow
3. Fix root cause
4. Canary back

Result: Contained and recovered.

### Provider down

Trigger: user says 'proxy provider outage' or 'all failing'

Steps:

1. Confirm scope
2. Fail over
3. Communicate ETA
4. Return gradually

Result: Outage ridden out.

### Breach drill

Trigger: user says 'credential leak' or 'compliance breach'

Steps:

1. Revoke and pause
2. Scope exposure
3. Disclose properly
4. Harden all

Result: Integrity response.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Severity matrix
- Role cards
- Playbooks per class
- Comms templates
- Recovery ladders
- Postmortem docs
- Drill calendar
- Improvement log

Never freelance incidents without roles, and never skip postmortem or disclosure duties.

## Phase 1 — Detect Fast

Signals: success, bans, provider status, auth failures.

Page on SEV thresholds.

Start the clock and log.

## Phase 2 — Triage Right

Score with `scripts/incident_triage.py --signals FILE`.

Assign IC, comms, ops.

Set severity and cadence.

## Phase 3 — Contain and Recover

Quarantine, failover, revoke, or pause.

Canary back up ladders.

Verify full health.

## Phase 4 — Learn

Postmortem 48h.

Update runbook plus controls.

Drill the same class.

## Examples

### Example 1: Wave to green

User says: "Overnight ban wave."

Actions:

1. Paged in 6 min
2. Contained in 20
3. Recovered by noon
4. Root cause fixed

Result: Routine response.

### Example 2: Outage calm

User says: "Provider down 3 hours."

Actions:

1. Failover in 4 min
2. Comms hourly
3. Gradual return
4. Credit claimed

Result: Customers unaffected.

## Troubleshooting

### Detection slow

Cause: Thresholds loose or signals missing

Fix:

1. Tighten SEV gates
2. Add ban-rate signal
3. Test paging
4. Review monthly

### Chaotic response

Cause: No roles or stale runbook

Fix:

1. Assign IC first
2. Follow playbook
3. Update after
4. Drill quarterly

### Repeat incidents

Cause: Postmortem actions rot

Fix:

1. Owner plus date each
2. Track to done
3. Re-drill
4. Escalate aging

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Ready.
- Respond.
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

Avoid threshold-free paging; role-free response; containment-free diagnosis; ladder-free recovery; postmortem-free repeats; disclosure-free breaches.

## Bundled References

Read `references/egress-ir.md` when responding to or drilling egress incidents.
Run `scripts/incident_triage.py` to score incident severity.
Copy `assets/checklists.md` into every delivery.
