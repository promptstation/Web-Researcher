---
name: egress-routing-policy
description: Route every request by policy with automatic health-gated failover. Use when the user asks to route traffic across proxy pools; fail over between providers; write routing policies; audit egress decisions; shadow-test routing changes.
compatibility: Two or more pools/providers; router in client or gateway; decision logs retained.
metadata:
  author: Promptstation
  version: 1.0.0
  category: proxy-management
---

# Egress Routing Policy

Send every request down its right path. You classify by target, geo, cost, and sensitivity; write ordered policy tables; fail over on health automatically; log every decision; and audit weekly.

Optimize simultaneously for:

- classified traffic
- live policies
- auto failover
- logged decisions
- audited routes

Policy in version control; no silent default that sends sensitive traffic down cheap paths.

## Use Cases

### Multi-provider

Trigger: user says 'two proxy vendors' or 'split traffic'

Steps:

1. Classify traffic
2. Write policy
3. Fail over ready
4. Audit weekly

Result: Ordered multi-provider routing.

### Failover proof

Trigger: user says 'provider outage plan' or 'prove failover'

Steps:

1. Health-gate pools
2. Drill outage
3. Verify shift
4. Document RTO

Result: Proven fast failover.

### Cost routing

Trigger: user says 'cheap pool first' or 'tier by cost'

Steps:

1. Tier pools by cost
2. Route fit-first
3. Overflow by policy
4. Track savings

Result: Cheapest-fit routing.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Dimension catalog
- Policy table versioned
- Failover thresholds
- Decision log schema
- Shadow-test results
- Audit reports
- RTO evidence
- Change history

Never route sensitive flows down unvetted cheap paths, and never change policy without shadow test.

## Phase 1 — Classify Traffic

Dimensions: class, geo, cost tier, sensitivity.

Label every request path.

Review labels quarterly.

## Phase 2 — Write Policy

Prototype with `scripts/policy_router.py --table policy.json`.

Ordered rules, explicit default.

Version in git; review changes.

## Phase 3 — Fail Over

Health-gate every pool.

Auto-shift on trip; alert.

Drill quarterly; record RTO.

## Phase 4 — Audit

Weekly: decisions vs policy.

Monthly: cost and compliance.

File reports.

## Examples

### Example 1: Outage shift

User says: "Primary provider down."

Actions:

1. Auto-shift in 90s
2. Zero data loss
3. Returned gradually
4. RTO filed

Result: Seamless failover.

### Example 2: Tiered savings

User says: "Everything on premium."

Actions:

1. Fit-first routing
2. Premium only sensitive
3. Down 35 percent
4. Success kept

Result: Smart tiering.

## Troubleshooting

### Flapping routes

Cause: Thresholds at noise

Fix:

1. Hysteresis bands
2. Cooldown returns
3. Smooth health
4. Verify stable

### Default swallows traffic

Cause: Rules too narrow

Fix:

1. Audit default share
2. Add explicit rules
3. Alert on default rate
4. Review monthly

### Shadow diverges

Cause: Stale shadow data

Fix:

1. Refresh fixtures
2. Compare weekly
3. Fix drift
4. Gate changes on shadow

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Write.
- Run.
- Prove.

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

Avoid single-pool dependence; rule-free routing; silent defaults; failover-free plans; decision-free debugging; shadow-free changes.

## Bundled References

Read `references/routing-policy.md` when writing or auditing routing policy.
Run `scripts/policy_router.py` to prototype policy routing.
Copy `assets/checklists.md` into every delivery.
