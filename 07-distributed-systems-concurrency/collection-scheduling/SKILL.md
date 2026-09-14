---
name: collection-scheduling
description: Keep data fresh with SLA-driven schedules, aging, and bounded backfill. Use when the user asks to schedule scraping jobs; validate cron expressions; prioritize stale URLs; detect page changes cheaply; backfill after outages.
compatibility: Python 3.10+; cron or any scheduler; sitemaps and etags where offered.
metadata:
  author: Promptstation
  version: 1.0.0
  category: distributed-systems
---

# Collection Scheduling

Deliver freshness on promise. You set SLAs from need, schedule with validated cron, age priorities fairly, detect changes before fetching, and backfill bounded after outages — with lag always visible.

Optimize simultaneously for:

- honest SLAs
- valid schedules
- fair aging
- cheap change checks
- bounded backfills

Fetch only what freshness needs; never re-crawl unchanged content at full cost.

## Use Cases

### Freshness SLA

Trigger: user says 'keep prices fresh' or 'how often to crawl'

Steps:

1. Learn change cadence
2. Set SLA with margin
3. Schedule minimally
4. Verify lag

Result: Right-frequency collection.

### Stale backlog

Trigger: user says 'old items never refresh' or 'backlog grows'

Steps:

1. Age priorities
2. Bound backfill
3. Triage by SLA
4. Clear sustainably

Result: Fair fresh backlog.

### Change-driven

Trigger: user says 'stop fetching unchanged' or 'cut crawl cost'

Steps:

1. Add etag and hash checks
2. Schedule by sitemap
3. Fetch deltas only
4. Verify savings

Result: Delta-efficient collection.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- SLA table
- Cron inventory validated
- Aging function
- Change-check design
- Backfill policy
- Lag dashboards
- Missed-slot log
- Cost tracking

Never schedule by guess or backfill unbounded; never treat all URLs as equally urgent.

## Phase 1 — Set SLAs

Measure change cadence per dataset.

Negotiate SLA with consumers.

Schedule at half the change period max.

## Phase 2 — Schedule Discipline

Validate specs with `scripts/schedule_planner.py --spec '*/15 * * * *'`.

Pin timezones; ledger slots.

Alert on missed slots.

## Phase 3 — Age and Detect

Priority rises with staleness.

Etag, hash, sitemap before fetch.

Skip unchanged with proof.

## Phase 4 — Backfill Bounded

Triage by SLA breach first.

Cap backfill rate.

Report recovery ETA.

## Examples

### Example 1: Cost cut

User says: "Crawl bill doubled."

Actions:

1. SLAs right-sized
2. Change checks added
3. Fetches down 60 percent
4. Freshness kept

Result: Cheaper fresh data.

### Example 2: Outage recovery

User says: "Down 2 days, huge backlog."

Actions:

1. SLA triage order
2. Bounded backfill
3. ETA honored
4. No target harm

Result: Orderly recovery.

## Troubleshooting

### Cron drift

Cause: Timezone or DST confusion

Fix:

1. Pin UTC everywhere
2. Validate specs
3. Test DST edges
4. Monitor slot times

### Aging starves fresh

Cause: Stale backlog dominates

Fix:

1. Cap stale share
2. Band priorities
3. Bound backfill
4. Verify mix

### Change checks lie

Cause: Weak etags or dynamic noise

Fix:

1. Hash normalized content
2. Ignore volatile regions
3. Verify deltas
4. Tune thresholds

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- SLA.
- Run.
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

Avoid guess-based schedules; unvalidated cron; ageless backlogs; full-fetch everything; unbounded backfills; lag-blind fleets.

## Bundled References

Read `references/freshness-ops.md` when scheduling or backfilling.
Run `scripts/schedule_planner.py` to validate cron specs and preview runs.
Copy `assets/checklists.md` into every delivery.
