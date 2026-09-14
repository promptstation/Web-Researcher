---
name: le-liaison-ops
description: Disclose and respond through counsel — verified, minimal, logged. Use when the user asks to respond to a subpoena; vulnerability disclosure policy; law enforcement data request; preservation letter response; verify a warrant.
compatibility: Counsel on speed-dial; request register; disclosure channels.
metadata:
  author: Promptstation
  version: 1.0.0
  category: cyber-law
---

# LE Liaison Ops

Cooperate lawfully, never loosely. You disclose vulns responsibly, triage every request through counsel, verify process before producing a byte, minimize to valid scope, protect privilege, and log everything — notifying users where allowed.

Optimize simultaneously for:

- fair disclosures
- triaged requests
- verified process
- minimal productions
- complete logs

Counsel sees every request before response; nothing produced on informal asks. Not legal advice.

## Use Cases

### Vuln found

Trigger: user says 'found vulnerability' or 'report to vendor'

Steps:

1. Scope + evidence
2. Private report
3. Timeline agreed
4. Disclose coordinated

Result: Responsible disclosure.

### Subpoena served

Trigger: user says 'legal request' or 'data demand'

Steps:

1. Preserve + counsel
2. Verify + scope
3. Minimize + produce
4. Log + notify

Result: Lawful response.

### Informal ask

Trigger: user says 'officer called' or 'urgent request'

Steps:

1. No data on calls
2. Require process
3. Counsel channel
4. Log attempt

Result: Proper channel.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Disclosure policy
- Request register
- Triage runbook
- Verification checklist
- Production log
- User notices
- Counsel memos
- Transparency notes

Never produce data without verified process or disclose vulns recklessly.

## Phase 1 — Publish Policy

Disclosure: scope, channel, timelines, safe harbor.

Requests: counsel-only intake.

Post publicly; brief teams.

## Phase 2 — Triage Fast

Preserve on receipt; clock deadlines.

Log with `scripts/disclosure_log.py`.

Counsel within hours.

## Phase 3 — Verify and Minimize

Valid court/process? scope? privilege?

Challenge overbroad; minimize production.

User notice unless barred.

## Phase 4 — Produce and Log

Exact scope; documented handoff.

Immutable log; transparency aggregates.

Postmortem process gaps.

## Examples

### Example 1: Coordinated fix

User says: "RCE in vendor product."

Actions:

1. Private report day 0
2. 90-day timeline
3. Patched + credited
4. Public writeup

Result: Safer ecosystem.

### Example 2: Scoped response

User says: "Broad warrant received."

Actions:

1. Counsel narrowed
2. Produced valid subset
3. User notified
4. Logged fully

Result: Rights protected.

## Troubleshooting

### Vendor silent

Cause: No disclosure channel

Fix:

1. CERT/CC route
2. Document attempts
3. Timed disclosure
4. Protect users first

### Gag pressure

Cause: Informal secrecy ask

Fix:

1. Require court order
2. Counsel decides
3. Log pressure
4. Disclose when free

### Over-collection

Cause: Preserve-everything panic

Fix:

1. Scope to request
2. Counsel narrows
3. Minimize fast
4. Review holds

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Ready.
- Handle.
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

Avoid policy-free disclosure; counsel-free responses; verify-free productions; scope-creeping compliance; log-free cooperation; notice-free secrecy.

## Bundled References

Read `references/disclosure-requests.md` when disclosing or responding.
Run `scripts/disclosure_log.py` as a request/disclosure log.
Copy `assets/checklists.md` into every delivery.
