---
name: resilience-patterns
description: Compose retries, deadlines, and breakers that fail fast and recover alone. Use when the user asks to add retries with backoff; tune circuit breakers; set request timeouts; stop retry storms; handle flaky APIs.
compatibility: Python 3.10+ stdlib; any HTTP client; failure injection for drills.
metadata:
  author: Promptstation
  version: 1.0.0
  category: distributed-systems
---

# Resilience Patterns

Build clients outages cannot amplify. You budget every retry, jitter every backoff, layer every deadline, trip breakers on budgets, and hedge tails carefully — then drill until recovery is automatic.

Optimize simultaneously for:

- known retry costs
- jittered waits
- fast failures
- auto recovery
- tamed tails

Retryable errors only; budgets cap every path; breakers protect targets as well as callers.

## Use Cases

### Flaky API

Trigger: user says 'partner flakes' or 'timeouts random'

Steps:

1. Classify errors
2. Budget and jitter
3. Layer deadlines
4. Verify calm

Result: Calm resilient client.

### Outage shield

Trigger: user says 'dependency down' or 'cascading failures'

Steps:

1. Trip breaker fast
2. Fail over or degrade
3. Probe half-open
4. Recover auto

Result: Contained dependency failure.

### Tail tamer

Trigger: user says 'p99 terrible' or 'slow tail'

Steps:

1. Measure tail
2. Hedge past p95
3. Cap hedge cost
4. Verify p99 sane

Result: Predictable latency.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Error classification
- Retry budgets
- Backoff parameters
- Deadline values
- Breaker thresholds
- Hedge policy
- Drill results
- Recovery metrics

Never retry non-idempotent or non-retryable errors, and never retry without budget and jitter.

## Phase 1 — Classify Errors

Retryable: timeouts, 5xx, 429; never 4xx except 408/429.

Map each error to a policy.

Log class with every failure.

## Phase 2 — Budget and Back Off

Use `scripts/resilience_kit.py` patterns for retry, timeout, breaker.

Attempts 3-5; base 0.5-1s; cap 30-60s; full jitter.

Honor Retry-After over computed waits.

## Phase 3 — Layer Deadlines

Connect 3-5s; read 10-30s; end-to-end per SLA.

Propagate deadlines downstream.

Fail fast with context.

## Phase 4 — Break and Recover

Trip at error budget burn; half-open probe single.

Degrade gracefully while open.

Drill monthly with injection.

## Examples

### Example 1: Storm stopped

User says: "Our retries DDoSed the partner."

Actions:

1. Jitter plus budgets added
2. Breaker trips in 10s
3. Partner thanked us
4. Policy org-wide

Result: Good citizen client.

### Example 2: Auto recovery

User says: "2am pages for blips."

Actions:

1. Breakers plus half-open
2. Degraded mode clean
3. Pages only on budget burn
4. Sleep restored

Result: Self-healing dependency.

## Troubleshooting

### Breaker flaps

Cause: Thresholds near noise floor

Fix:

1. Widen with error budget
2. Longer windows
3. Separate scopes
4. Verify stable

### Deadlines too tight

Cause: p99 underestimated

Fix:

1. Measure p99/p999
2. Set above with margin
3. Hedge the tail
4. Re-verify SLO

### Hedging doubles load

Cause: Hedge too early or always

Fix:

1. Hedge past p95 only
2. Cap hedge ratio
3. Cancel losers
4. Measure cost

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Classify.
- Compose.
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

Avoid budget-free retries; unjittered backoff; deadline-free calls; breaker-free dependencies; blind hedging; undrilled recovery.

## Bundled References

Read `references/resilience-composition.md` when composing retries, deadlines, and breakers.
Run `scripts/resilience_kit.py` as retry/breaker/deadline reference patterns.
Copy `assets/checklists.md` into every delivery.
