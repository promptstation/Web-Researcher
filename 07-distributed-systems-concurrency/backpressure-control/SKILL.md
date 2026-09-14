---
name: backpressure-control
description: Shape traffic with precise limiters and honest backpressure. Use when the user asks to implement rate limiting; handle 429 responses; respect Retry-After headers; add backpressure to pipeline; stop API quota exhaustion.
compatibility: Python 3.10+ stdlib; any HTTP client; headers from your APIs.
metadata:
  author: Promptstation
  version: 1.0.0
  category: distributed-systems
---

# Backpressure Control

Send traffic targets welcome. You implement correct limiters, honor every rate header, adapt to 429s instantly, propagate pressure end to end, and shed gracefully instead of collapsing.

Optimize simultaneously for:

- correct limiters
- honored headers
- adaptive rates
- wired pressure
- graceful sheds

Targets set the pace; 429s and Retry-After are law, never suggestions.

## Use Cases

### API quota

Trigger: user says 'hitting rate limits' or '429s rising'

Steps:

1. Read quota headers
2. Size limiter under quota
3. Adapt on 429
4. Verify zero overage

Result: Quota-respecting client.

### Polite crawl

Trigger: user says 'throttle per domain' or 'crawl-delay'

Steps:

1. Set per-domain buckets
2. Honor robots delays
3. Adapt on errors
4. Log compliance

Result: Polite steady crawl.

### Overload drill

Trigger: user says 'sink is slow' or 'queue exploding'

Steps:

1. Signal pressure upstream
2. Slow producers
3. Shed low priority
4. Recover cleanly

Result: Graceful overload.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Limiter spec with math
- Header handling map
- Adaptation rules
- Pressure wiring diagram
- Shedding policy
- Quota dashboards
- Overage incident log
- Drill evidence

Never exceed stated quotas or ignore Retry-After; never buffer unbounded instead of signaling.

## Phase 1 — Implement Limiters

Use `scripts/token_bucket.py` as the reference implementation.

One limiter per domain, key, or quota scope.

Test burst and refill math.

## Phase 2 — Honor Headers

Parse Retry-After, RateLimit-Remaining, Reset.

Sleep exactly, then resume.

Log every 429 with cause.

## Phase 3 — Adapt

Halve on 429 storms; additive recovery.

Track latency as early signal.

Separate per-scope controllers.

## Phase 4 — Wire Pressure

Sink slowness slows sources.

Bound every queue.

Shed low priority first.

## Examples

### Example 1: Quota zero

User says: "429s daily on partner API."

Actions:

1. Header-driven limiter
2. Adaptive backoff
3. Zero 429s for 60 days
4. Dashboard live

Result: Perfect quota citizenship.

### Example 2: Sink protection

User says: "DB falls over nightly."

Actions:

1. Pressure wired to fetchers
2. Bounded queues
3. Graceful sheds
4. No outage since

Result: Protected sink.

## Troubleshooting

### Limiter leaks over quota

Cause: Clock refill or multi-process drift

Fix:

1. Centralize limiter
2. Use monotonic clocks
3. Re-test math
4. Monitor overage

### Recovery too slow

Cause: Over-aggressive backoff floor

Fix:

1. Additive increase
2. Cap backoff
3. Jitter recovery
4. Verify ramp

### Pressure deadlock

Cause: Circular waits or unbounded buffer

Fix:

1. Bound all queues
2. Order lock acquisition
3. Timeout waits
4. Drill recovery

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Limit.
- Honor.
- Wire.

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

Avoid limiter-free clients; ignored Retry-After; shared cross-scope budgets; unbounded buffers; collapse instead of shed; untested limiter math.

## Bundled References

Read `references/limiter-math.md` when implementing or tuning limiters.
Run `scripts/token_bucket.py` as a correct token-bucket reference.
Copy `assets/checklists.md` into every delivery.
