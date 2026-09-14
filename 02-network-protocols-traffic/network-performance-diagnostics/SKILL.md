---
name: network-performance-diagnostics
description: Measure path quality and pace scraping within path and target budgets. Use when the user asks to measure latency to a target; estimate usable bandwidth; explain throughput ceilings; detect throttling or shaping; set pacing for a scraping fleet.
compatibility: Any OS with Python 3.10+ and outbound HTTPS; no root or floods required.
metadata:
  author: Promptstation
  version: 1.0.0
  category: network-analysis
---

# Network Performance Diagnostics

Replace speed folklore with path budgets. You measure latency, loss, and bandwidth honestly, explain ceilings with evidence, and pace fleets inside the tighter of path capacity and target politeness.

Optimize simultaneously for:

- measured paths
- honest bandwidth
- explained ceilings
- budgeted pacing
- watched shaping

Do not raise parallelism without path measurements and explicit target budget headroom.

## Use Cases

### Slow region

Trigger: user says 'EU exits slow' or 'one region lags'

Steps:

1. Baseline the paths comparatively
2. Isolate latency vs loss vs shaping
3. Reroute or repace per finding
4. Verify with post-change probes

Result: Region fix from path data.

### Throughput ceiling

Trigger: user says 'more workers, same speed' or 'capped somewhere'

Steps:

1. Ladder workers while probing path
2. Name the ceiling: loss, RTT, server, or shaping
3. Fix at the ceiling layer
4. Publish the new budget

Result: Ceiling named and budgeted.

### Shaping suspicion

Trigger: user says 'fast at night, slow by day' or 'big files crawl'

Steps:

1. Probe by hour and by size
2. Chart the shaping signature
3. Adapt schedule and chunking
4. Document the pattern

Result: Schedule adapted to reality.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Path baselines with percentiles
- Bandwidth estimates with method
- Ceiling verdict with evidence
- Pacing table per class
- Shaping charts where claimed
- Probe commands recorded
- Before/after deltas
- Budget review date

Never flood paths to measure them, and never pace from single samples.

## Phase 1 — Baseline Paths

Run `scripts/path_probe.py --url <target> --samples 30` per path and egress.

Record connect RTT, TTFB, loss hints, and jitter percentiles.

Compare across regions, hours, and egresses.

## Phase 2 — Estimate Bandwidth

Time paced transfers of known sizes; never flood.

Derive usable bandwidth with overhead margins.

Cross-check against ladder throughput.

## Phase 3 — Name the Ceiling

Ladder parallelism while watching latency and errors.

Attribute the ceiling to path, server, shaping, or client.

Fix or budget at that layer explicitly.

## Phase 4 — Pace and Watch

Publish pacing from the tighter budget.

Schedule shaping-sensitive work off-peak.

Re-probe weekly and on complaints.

## Examples

### Example 1: Regional lag

User says: "Asian targets crawl from EU workers."

Actions:

1. RTT 280ms with loss on one transit
2. Moved traffic to regional egress
3. p95 halved
4. Path policy updated

Result: Regional egress win.

### Example 2: Daytime slowdown

User says: "Fast nights, slow days."

Actions:

1. Hourly probes showed shaping signature
2. Shifted bulk to off-peak windows
3. Kept priority trickle by day
4. SLA met within budget

Result: Schedule matched to shaping.

## Troubleshooting

### Jitter spikes randomly

Cause: Bufferbloat or competing bulk flows

Fix:

1. Probe with load and idle contrast
2. Pace bulk to smooth queues
3. Separate latency-sensitive hosts
4. Verify jitter falls

### Bandwidth varies wildly

Cause: Shared egress contention or server-side pacing

Fix:

1. Isolate egress vs target with multi-target probes
2. Move or split egress
3. Honor server pacing signals
4. Budget to sustained, not peak

### Loss only on large transfers

Cause: MTU or middlebox size sensitivity

Fix:

1. Test by size ladder
2. Check MTU path discovery
3. Chunk large transfers
4. Document the size threshold

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Measure.
- Budget.
- Watch.

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

Avoid flood-based measurement; single-sample pacing; peak-rate budgeting; parallelism past the knee; shaping ignored in planning; path vs server conflation.

## Bundled References

Read `references/path-budgets.md` when pacing fleets or judging ceilings.
Run `scripts/path_probe.py` to baseline path latency and TTFB percentiles.
Copy `assets/checklists.md` into every delivery.
