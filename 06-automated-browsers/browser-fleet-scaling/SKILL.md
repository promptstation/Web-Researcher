---
name: browser-fleet-scaling
description: Scale browser fleets with sized contexts, queues, guards, and backpressure. Use when the user asks to scale Playwright workers; size browser contexts per host; add queues to scraping; prevent worker OOMs; shard crawling by domain.
compatibility: Any OS with Python 3.10+; Docker optional; queue backend per scale (file, Redis, RabbitMQ).
metadata:
  author: Promptstation
  version: 1.0.0
  category: browser-automation
---

# Browser Fleet Scaling

Scale without collapse. You size from measured memory, queue work with leases, guard every resource, apply backpressure honestly, and shard so one hot domain never sinks the fleet.

Optimize simultaneously for:

- right-sized hosts
- queued work
- armed guards
- honest backpressure
- clean shards

Measure before scaling; never add workers to fix target-side or egress-side ceilings.

## Use Cases

### Scale-up

Trigger: user says 'need 10x throughput' or 'add workers'

Steps:

1. Find the true ceiling
2. Size hosts
3. Queue and shard
4. Ramp with guards

Result: Measured scale-up.

### OOM fleet

Trigger: user says 'workers die' or 'memory grows'

Steps:

1. Measure per-context growth
2. Cap and recycle
3. Add guards
4. Verify flat

Result: Stable fleet.

### Hot domain

Trigger: user says 'one domain floods us' or 'unfair sharing'

Steps:

1. Shard by domain
2. Isolate throttles
3. Cap per-shard workers
4. Verify fairness

Result: Fair isolated scaling.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Sizing math with measurements
- Queue design with leases
- Guard thresholds
- Backpressure map
- Shard plan
- Ramp procedure
- Load-test results
- Run dashboards

Never scale past measured ceilings, and never share throttles across shards.

## Phase 1 — Size from Data

Run `scripts/worker_sizer.py --headroom 0.25` for host capacity.

Measure per-context RSS on real targets.

Derive browsers and contexts per host.

## Phase 2 — Queue Work

Pick backend by scale and team skill.

Lease with timeouts and redelivery.

Shard queues by domain class.

## Phase 3 — Guard Resources

Cap memory, CPU, contexts per worker.

Shed load gracefully at thresholds.

Recycle browsers on schedule.

## Phase 4 — Ramp and Verify

Ramp 1-2-5-10x watching all signals.

Stop at first ceiling; budget under it.

Load-test quarterly.

## Examples

### Example 1: 10x ramp

User says: "From 10k to 100k pages daily."

Actions:

1. Ceiling found at egress
2. Added pools plus shards
3. Ramped over a week
4. Stable at 12x headroom

Result: Headroomed scale.

### Example 2: Memory leak hunt

User says: "Workers grow 2GB daily."

Actions:

1. Per-context growth isolated
2. Recycle every 100 jobs
3. Flat for a month
4. Guard alarmed

Result: Leak contained by design.

## Troubleshooting

### Throughput flat as workers rise

Cause: Ceiling elsewhere: target, egress, queue

Fix:

1. Ladder one variable
2. Name the ceiling
3. Fix or budget there
4. Stop adding workers

### Queue grows unbounded

Cause: Producers outpace guarded workers

Fix:

1. Throttle producers
2. Add workers to ceiling only
3. Shed low priority
4. Alert on age

### Noisy-neighbor shards

Cause: Shared throttles or hosts

Fix:

1. Split shards fully
2. Pin workers per shard
3. Isolate budgets
4. Verify fairness

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Size.
- Queue.
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

Avoid unmeasured scaling; shared cross-shard throttles; guard-free workers; unbounded queues; ceiling-ignoring ramps; untested load claims.

## Bundled References

Read `references/fleet-math.md` when sizing or sharding browser fleets.
Run `scripts/worker_sizer.py` to size browser workers from host memory.
Copy `assets/checklists.md` into every delivery.
