---
name: web-change-mining
description: Mine change patterns to schedule revisits and prove freshness. Use when the user asks to measure page change rates; schedule recrawls; prove data freshness; model update frequency; analyze fetch histories.
compatibility: Python 3.10+; fetch history store; hash discipline from incremental pipelines.
metadata:
  author: Promptstation
  version: 1.0.0
  category: data-mining
---

# Web Change Mining

Revisit by evidence, not habit. You log histories, timeline hashes, model rates per class, derive schedules from rates plus SLAs, and prove freshness with lag metrics.

Optimize simultaneously for:

- logged histories
- true timelines
- modeled rates
- derived schedules
- proven lag

Schedules from measured rates; freshness claims backed by lag data.

## Use Cases

### Recrawl right

Trigger: user says 'how often' or 'recrawl schedule'

Steps:

1. Model rates
2. Derive schedule
3. Verify lag
4. Tune quarterly

Result: Evidence schedule.

### SLA proof

Trigger: user says 'prove fresh' or 'freshness audit'

Steps:

1. Measure lag
2. Report per class
3. Show gaps
4. File evidence

Result: Audited freshness.

### Noise cut

Trigger: user says 'everything looks changed' or 'hash churn'

Steps:

1. Normalize more
2. Filter noise
3. Re-model
4. Verify stable

Result: True change signal.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- History schema
- Timeline samples
- Rate models
- Class bands
- Schedules
- Lag dashboards
- SLA table
- Audit reports

Never schedule by guess or claim fresh without lag measurement.

## Phase 1 — Log Histories

Per URL: fetched_at, hash, status, bytes.

Retain per analysis need.

Index by class + time.

## Phase 2 — Model Rates

Run `scripts/change_stats.py --history h.jsonl` per class.

Poisson-ish lambda; band classes.

Filter volatile noise first.

## Phase 3 — Derive Schedules

Interval from rate + SLA.

Fast lanes for hot classes.

Cap by politeness.

## Phase 4 — Prove Lag

Change-to-fetch lag sampled.

Dashboard per class.

Audit quarterly.

## Examples

### Example 1: Schedule right

User says: "Recrawl daily everything?"

Actions:

1. Rates: 5 percent daily-hot
2. Tiered schedules
3. Fetches down 70
4. Freshness up

Result: Smart revisits.

### Example 2: Lag proven

User says: "Customer asks freshness proof."

Actions:

1. Lag p95 3h shown
2. Audit filed
3. Deal closed
4. Monitor kept

Result: Sold freshness.

## Troubleshooting

### Rates inflated

Cause: Ads/timestamps unnormalized

Fix:

1. Normalize harder
2. Re-baseline
3. Verify stable
4. Monitor churn

### Hot misses

Cause: Class too coarse

Fix:

1. Split classes
2. Fast-lane hot
3. Verify lag
4. Re-band

### Lag hidden

Cause: Averages only

Fix:

1. p95 per class
2. Worst-lists
3. Alert tails
4. Fix slow paths

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Log.
- Model.
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

Avoid guess scheduling; noise-fed rates; average-only lag; class-free revisits; proof-free freshness; model-free SLAs.

## Bundled References

Read `references/change-modeling.md` when modeling change or scheduling revisits.
Run `scripts/change_stats.py` to compute change rates.
Copy `assets/checklists.md` into every delivery.
