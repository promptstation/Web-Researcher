---
name: proxy-cost-control
description: Attribute every egress dollar and cut unit cost without losing success. Use when the user asks to cut proxy costs; attribute proxy spend; budget cost per request; alert on proxy overruns; right-size proxy pools.
compatibility: Provider invoices plus outcome logs; spreadsheet or BI for reports; no new tools.
metadata:
  author: Promptstation
  version: 1.0.0
  category: proxy-management
---

# Proxy Cost Control

Spend each egress dollar on purpose. You attribute fully, budget per 1k successes, alert before overruns, right-size types from data, and cut waste class by class — reporting savings monthly.

Optimize simultaneously for:

- full attribution
- live budgets
- early alerts
- right types
- tracked savings

Savings never from consent-free supply or politeness cuts; success rate guarded on every change.

## Use Cases

### Bill shock

Trigger: user says 'proxy bill doubled' or 'cut spend'

Steps:

1. Attribute the delta
2. Name waste classes
3. Fix top two
4. Verify savings

Result: Explained controlled bill.

### Budget live

Trigger: user says 'cap proxy spend' or 'alert overruns'

Steps:

1. Set unit budgets
2. Alert at 80/100
3. Throttle or shift
4. Review weekly

Result: Guarded spend.

### Savings program

Trigger: user says '10 percent cheaper' or 'unit economics'

Steps:

1. Baseline unit cost
2. Roadmap savings
3. Ship monthly
4. Report trend

Result: Falling unit cost.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Attribution table
- Unit budgets
- Alert rules
- Right-size log
- Waste register
- Savings report
- Guard metrics
- Forecast

Never cut consent, politeness, or success guardrails to save money.

## Phase 1 — Attribute Spend

Join invoices to outcome logs.

Run `scripts/cost_tracker.py --logs outcomes.jsonl --rate 3.5` per pool.

Attribute 100 percent monthly.

## Phase 2 — Budget Units

Cost per 1k successes per pool.

Alert 80 warn, 100 throttle.

Owner per budget.

## Phase 3 — Cut Waste

Retry waste, unchanged refetch, wrong types, idle pools.

Fix top two monthly.

Guard success rate.

## Phase 4 — Report

Monthly unit-cost trend.

Savings with proof.

Forecast next quarter.

## Examples

### Example 1: 40 percent cut

User says: "Spend out of control."

Actions:

1. Attributed: retries 30 percent
2. Fixed backoff plus types
3. Down 40, success up
4. Program continues

Result: Disciplined spend.

### Example 2: Overrun caught

User says: "Budget blown silently."

Actions:

1. Alerts at 80 live
2. Caught day 12
3. Shifted pools
4. Month closed on budget

Result: Early warning works.

## Troubleshooting

### Attribution gaps

Cause: Untagged traffic or missing logs

Fix:

1. Tag every pool
2. Log every outcome
3. Reconcile to invoice
4. Close gaps

### Unit cost rises

Cause: Success falling or mix creep

Fix:

1. Split price vs success effects
2. Fix each lever
3. Re-baseline
4. Alert sooner

### Savings revert

Cause: One-off fixes, no guards

Fix:

1. Automate the fix
2. Alert on regress
3. Owner assigned
4. Review monthly

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Know.
- Guard.
- Save.

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

Avoid unattributed spend; budget-free pools; silent overruns; wrong-type waste; retry-burned budgets; guard-free cuts.

## Bundled References

Read `references/egress-economics.md` when budgeting or cutting proxy spend.
Run `scripts/cost_tracker.py` to compute unit cost per pool.
Copy `assets/checklists.md` into every delivery.
