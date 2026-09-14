---
name: queue-task-distribution
description: Distribute scraping work over durable, leased, fairly-prioritized queues. Use when the user asks to add a queue to my scraper; choose Celery or Redis queue; implement job leases; handle poison jobs; prioritize crawl queues.
compatibility: Python 3.10+; backend per scale; SQLite/file for small, Redis/RabbitMQ for large.
metadata:
  author: Promptstation
  version: 1.0.0
  category: distributed-systems
---

# Queue Task Distribution

Move work through queues that never lose or duplicate. You model jobs with identity, pick backends by honest scale, lease with safe redelivery, prioritize without starvation, and dead-letter with review.

Optimize simultaneously for:

- modeled jobs
- fit backends
- safe leases
- fair priorities
- reviewed DLQs

Every job acked exactly once in effect; poison jobs reviewed, never silently dropped or infinitely retried.

## Use Cases

### First queue

Trigger: user says 'outgrew a for-loop' or 'need workers'

Steps:

1. Model jobs
2. Stand up backend
3. Lease and ack
4. Prove no loss

Result: Durable distribution.

### Priority mess

Trigger: user says 'urgent jobs wait' or 'bulk starves fresh'

Steps:

1. Band priorities
2. Weight fairly
3. Prove with mix
4. Alert on age

Result: Fair scheduling.

### Poison storm

Trigger: user says 'one bad URL loops' or 'DLQ growing'

Steps:

1. Cap retries
2. Dead-letter fast
3. Review batch
4. Fix and requeue

Result: Contained poison.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Job schema
- Backend decision
- Lease parameters
- Priority policy
- DLQ review log
- Depth/age alerts
- Drain runbook
- Loss/dup proof

Never ack before durable write, and never retry poison without review.

## Phase 1 — Model Jobs

Identity, payload, priority, attempts, timestamps.

Version the schema.

Test serialization round-trips.

## Phase 2 — Stand Up Backend

Use `scripts/file_queue.py` for small scale or learning.

Graduate by the backend ladder with reasons.

Prove durability with kill tests.

## Phase 3 — Lease and Prioritize

Lease 5-15 min; extend long jobs.

Ack only after durable write.

Band priorities; alert on age per band.

## Phase 4 — Review DLQ

Triage daily; fix classes not cases.

Requeue with fixed code only.

Track poison rate.

## Examples

### Example 1: Loop to fleet

User says: "Single script, 8-hour runs."

Actions:

1. Modeled jobs, file queue first
2. 4 workers, no loss in kill test
3. Graduated to Redis at 10x
4. Runtime to 40 min

Result: Scaled safely.

### Example 2: Fairness fix

User says: "Fresh items wait behind bulk."

Actions:

1. Banded urgent/fresh/bulk
2. Weighted 5:3:1
3. P95 age sane
4. Starvation gone

Result: Fair queue.

## Troubleshooting

### Jobs processed twice

Cause: Ack before write or short leases

Fix:

1. Write then ack
2. Extend leases
3. Add idempotency
4. Prove with kill tests

### Jobs stuck invisible

Cause: Dead worker holding lease

Fix:

1. Tune lease timeout
2. Heartbeat long jobs
3. Reaper redelivers
4. Alert on redelivery rate

### DLQ floods

Cause: Target change or bug in handler

Fix:

1. Pause intake
2. Fix the class
3. Replay sample
4. Then requeue

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Model.
- Run.
- Learn.

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

Avoid ack-before-write; leaseless queues; unbounded retries; priority-free floods; unreviewed DLQs; backend by ambition.

## Bundled References

Read `references/queue-ladder.md` when choosing or graduating queue backends.
Run `scripts/file_queue.py` as a tiny durable leased queue (stdlib sqlite).
Copy `assets/checklists.md` into every delivery.
