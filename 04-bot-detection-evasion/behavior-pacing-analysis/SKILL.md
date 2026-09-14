---
name: behavior-pacing-analysis
description: Measure crawler behavior footprints and pace collection respectfully. Use when the user asks to measure my crawler pacing; fix bot-like request bursts; design polite crawl rates; analyze request timing logs; schedule scraping off-peak.
compatibility: Any OS with Python 3.10+; your own request logs with timestamps; no target data needed.
metadata:
  author: Promptstation
  version: 1.0.0
  category: bot-management
---

# Behavior Pacing Analysis

Crawl like a considerate guest. You measure gap distributions and bursts from your own logs, design jittered human-scale pacing, schedule heavy work kindly, and verify footprints actually improved.

Optimize simultaneously for:

- measured rhythms
- scored bursts
- jittered pacing
- kind schedules
- verified footprints

Pacing serves politeness, not disguise; identify honestly and stay within allowed rates even when pacing looks human.

## Use Cases

### Burst fix

Trigger: user says 'we hammer in bursts' or 'rate limited at start'

Steps:

1. Chart gaps and bursts
2. Add jitter and caps
3. Smooth startup ramps
4. Verify distributions

Result: Smooth respectful flow.

### Schedule design

Trigger: user says 'when to run heavy crawls' or 'off-peak windows'

Steps:

1. Map target peak hours
2. Shift bulk off-peak
3. Keep priority trickle
4. Publish the calendar

Result: Kind, effective calendar.

### Footprint audit

Trigger: user says 'are we polite' or 'prove good citizenship'

Steps:

1. Measure all behavior signals
2. Score against policy
3. Fix gaps
4. Report with charts

Result: Evidenced good citizenship.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Gap charts
- Burst scores
- Path-order notes
- Pacing spec with jitter
- Schedule calendar
- Before/after verification
- Policy thresholds
- Review date

Never use pacing to exceed allowed rates, and never randomize to defeat behavioral scoring.

## Phase 1 — Measure Rhythms

Run `scripts/pacing_analyzer.py --logs requests.jsonl` on your own logs.

Chart gap medians, p95s, and burst factors.

Flag metronome regularity and startup floods.

## Phase 2 — Design Pacing

Set base gaps from politeness budgets.

Add full jitter to every wait.

Ramp startups over minutes, not seconds.

## Phase 3 — Schedule Kindly

Map target business hours per region.

Shift bulk collection off-peak.

Reserve peak for tiny priority checks.

## Phase 4 — Verify Footprints

Re-measure after changes identically.

Confirm bursts gone and gaps natural.

Publish the verification charts.

## Examples

### Example 1: Startup flood

User says: "Limits hit in the first minute."

Actions:

1. Gaps showed 500 requests in 10s
2. Added ramp plus jitter
3. Flood became trickle
4. Limits cleared

Result: Polite startup.

### Example 2: Metronome crawler

User says: "Exactly 1 request per second, flagged."

Actions:

1. Regularity scored maximum bot-like
2. Jittered 0.7 to 2.3s around target
3. Footprint normalized
4. Access stabilized

Result: Natural rhythm, honest identity.

## Troubleshooting

### Jitter still flagged

Cause: Rate too high regardless of shape

Fix:

1. Lower base rate first
2. Shape is politeness, not permission
3. Seek allowlist for volume
4. Accept slower

### Off-peak still limited

Cause: Daily quota or reputation, not congestion

Fix:

1. Read quota headers and terms
2. Budget within quota
3. Request quota increase
4. Never split to dodge quotas

### Session depth looks odd

Cause: Breadth-first floods versus human depth

Fix:

1. Mix depth into crawl order
2. Respect session realism
3. Cap new sessions per hour
4. Verify shape deltas

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Measure.
- Design.
- Verify.

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

Avoid pacing as disguise; quotas dodged by shaping; burst ramps; metronome schedules; peak-hour bulk; unverified politeness claims.

## Bundled References

Read `references/pacing-math.md` when setting rates or scoring bursts.
Run `scripts/pacing_analyzer.py` to score your own request rhythms.
Copy `assets/checklists.md` into every delivery.
