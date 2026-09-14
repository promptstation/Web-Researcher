---
name: consent-management-ops
description: Run consent that is valid, recorded, withdrawable, and auditable. Use when the user asks to design GDPR consent; record consent evidence; honor consent withdrawal; audit consent records; fix dark patterns.
compatibility: Consent store (ledger); UX control; vendor propagation paths.
metadata:
  author: Promptstation
  version: 1.0.0
  category: privacy-law
---

# Consent Management Ops

Make consent real. You design unbundled informed choices, record tamper-evident proof, propagate withdrawal everywhere instantly, refresh on change, and audit chains with evidence — banning dark patterns outright.

Optimize simultaneously for:

- valid designs
- solid evidence
- instant withdrawal
- fresh consent
- audited chains

Consent never bundled, pre-ticked, or nagged; withdrawal as easy as giving.

## Use Cases

### New consent

Trigger: user says 'need consent for X' or 'cookie banner'

Steps:

1. Design valid
2. Record proof
3. Plumb withdrawal
4. Audit e2e

Result: Lawful consent.

### Withdrawal test

Trigger: user says 'prove withdrawal works' or 'user complained'

Steps:

1. Withdraw test
2. Trace systems
3. Fix gaps
4. Verify timed

Result: Proven withdrawal.

### Dark-pattern purge

Trigger: user says 'UX review' or 'regulator warning'

Steps:

1. Audit flows
2. Remove patterns
3. Re-test
4. Document clean

Result: Honest UX.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Consent designs
- Evidence schema
- Ledger sample
- Withdrawal map
- Propagation SLA
- Refresh log
- Audit reports
- Pattern ban list

Never pre-tick, bundle, or nag consent, and never delay withdrawal.

## Phase 1 — Design Valid

Specific per purpose; informed; unbundled.

No pre-ticks, no walls, equal prominence.

Counsel-review text.

## Phase 2 — Record Proof

Use `scripts/consent_log.py` ledger (who/what/when/how/notice).

Tamper-evident; retained per schedule.

Exportable for audits.

## Phase 3 — Withdraw Instant

One-click; propagate <24h all systems+vendors.

Confirm to subject.

Test quarterly timed.

## Phase 4 — Refresh and Audit

Re-consent on purpose/notice change.

Chain audits yearly.

Dark-pattern scans per release.

## Examples

### Example 1: Banner fixed

User says: "Cookie wall flagged."

Actions:

1. Redesigned equal-choice
2. Evidence ledger live
3. Withdrawal tested 2h
4. Complaint closed

Result: Compliant consent.

### Example 2: Withdrawal proven

User says: "Regulator asks proof."

Actions:

1. Traced 10 withdrawals e2e
2. All <24h incl vendors
3. Evidence filed
4. Passed

Result: Audited lifecycle.

## Troubleshooting

### Vendor lag

Cause: No propagation API

Fix:

1. Contractual SLA
2. Manual queue + verify
3. Replace vendor
4. Test e2e

### Consent fatigue

Cause: Too many prompts

Fix:

1. Bundle lawfully minimal
2. Remember choices
3. Reduce asks
4. UX test

### Evidence gaps

Cause: Legacy grants unrecorded

Fix:

1. Re-consent campaigns
2. Document legacy
3. Sunset unprovable
4. Gate future

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Ask.
- Keep.
- Honor.

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

Avoid bundled consent; pre-ticked boxes; nagging walls; evidence-free grants; slow withdrawal; vendor-blind propagation.

## Bundled References

Read `references/consent-lifecycle.md` when designing or auditing consent.
Run `scripts/consent_log.py` as a consent ledger.
Copy `assets/checklists.md` into every delivery.
