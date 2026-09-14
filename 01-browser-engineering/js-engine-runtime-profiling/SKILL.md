---
name: js-engine-runtime-profiling
description: Profile event-loop, compile-tier, and memory behavior to fix long tasks and leaks with trace proof. Use when the user asks to explain promise versus timer ordering; profile long tasks and slow handlers; find a JavaScript memory leak; fix forced layouts and jank; move heavy work to workers.
compatibility: Any modern browser with DevTools Performance and Memory panels; Node.js 18+ for snippet runs; no frameworks required.
metadata:
  author: Promptstation
  version: 1.0.0
  category: browser-engineering
---

# JS Engine Runtime Profiling

Turn runtime folklore into measured facts. You model the event loop, attribute main-thread cost to exact handlers, prove leaks with retaining paths, and move work off the critical thread without breaking order.

Optimize simultaneously for:

- predictable scheduling
- attributed long tasks
- proven leak fixes
- offloaded heavy work
- reproducible profiles

Do not claim a performance fix without a named handler, a before/after trace, and a leak or layout check where relevant.

## Use Cases

### Janky interactions

Trigger: user says 'clicks feel slow' or 'INP is bad on this page'

Steps:

1. Record interaction with Performance and web-vitals attribution
2. Attribute worst tasks to handlers bottom-up
3. Split or defer the handler work
4. Re-measure the same interaction and report deltas

Result: Named handler fix with interaction proof.

### Growing memory

Trigger: user says 'tab memory grows forever' or 'scraper leaks over hours'

Steps:

1. Take baseline, action, and post-action heap snapshots
2. Diff shallow and retained sizes by constructor
3. Follow the retaining path to the registration site
4. Fix, re-run the action loop, and prove flat memory

Result: Leak fixed at the retaining root.

### Worker offload

Trigger: user says 'parsing blocks the page' or 'search indexing janks'

Steps:

1. Isolate the pure transform with inputs and outputs
2. Move it to a worker with chunked messages
3. Keep ordering with sequence numbers
4. Prove main-thread tasks shortened

Result: Same results, freed main thread.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Scheduling model: predicted order with verified run output
- Attribution: named handler per long task with self time
- Layout audit: forced-layout count before and after
- Leak proof: retaining path plus flat re-run graph
- Worker contract: message shapes, chunking, and order keys
- Trace artifacts: saved profiles with steps to reproduce
- Change list: handler, file, and scheduling rationale
- Guard: regression check a second person can repeat

Never ship runtime changes without attributed handlers, saved traces, and a re-run proof.

## Phase 1 — Model the Loop

Write the predicted order for the snippet or flow: sync script, microtasks, render, timers, I/O.

Run `node scripts/event_loop_drill.js` to calibrate mental models before touching page code.

Verify one real page flow against the model and note where frameworks add scheduling layers.

## Phase 2 — Attribute Cost

Record Performance with CPU throttling matching the target device class.

Read bottom-up by self time; name the handler, file, and call path for each long task.

Flag forced layouts and style recalc driven by JS reads after writes.

## Phase 3 — Prove Leaks or Layouts

For memory: three snapshots across repeated actions, detached-DOM check, allocation timeline for hot allocators.

For layout: batch reads before writes, cache measurements, use transform and opacity for animation.

Change one thing at a time and re-record.

## Phase 4 — Offload and Verify

Move pure transforms to workers with explicit message contracts and backpressure.

Idle-schedule non-critical hydration with deadlines and cancellation.

Re-run the original interaction or loop and publish deltas with trace links.

## Examples

### Example 1: Slow filter interaction

User says: "Filtering 5k rows freezes the page."

Actions:

1. Attributed 900ms task to synchronous filter plus layout thrash
2. Batched DOM writes and virtualized rows
3. Moved filter compute to a worker
4. Re-measured: interaction under 120ms

Result: Named fix with interaction proof.

### Example 2: Automation memory growth

User says: "Long scrape run grows without bound."

Actions:

1. Snapshots showed listener retention on recycled pages
2. Removed listeners in teardown and closed contexts
3. Re-ran 200 jobs flat at baseline plus 5%
4. Added listener audit to the runbook

Result: Flat memory with a prevention check.

## Troubleshooting

### Deopt warnings and slow optimized code

Cause: Hidden-class churn or mixed-type hot paths

Fix:

1. Stabilize object shapes in hot paths
2. Avoid delete and mixed element kinds
3. Narrow polymorphic call sites
4. Re-profile to confirm tier stability

### Microtask starvation of rendering

Cause: Promise chains that never yield to the render step

Fix:

1. Chunk chains with scheduler yields
2. Move bulk steps to workers
3. Cap queue depth with backpressure
4. Verify frames resume in trace

### Worker slower than main thread

Cause: Serialization cost or chatty messaging

Fix:

1. Batch messages and use transferables
2. Reduce round trips with coarser chunks
3. Measure postMessage overhead explicitly
4. Keep tiny tasks local

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Model.
- Cost.
- Fix.

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

Avoid optimization without attributed handlers; leak claims without retaining paths; worker moves without message contracts; microtask chains that never yield; forced layouts fixed by throttling instead of batching; trace-free performance claims.

## Bundled References

Read `references/engine-tiers.md` when reasoning about compile behavior or task order.
Run `scripts/event_loop_drill.js` to calibrate execution-order predictions before debugging real flows.
Copy `assets/checklists.md` into every delivery.
