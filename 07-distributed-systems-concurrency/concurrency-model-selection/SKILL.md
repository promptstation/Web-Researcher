---
name: concurrency-model-selection
description: Choose concurrency models from benchmarks, not folklore. Use when the user asks to asyncio or threads for scraping; measure GIL impact; size worker pools; combine async with multiprocessing; fix race conditions.
compatibility: Python 3.10+; stdlib only for benchmarks; no network needed for simulated runs.
metadata:
  author: Promptstation
  version: 1.0.0
  category: distributed-systems
---

# Concurrency Model Selection

Pick concurrency with evidence. You benchmark each workload three ways, measure GIL impact honestly, size pools from data, combine models at clean boundaries, and keep shared state out of hot paths.

Optimize simultaneously for:

- compared models
- measured GIL
- sized pools
- clean hybrids
- race-free code

No model choice without a benchmark; no shared mutable state across workers.

## Use Cases

### New collector

Trigger: user says 'fast concurrent fetcher' or 'which model'

Steps:

1. Characterize workload
2. Benchmark three ways
3. Choose with margin
4. Size and ship

Result: Right model, sized.

### Slow pipeline

Trigger: user says 'CPU pegged' or 'threads not helping'

Steps:

1. Profile first
2. Name the bottleneck
3. Move CPU to processes
4. Re-measure

Result: Bottleneck fixed.

### Race hunt

Trigger: user says 'duplicate records' or 'lost updates'

Steps:

1. Find shared state
2. Replace with queues
3. Add idempotency
4. Prove with stress

Result: Deterministic output.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Workload characterization
- Three-way benchmark
- GIL measurement
- Pool sizing math
- Hybrid boundary doc
- Race review
- Shutdown tests
- Perf baseline

Never choose by hype or share mutable state across workers.

## Phase 1 — Characterize Workload

Classify IO-bound, CPU-bound, or mixed with profiles.

Note payload sizes and latencies.

Set throughput and latency targets.

## Phase 2 — Benchmark Models

Run `scripts/concurrency_bench.py --jobs 200` for baseline shapes.

Benchmark threads, asyncio, and processes on your workload.

Record with hardware notes.

## Phase 3 — Design Hybrid

Async or threads for IO, processes for CPU.

Queues at every boundary.

Size pools from the bench.

## Phase 4 — Harden

Graceful shutdown with drain.

Stress for races.

Lock the baseline.

## Examples

### Example 1: Fetcher choice

User says: "10k API pulls hourly."

Actions:

1. Async beat threads 3x on bench
2. Sized 200 conns
3. Shipped hybrid with pool parser
4. Target met at 40 percent CPU

Result: Evidence-backed design.

### Example 2: Parser bottleneck

User says: "HTML parsing pegs CPU."

Actions:

1. GIL measured, parsers moved out
2. Process pool 4x throughput
3. Queue boundary clean
4. Stable since

Result: CPU properly placed.

## Troubleshooting

### Async slower than threads

Cause: Blocking calls inside the loop

Fix:

1. Find blocking calls
2. Offload to executors
3. Re-bench
4. Monitor loop lag

### More workers, same speed

Cause: Ceiling elsewhere or lock contention

Fix:

1. Profile contention
2. Name the ceiling
3. Fix there
4. Stop adding workers

### Shutdown hangs

Cause: Dangling tasks or unjoined pools

Fix:

1. Cancel with timeouts
2. Join pools
3. Drain queues
4. Test signals

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Bench.
- Design.
- Ship.

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

Avoid hype-driven choice; unmeasured pools; blocking async loops; shared mutable workers; shutdown-free code; one-model-everywhere.

## Bundled References

Read `references/concurrency-guide.md` when choosing or sizing concurrency.
Run `scripts/concurrency_bench.py` to compare concurrency shapes on simulated IO.
Copy `assets/checklists.md` into every delivery.
