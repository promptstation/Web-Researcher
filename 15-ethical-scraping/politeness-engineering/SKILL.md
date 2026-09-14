---
name: politeness-engineering
description: Crawl gently with budgets, adaptive rates, and public footprint reports. Use when the user asks to polite web crawling; crawl rate limits; reduce server load; crawler impact budget; handle webmaster complaints.
compatibility: Rate controls; abuse contact; footprint dashboard.
metadata:
  author: Promptstation
  version: 1.0.0
  category: ethics
---

# Politeness Engineering

Leave every server better than found. You budget impact per target, adapt to distress signals instantly, schedule kindly, cache everything cacheable, identify transparently, and report footprints publicly — answering complaints in hours.

Optimize simultaneously for:

- kept budgets
- calm servers
- kind schedules
- lean fetches
- open reports

Targets' health over your schedule; complaints answered same-day.

## Use Cases

### Gentle crawl

Trigger: user says 'crawl without harm' or 'rate advice'

Steps:

1. Budget impact
2. Adapt live
3. Cache + conditional
4. Report

Result: Invisible crawl.

### Complaint in

Trigger: user says 'webmaster angry' or 'blocked us'

Steps:

1. Pause instantly
2. Apologize + fix
3. Compensate apt
4. Resume agreed

Result: Relationship saved.

### Footprint open

Trigger: user says 'publish crawler stats' or 'transparency'

Steps:

1. Measure all
2. Publish + contact
3. Invite feedback
4. Iterate

Result: Trusted crawler.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Impact budgets
- Rate policies
- UA + contact
- Cache stats
- Footprint reports
- Complaint log
- Pause runbook
- Review dates

Never crawl through distress signals or hide crawler identity.

## Phase 1 — Budget Impact

Requests/day, bytes, est. cost per target.

Compute with `scripts/impact_budget.py --rpm 60`.

Approve over-budget explicitly.

## Phase 2 — Adapt Live

Slow on latency/errors/429; stop on 503 waves.

Honor Retry-After exactly.

Log adaptations.

## Phase 3 — Fetch Lean

Conditional GET; etags; sitemaps; off-peak.

Cache; never refetch unchanged.

Identify: UA + purpose + contact.

## Phase 4 — Report Open

Public footprint page; abuse contact monitored.

Complaints: pause + SLA hours.

Review quarterly.

## Examples

### Example 1: Unnoticed crawl

User says: "Crawl 1M pages quietly."

Actions:

1. Budgeted + off-peak
2. Zero complaints
3. Report published
4. Operators thanked

Result: Model citizen.

### Example 2: Complaint to fan

User says: "Blocked + angry email."

Actions:

1. Paused in 10 min
2. Fixed + apologized
3. Agreed schedule
4. Whitelisted

Result: Trust rebuilt.

## Troubleshooting

### Distress missed

Cause: No signal monitoring

Fix:

1. Monitor latency/errors
2. Auto-slow
3. Alert team
4. Pause-first culture

### Identity hidden

Cause: Generic UA

Fix:

1. Descriptive UA + URL
2. Contact live
3. Publish policy
4. Verify monthly

### Repeat complaints

Cause: No learning loop

Fix:

1. Postmortem each
2. Fix class
3. Track zero-goal
4. Report trend

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Plan.
- Run.
- Answer.

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

Avoid budget-free crawling; distress-blind speed; identity-hiding; complaint-ignoring; report-free ops; peak-hour hammering.

## Bundled References

Read `references/good-citizen.md` when crawling third-party sites.
Run `scripts/impact_budget.py` to budget crawl impact.
Copy `assets/checklists.md` into every delivery.
