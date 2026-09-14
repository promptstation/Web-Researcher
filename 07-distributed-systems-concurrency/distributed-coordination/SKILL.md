---
name: distributed-coordination
description: Coordinate fleets with fenced locks, single leaders, and exactly-once schedules. Use when the user asks to prevent duplicate cron runs; elect a leader process; distributed locking in Python; shard work across workers; avoid split-brain schedulers.
compatibility: Python 3.10+; Redis or Postgres for multi-host; file locks for single host.
metadata:
  author: Promptstation
  version: 1.0.0
  category: distributed-systems
---

# Distributed Coordination

Keep fleets acting as one. You lock with leases and fencing, elect single leaders, schedule exactly once, shard deterministically, and fail closed so split-brain stays theoretical.

Optimize simultaneously for:

- fenced locks
- single leaders
- once-only schedules
- clean shards
- closed failures

One owner per decision at a time; fail closed on doubt; prove with failover drills.

## Use Cases

### Cron once

Trigger: user says 'cron runs twice' or 'duplicate schedules'

Steps:

1. Ledger scheduled runs
2. Lock per slot
3. Fence with tokens
4. Prove single

Result: Exactly-once schedules.

### Leader tasks

Trigger: user says 'one worker must' or 'elect coordinator'

Steps:

1. Elect with lease
2. Heartbeat steady
3. Fail over fast
4. Fence the old

Result: Single coordinator always.

### Shard fleet

Trigger: user says 'split domains' or 'no overlap'

Steps:

1. Hash-shard deterministically
2. Assign per worker
3. Rebalance on change
4. Verify coverage

Result: Overlap-free fleet.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Lock spec with TTL
- Fencing design
- Election log
- Schedule ledger
- Shard map
- Failover evidence
- Clock assumptions
- Split-brain analysis

Never coordinate without leases and fencing, and never fail open on ownership doubt.

## Phase 1 — Lock Safely

Use `scripts/file_lock.py` on single hosts; Redis Redlock or Postgres advisory multi-host.

TTL 2-3x work time; extend heartbeats.

Fence every guarded action with tokens.

## Phase 2 — Elect Leaders

One scheduler leader with short lease.

Failover under 2x lease.

Old leader fenced before new acts.

## Phase 3 — Schedule Once

Ledger every slot before running.

Skip on ledgered slot.

Reconcile missed slots.

## Phase 4 — Shard and Drill

Deterministic hash sharding.

Kill leaders quarterly.

Prove single ownership.

## Examples

### Example 1: Double-cron

User says: "Billing crawl runs twice nightly."

Actions:

1. Ledgered slots, locked runs
2. Duplicates zero
3. Missed-slot alerts
4. Calm ever since

Result: Once-only schedule.

### Example 2: Failover proof

User says: "Prove leader safety."

Actions:

1. Killed leader mid-schedule
2. Failover 8s, fenced old
3. No double-run
4. Drill recorded

Result: Trusted election.

## Troubleshooting

### Lock expires mid-work

Cause: TTL under work time

Fix:

1. Extend heartbeats
2. Raise TTL
3. Chunk work under TTL
4. Monitor hold times

### Two leaders briefly

Cause: Slow failover detection

Fix:

1. Shorten lease
2. Fence with tokens
3. Fail closed
4. Drill partition

### Clock skew breaks TTLs

Cause: NTP drift across hosts

Fix:

1. Enforce NTP
2. Use monotonic where local
3. Add skew margins
4. Alert on drift

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Lock.
- Lead.
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

Avoid leaseless locks; unfenced writes; multi-leader schedules; ledger-free cron; overlapping shards; fail-open ownership.

## Bundled References

Read `references/coordination-safety.md` when locking, electing, or scheduling.
Run `scripts/file_lock.py` as a cross-process single-host lock.
Copy `assets/checklists.md` into every delivery.
