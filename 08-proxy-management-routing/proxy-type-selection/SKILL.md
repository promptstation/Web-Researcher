---
name: proxy-type-selection
description: Select proxy types and providers from fair trials and honest scorecards. Use when the user asks to choose datacenter or residential proxies; trial proxy providers; compare proxy costs; vet proxy ethics; negotiate proxy plans.
compatibility: Any stack; trial budgets; target list for realistic trials.
metadata:
  author: Promptstation
  version: 1.0.0
  category: proxy-management
---

# Proxy Type Selection

Buy egress with evidence. You compare types honestly, trial providers blind on your workload, score on success plus ethics, model true cost, and negotiate from data — with exit plans before entry.

Optimize simultaneously for:

- honest comparisons
- fair trials
- blind scores
- true costs
- ethical sourcing

Consent-sourced supply only; no provider without ethics vetting and exit plan.

## Use Cases

### First buy

Trigger: user says 'need proxies' or 'which provider'

Steps:

1. Define workload needs
2. Shortlist types
3. Trial top two
4. Score and buy

Result: Right-sized first buy.

### Cost shock

Trigger: user says 'proxy bill exploded' or 'cheaper options'

Steps:

1. Attribute cost by use
2. Right-size types
3. Trial alternatives
4. Migrate safely

Result: Lower bill, same outcomes.

### Ethics review

Trigger: user says 'audit suppliers' or 'sourcing questions'

Steps:

1. Request sourcing proof
2. Score ethics
3. Replace failures
4. Document chain

Result: Defensible supply chain.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Workload needs doc
- Type comparison
- Trial protocol plus data
- Scorecard completed
- Cost model
- Ethics vetting
- Contract plus SLA
- Exit plan

Never buy on marketing or price alone, and never source without consent proof.

## Phase 1 — Define Needs

Volume, geo, success target, latency budget.

Classify sensitivity per target class.

Set trial success criteria.

## Phase 2 — Trial Fairly

Use `scripts/proxy_trial.py` to score trial outcomes.

Identical workloads, blind labels.

Measure success, latency, stability.

## Phase 3 — Score Blind

Weight by your use case.

Include ethics and support.

Decide from numbers.

## Phase 4 — Buy and Exit-Plan

Negotiate from trial data.

Contract SLA plus exit terms.

Keep a warm second source.

## Examples

### Example 1: Right-sized buy

User says: "Spending residential everywhere."

Actions:

1. Classified: 70 percent fits DC
2. Mixed pools by class
3. Bill down 55 percent
4. Success steady

Result: Fit-for-purpose spend.

### Example 2: Ethics switch

User says: "Supplier cannot prove consent."

Actions:

1. Failed vetting, documented
2. Migrated to vetted source
3. Cost plus 10, risk gone
4. Chain filed

Result: Defensible egress.

## Troubleshooting

### Trial looks too good

Cause: Trial pool cleaner than paid

Fix:

1. Trial on paid-tier sample
2. Measure 2+ weeks
3. Contract the metrics
4. Keep second source

### Costs drift up

Cause: Mix creep or retry waste

Fix:

1. Attribute monthly
2. Right-size types
3. Fix retry waste
4. Alert on unit cost

### Single-source risk

Cause: One provider, no exit

Fix:

1. Qualify second source
2. Keep warm quota
3. Test failover
4. File exit plan

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Define.
- Trial.
- Buy.

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

Avoid marketing-led buying; residential-by-default; trial-free commits; price-only choice; unvetted supply; single-source lock-in.

## Bundled References

Read `references/proxy-types.md` when comparing types or vetting providers.
Run `scripts/proxy_trial.py` to score blind provider trials.
Copy `assets/checklists.md` into every delivery.
