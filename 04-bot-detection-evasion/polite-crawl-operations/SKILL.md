---
name: polite-crawl-operations
description: Budget rates, honor pacing signals, and adapt throttles to stay welcome. Use when the user asks to set crawl rates per host; handle 429s correctly; honor Retry-After; build adaptive throttling; prove long-run politeness.
compatibility: Any OS with Python 3.10+; your own client code; no target cooperation beyond standard signals.
metadata:
  author: Promptstation
  version: 1.0.0
  category: bot-management
---

# Polite Crawl Operations

Earn continued access through discipline. You budget rates per host, honor every pacing signal first, adapt throttles to live feedback, and prove politeness with long-run dashboards.

Optimize simultaneously for:

- budgeted rates
- honored signals
- correct backoff
- adaptive control
- proven politeness

Server signals outrank local schedules always; never exceed quotas by parallelism tricks.

## Use Cases

### New target onboarding

Trigger: user says 'start crawling X' or 'what rate is safe'

Steps:

1. Classify host and quota
2. Start at 10 percent of budget
3. Ramp on health
4. Publish the budget

Result: Safe ramp with record.

### 429 recovery

Trigger: user says 'getting throttled' or 'quota errors'

Steps:

1. Honor Retry-After immediately
2. Cut concurrency and rate
3. Recover gradually
4. Tune budget down

Result: Restored access, right-sized budget.

### Fleet discipline

Trigger: user says 'prove we are polite' or 'audit rates'

Steps:

1. Dashboard gaps and errors
2. Score vs budgets
3. Fix violators
4. Report monthly

Result: Evidenced good citizenship.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Budget table per host
- Signal-honoring order doc
- Backoff spec
- Adaptive rules
- Quota tracking
- Dashboards
- Violation log
- Review cadence

Never split traffic to dodge quotas, and never ignore Retry-After for deadlines.

## Phase 1 — Budget Rates

Classify hosts: tiny, standard, large, API-quota.

Set base rates far under limits.

Record crawl-delay and quota per host.

## Phase 2 — Honor Signals

Order: Retry-After, then 429/503 backoff, then crawl-delay, then budget.

Parse both delay-seconds and HTTP dates.

Log every signal response.

## Phase 3 — Adapt Live

Run `scripts/adaptive_throttle.py --demo` to validate controller logic.

Tighten fast on errors, relax slowly on health.

Couple concurrency to rate changes.

## Phase 4 — Prove Politeness

Dashboard gaps, errors, and quota use.

Review monthly with stakeholders.

Tune budgets from evidence.

## Examples

### Example 1: API quota

User says: "1k requests per hour limit."

Actions:

1. Budgeted 800 with adaptive cap
2. Honored quota headers
3. Zero overages in 6 months
4. Increased on request later

Result: Trusted API consumer.

### Example 2: Small-site care

User says: "Crawl a tiny blog safely."

Actions:

1. One request per 5s, off-peak
2. Sitemap-first, 200 pages total
3. Zero errors, thank-you reply
4. Template for small sites

Result: Model small-site behavior.

## Troubleshooting

### 429 despite low rate

Cause: Shared quota, burst shape, or concurrency

Fix:

1. Check quota scope and window
2. Smooth bursts
3. Cut concurrency to 1
4. Ask operator for terms

### Retry-After date in past

Cause: Clock skew or stale response

Fix:

1. Sync clocks
2. Treat as short delay
3. Log the anomaly
4. Continue cautiously

### Adaptive oscillates

Cause: Relaxing too fast after errors

Fix:

1. Slow the relax step 10x
2. Add cooldown windows
3. Require sustained health
4. Re-tune from logs

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Budget.
- Signals.
- Adapt.

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

Avoid quota dodging by parallelism; Retry-After ignored; fixed sleeps as policy; fast relax after errors; deadline-driven hammering; unlogged adaptations.

## Bundled References

Read `references/pacing-signals.md` when honoring server pacing or designing throttles.
Run `scripts/adaptive_throttle.py` to validate adaptive pacing logic.
Copy `assets/checklists.md` into every delivery.
