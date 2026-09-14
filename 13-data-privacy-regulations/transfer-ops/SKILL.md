---
name: transfer-ops
description: Govern cross-border transfers with mechanisms, TIAs, and safeguards. Use when the user asks to transfer data internationally; sign SCCs; run a transfer impact assessment; map cross-border data flows; handle Schrems implications.
compatibility: Counsel for mechanism calls; transfer inventory; vendor cooperation.
metadata:
  author: Promptstation
  version: 1.0.0
  category: privacy-law
---

# Transfer Ops

Move data across borders on solid paper. You map every route, mechanism each one, assess impact honestly, add real safeguards, and review on legal change — with suspension paths ready.

Optimize simultaneously for:

- mapped routes
- mechanismed flows
- honest TIAs
- real safeguards
- ready suspensions

No transfer without registered mechanism; TIAs honest or not done at all.

## Use Cases

### New route

Trigger: user says 'use US vendor' or 'store in X'

Steps:

1. Map route
2. Mechanism + TIA
3. Safeguards
4. Approve + register

Result: Lawful route.

### Ruling shock

Trigger: user says 'adequacy struck' or 'new decision'

Steps:

1. Assess impact
2. Switch mechanism
3. Add safeguards
4. Suspend if needed

Result: Adapted transfers.

### Register audit

Trigger: user says 'prove transfers ok' or 'audit TIA'

Steps:

1. Pull register
2. Show TIAs
3. List reviews
4. File evidence

Result: Audited routes.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Transfer register
- Mechanism per route
- TIA docs
- Safeguard specs
- Review triggers
- Suspension runbook
- Counsel sign-offs
- Change log

Never transfer on lapsed mechanisms or file copy-paste TIAs.

## Phase 1 — Map Routes

From/to/data/purpose/vendor per flow.

Register with `scripts/transfer_register.py`.

Complete inventory first.

## Phase 2 — Mechanism Each

Adequacy > SCCs > BCRs > derogation.

Counsel confirms; paper filed.

Vendor flow-downs signed.

## Phase 3 — Assess and Safeguard

TIA: law + practice + risk.

Encrypt, minimize, gate access.

Residual risk stated.

## Phase 4 — Review Ready

Triggers: rulings, vendor change, scope.

Yearly re-review.

Suspension drilled.

## Examples

### Example 1: Vendor route

User says: "US analytics vendor?"

Actions:

1. SCCs + TIA
2. Pseudonymized + gated
3. Registered
4. Approved with review

Result: Compliant vendor.

### Example 2: Ruling adapted

User says: "Adequacy decision changed."

Actions:

1. Impact in a week
2. Mechanisms switched
3. Zero downtime
4. Filed

Result: Agile Records.

## Troubleshooting

### Vendor refuses SCCs

Cause: Small or stubborn vendor

Fix:

1. Escalate + alternatives
2. Derogation only if fits
3. Replace vendor
4. Suspend route

### TIA theater

Cause: Copy-paste assessments

Fix:

1. Route-specific facts
2. Real safeguards
3. Counsel challenge
4. Re-do honestly

### Shadow transfers

Cause: Unknown SaaS routes

Fix:

1. Discover (SSO, spend, DNS)
2. Register all
3. Mechanism backlog
4. Prevent recurrence

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Map.
- Paper.
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

Avoid register-free transfers; mechanism-free routes; theater TIAs; safeguard-free SCCs; trigger-free reviews; suspension-free plans.

## Bundled References

Read `references/transfer-governance.md` when moving data cross-border.
Run `scripts/transfer_register.py` as a transfer register.
Copy `assets/checklists.md` into every delivery.
