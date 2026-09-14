---
name: scraping-traffic-anomaly-detection
description: Baseline collection traffic and catch ban waves, drift, and decay early with playbooks. Use when the user asks to baseline my scraping traffic; detect ban waves early; set alerts for collection health; explain a success-rate collapse; build scraping incident playbooks.
compatibility: Any OS with Python 3.10+; JSONL request logs as input; no ML libraries required.
metadata:
  author: Promptstation
  version: 1.0.0
  category: network-analysis
---

# Scraping Traffic Anomaly Detection

Catch collection incidents in minutes, not days. You baseline every signal that matters, set thresholds from distributions, correlate shifts into classified incidents, and run playbooks that restore health measurably.

Optimize simultaneously for:

- true baselines
- meaningful alerts
- classified incidents
- executed playbooks
- verified recoveries

Do not page on single-metric noise; correlate signals, classify first, then execute the matching playbook.

## Use Cases

### Ban wave

Trigger: user says 'success collapsed' or 'all 403s suddenly'

Steps:

1. Confirm multi-signal signature
2. Classify scope: domain, pool, or fleet
3. Execute ban-wave playbook
4. Verify recovery to baseline

Result: Contained wave, measured recovery.

### Silent drift

Trigger: user says 'fields empty lately' or 'data quality slipping'

Steps:

1. Chart validation and null rates
2. Pin drift start and scope
3. Fix extractor, bump version
4. Backfill affected window

Result: Drift fixed with backfill.

### Cost spike

Trigger: user says 'proxy bill exploded' or 'cost per page up'

Steps:

1. Attribute cost by pool and domain
2. Find retry or rotation waste
3. Tighten policy at the waste
4. Confirm cost per 1k restored

Result: Cost restored with cause named.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Signal inventory per domain
- Baseline stats with windows
- Threshold table with hysteresis
- Signature classification
- Playbook executed stepwise
- Timeline of detection to recovery
- Recovery charts vs baseline
- Postmortem with prevention

Never alert without baselines, and never close incidents without recovery charts.

## Phase 1 — Inventory Signals

List rate, status mix, latency p50/p95, challenge rate, validation rate, dedupe rate, cost per 1k per domain.

Confirm each signal flows from logs to metrics without gaps.

Record season and schedule effects per domain.

## Phase 2 — Baseline and Threshold

Run `scripts/traffic_baseline.py --logs jobs.log.jsonl --window-days 7` to derive baselines and flags.

Set warn and page thresholds from distributions with hysteresis and cooldowns.

Tune until pages are rare and real.

## Phase 3 — Classify Shifts

Match shifts to signatures: ban wave, drift, decay, cost, or capacity.

Confirm with secondary signals before paging.

Open incident with class, scope, and start time.

## Phase 4 — Respond and Verify

Execute the matching playbook stepwise with timestamps.

Watch signals return inside thresholds.

Publish recovery charts and postmortem prevention.

## Examples

### Example 1: Subnet ban

User says: "One pool went all red."

Actions:

1. Signature matched pool-scoped ban
2. Quarantined pool, shifted load
3. Success restored in 20 minutes
4. Pool rehabbed next day

Result: Fast containment, clean recovery.

### Example 2: Layout drift

User says: "Prices missing since Tuesday."

Actions:

1. Validation rate fell Tuesday 14:00
2. Pinned selector change, fixed extractor
3. Backfilled the window
4. Alert added on null rate

Result: Backfilled with new guard.

## Troubleshooting

### Alerts flap constantly

Cause: Thresholds without hysteresis on noisy signals

Fix:

1. Add hysteresis bands
2. Lengthen windows
3. Require multi-signal confirmation
4. Re-tune to rare-and-real

### Incident missed by alerts

Cause: Unbaselined signal or holiday-season drift

Fix:

1. Add the missed signal
2. Season-adjust baselines
3. Backtest thresholds on history
4. Drill the new rule

### Recovery claimed too early

Cause: Single green sample after fix

Fix:

1. Require sustained green windows
2. Confirm all signals, not one
3. Watch one full cycle
4. Then close with charts

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Baseline.
- Alerts.
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

Avoid alerts without baselines; single-signal paging; incidents closed without charts; thresholds copied across domains; seasons ignored; postmortems skipped.

## Bundled References

Read `references/incident-signatures.md` when classifying shifts or writing playbooks.
Run `scripts/traffic_baseline.py` to baseline JSONL logs and flag current anomalies.
Copy `assets/checklists.md` into every delivery.
