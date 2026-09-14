---
name: proxy-pool-operations
description: Operate proxy pools with sound rotation, caps, and auto-quarantine. Use when the user asks to rotate proxies correctly; manage sticky sessions; quarantine bad proxies; cap concurrency per IP; rebalance proxy pools.
compatibility: Any provider with rotation controls; pool state in config or DB; metrics from logs.
metadata:
  author: Promptstation
  version: 1.0.0
  category: proxy-management
---

# Proxy Pool Operations

Run pools that heal themselves. You rotate by target class, pin sessions only where needed, cap every egress from measurement, quarantine failures in minutes, and keep spares warm for painless rebalance.

Optimize simultaneously for:

- sound rotation
- controlled sessions
- measured caps
- fast quarantine
- warm spares

Rotation serves politeness and reliability, never ban evasion against stated access decisions.

## Use Cases

### Pool setup

Trigger: user says 'set up rotation' or 'new pool'

Steps:

1. Classify targets
2. Set rotation per class
3. Cap per egress
4. Arm quarantine

Result: Healthy new pool.

### Ban wave

Trigger: user says 'IPs dying' or 'success dropping'

Steps:

1. Quarantine fast
2. Slow rotation burn
3. Probe recovery
4. Fix root cause

Result: Contained wave.

### Rebalance

Trigger: user says 'add capacity' or 'migrate pools'

Steps:

1. Warm spares
2. Shift gradually
3. Watch metrics
4. Retire cleanly

Result: Painless rebalance.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Rotation policy per class
- Session TTL map
- Egress cap table
- Quarantine rules
- Probe procedure
- Spare inventory
- Pool dashboards
- Incident log

Never rotate to dodge explicit bans, and never run pools without quarantine and spares.

## Phase 1 — Design Rotation

Per-request for bulk tolerant; sticky for logins and carts.

TTL 5-30 min; document per class.

Simulate with `scripts/pool_simulator.py --egress 50 --rpm 600`.

## Phase 2 — Cap Egress

Measure tolerance per target class.

Cap requests and concurrency per egress.

Alert before caps, not after.

## Phase 3 — Quarantine Fast

Trip on 3 consecutive failures or ban signal.

Probe recovery with canaries.

Auto-return or retire.

## Phase 4 — Rebalance

Warm spares at 20 percent.

Shift 10 percent steps.

Verify metrics each step.

## Examples

### Example 1: Wave contained

User says: "Success 90 to 40 overnight."

Actions:

1. Quarantined 30 percent auto
2. Root cause: cap too high
3. Lowered, probed back
4. Green in 2 hours

Result: Self-healed pool.

### Example 2: Migration clean

User says: "Move 200 egress live."

Actions:

1. Warmed spares
2. 10 percent steps
3. Zero success dip
4. Old retired clean

Result: Invisible migration.

## Troubleshooting

### Rotation burns IPs

Cause: Per-request on sensitive targets

Fix:

1. Move to sticky
2. Slow cadence
3. Fix root behavior
4. Review policy

### Sticky leaks across users

Cause: Shared affinity map

Fix:

1. Scope affinity per account
2. Expire aggressively
3. Audit map
4. Isolate pools

### Quarantine flaps

Cause: Thresholds at noise floor

Fix:

1. Require 3 consecutive
2. Add ban-signal weight
3. Cooldown returns
4. Tune quarterly

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Design.
- Guard.
- Grow.

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

Avoid rotation-by-default; mid-login rotation; cap-free egress; quarantine-free pools; spare-free fleets; evasion-framed rotation.

## Bundled References

Read `references/pool-policy.md` when designing rotation or quarantine.
Run `scripts/pool_simulator.py` to sanity-check pool sizing.
Copy `assets/checklists.md` into every delivery.
