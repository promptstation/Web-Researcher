---
name: scrape-data-quality
description: Watch scraped data quality with fill, validity, freshness, and drift signals. Use when the user asks to monitor data quality; track field fill rates; detect silent scraping breakage; measure data freshness; set up golden record tests.
compatibility: Python 3.10+; metrics backend for trends; 20+ golden records per critical feed.
metadata:
  author: Promptstation
  version: 1.0.0
  category: data-engineering
---

# Scrape Data Quality

Catch bad data before consumers do. You track fills, validate continuously, measure lag, detect drift, and guard golden records — alerting on bands, not anecdotes.

Optimize simultaneously for:

- tracked fills
- valid feeds
- measured lag
- caught drift
- guarded goldens

Quality SLOs per feed; silent breakage is a SEV, not a shrug.

## Use Cases

### Silent break

Trigger: user says 'prices vanished' or 'fields empty'

Steps:

1. Check fills and goldens
2. Name the break
3. Fix extractor
4. Backfill gap

Result: Caught and healed.

### Freshness SLA

Trigger: user says 'data stale' or 'lag unknown'

Steps:

1. Measure lag
2. Alert on SLA
3. Fix scheduling
4. Verify fresh

Result: Fresh on promise.

### Drift watch

Trigger: user says 'prices shifted?' or 'category mix odd'

Steps:

1. Baseline distributions
2. Band alerts
3. Investigate moves
4. Confirm or fix

Result: Explained distributions.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Fill dashboards
- Validity suite
- Lag metrics
- Drift baselines
- Golden set
- SLO table
- Alert rules
- Breakage log

Never ship feeds without quality SLOs or ignore golden failures.

## Phase 1 — Track Fills

Run `scripts/dq_check.py --in feed.jsonl` per batch.

Per field per source; bands at p10/p90.

Alert on band breach.

## Phase 2 — Validate Always

Suite runs per batch; blocks serve on fail.

Quarantine with codes.

Trend pass rates.

## Phase 3 — Measure Lag

Fetched-to-served per record.

SLA per dataset; alert early.

Dashboard p50/p95.

## Phase 4 — Guard Goldens

20+ known records per feed.

Fail loud on mismatch.

Review drift weekly.

## Examples

### Example 1: Break caught

User says: "Site redesigned overnight."

Actions:

1. Fill alerts in 1 hour
2. Extractor patched
3. Gap backfilled
4. Consumers unaffected

Result: Invisible incident.

### Example 2: Drift explained

User says: "Average price jumped."

Actions:

1. Drift alert fired
2. Mix shift confirmed real
3. Baseline updated
4. Report filed

Result: Signal not noise.

## Troubleshooting

### Alert storms

Cause: Bands too tight

Fix:

1. Widen to p5/p95
2. Require persistence
3. Separate sources
4. Review weekly

### Goldens rot

Cause: Real-world change

Fix:

1. Re-verify quarterly
2. Version goldens
3. Document changes
4. Keep 20+ fresh

### Lag hidden

Cause: Averages mask tails

Fix:

1. Track p95/p99
2. Alert on tails
3. Segment by source
4. Fix slow paths

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Track.
- Guard.
- Respond.

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

Avoid unmonitored feeds; average-only lag; golden-free suites; band-free alerts; drift-blind dashboards; playbook-free breakage.

## Bundled References

Read `references/dq-monitoring.md` when monitoring feed quality.
Run `scripts/dq_check.py` to check batch quality.
Copy `assets/checklists.md` into every delivery.
