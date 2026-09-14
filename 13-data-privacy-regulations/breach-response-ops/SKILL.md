---
name: breach-response-ops
description: Contain breaches fast, notify lawfully, and learn permanently. Use when the user asks to respond to a data breach; assess breach notification duty; draft breach notices; run a breach tabletop; maintain a breach register.
compatibility: On-call + counsel + DPO; playbooks checked in; drill staging.
metadata:
  author: Promptstation
  version: 1.0.0
  category: privacy-law
---

# Breach Response Ops

Meet breaches prepared. You detect in hours, contain decisively while preserving evidence, assess notification duties against the clock, notify authorities and subjects properly, and postmortem every incident into stronger controls.

Optimize simultaneously for:

- fast detection
- clean containment
- right notifications
- supported subjects
- filed learning

Clocks start at awareness; counsel + DPO looped immediately; no cover-ups, ever.

## Use Cases

### Live breach

Trigger: user says 'breach suspected' or 'data exposed'

Steps:

1. Contain + preserve
2. Assess + clock
3. Notify + support
4. Postmortem

Result: Controlled response.

### Vendor breach

Trigger: user says 'vendor incident' or 'processor notice'

Steps:

1. Scope your data
2. Clock starts
3. Notify per duty
4. Remediate vendor

Result: Owned response.

### Tabletop

Trigger: user says 'drill breach' or 'test readiness'

Steps:

1. Inject scenario
2. Run clock
3. Grade response
4. Fix gaps

Result: Proven readiness.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Playbooks
- Role cards
- Clock tracker
- Assessment memos
- Notice drafts
- Subject support
- Breach register
- Postmortems

Never delay containment or notification, and never minimize scope to avoid duties.

## Phase 1 — Detect and Contain

Signals + report line known.

Revoke/isolate; preserve logs.

Start `scripts/breach_clock.py --case X` immediately.

## Phase 2 — Assess Duties

Risk to rights: notify authority 72h unless unlikely.

High risk: subjects without delay.

Counsel + DPO decide; memo filed.

## Phase 3 — Notify Right

Authority: nature, categories, volume, DPO, consequences, measures.

Subjects: plain language + support + steps.

Log all comms.

## Phase 4 — Learn

Postmortem 2 weeks.

Controls + training updated.

Register filed; drill next.

## Examples

### Example 1: Contained fast

User says: "S3 bucket public 6 hours."

Actions:

1. Closed in 40 min
2. Scoped: no sensitive
3. Authority memo filed
4. Controls hardened

Result: Minor, managed.

### Example 2: Notified right

User says: "Customer DB exfiltrated."

Actions:

1. 72h authority met
2. Subjects + support
3. Postmortem public-ish
4. Trust rebuilt

Result: Integrity response.

## Troubleshooting

### Scope unknown

Cause: Logging gaps

Fix:

1. Assume worst lawfully
2. Scope aggressively
3. Fix logging
4. Disclose honestly

### Clock panic

Cause: No playbook

Fix:

1. Follow phases
2. Counsel early
3. Notify phased
4. Drill after

### Repeat causes

Cause: Postmortem rot

Fix:

1. Owner + date all
2. Verify shipped
3. Re-drill
4. Report to leadership

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Ready.
- Respond.
- Close.

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

Avoid clock-free response; evidence-trampling; duty-dodging scope; notice-free high-risk; register-free incidents; drill-free teams.

## Bundled References

Read `references/breach-playbook.md` when responding to breaches.
Run `scripts/breach_clock.py` to track breach clocks.
Copy `assets/checklists.md` into every delivery.
