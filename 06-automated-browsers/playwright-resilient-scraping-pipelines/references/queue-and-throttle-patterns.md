# Queue and Throttle Patterns

Use this reference when modeling jobs, choosing a queue backend, or tuning throttles, retries, and circuit breakers.

## Job model

Required fields:

- `job_id`: stable hash of canonical URL + extraction version.
- `url`: canonical URL (tracking params stripped).
- `domain`: lowercase host for throttle keying.
- `priority`: 0-9, higher runs first.
- `attempts`: incremented on each lease.
- `max_attempts`: default 4.
- `lease_until`: ISO timestamp; expired leases return to queued.
- `version`: extraction schema version, e.g. `v3`.

Keep jobs small and JSON-serializable. Store large payloads in object storage and pass pointers.

## Queue backends

| Scale | Backend | Notes |
|---|---|---|
| <10k jobs, single box | Python `asyncio.Queue` + JSON checkpoint | Simplest; bundled script uses this. Survives restarts via checkpoint file. |
| 10k-500k jobs, few workers | Redis + RQ / BullMQ | Priorities, delays, dead-letter via failed registry. Set `visibility timeout` 10 min. |
| 500k+ or multi-tenant | RabbitMQ / Celery / Postgres-backed queue | Durable, routable per domain, auditable. Use per-domain queues for independent throttles. |

Always separate hot retries from dead-letter. Hot retries requeue with delay. Dead-letter requires human or migration action.

## Per-domain throttling

Use token bucket per domain plus global semaphore:

- Token bucket: `rate` tokens/min, `burst` = 2x rate/60, refill continuously.
- Global semaphore: `max_contexts` across all domains (start 3-8 per 8GB worker).
- Honor `Retry-After` and `crawl-delay` when present; take the max of configured and signaled delay.

Starting points:

- Tolerant docs/blogs: 30-60 req/min, burst 5.
- E-commerce/marketplaces: 12-30 req/min, burst 3.
- Defended targets: 6-12 req/min, burst 2, concurrency 1-2.

Measure 429 + challenge rate for 15 minutes before raising limits.

## Retry taxonomy

Retriable (requeue with backoff):

- `timeout`, `navigation-reset`, `target-crashed`, `proxy-disconnect`
- HTTP 408, 425, 429, 500, 502, 503, 504
- `challenge-detected` (first 2 attempts only, then park)

Terminal (dead-letter immediately):

- HTTP 404, 410
- `login-revoked`, `forbidden-permanent` after cooldown probe
- `validation-failed-schema-break` (layout changed; needs extractor fix)
- `robots-disallowed` or `tos-blocked` (do not retry; escalate scope decision)

Log `error_class` on every outcome. Alert when any class spikes.

## Backoff with jitter

Full jitter (preferred for scraping fleets):

```python
import random
sleep = random.uniform(0, min(cap, base * (2 ** attempt)))
```

Defaults: `base=2s`, `cap=120s`, `max_attempts=4`.

- Always add jitter. Synchronized retries from N workers look like a DDoS.
- Double `cap` when the breaker is open.
- Add `Retry-After` seconds on top of computed sleep when the header exists.

## Circuit breaker per domain

Trip when:

- 10 consecutive retriable failures, or
- challenge rate >30% over rolling 5 min, or
- 429 rate >20% over rolling 5 min.

When open:

- Halve concurrency for that domain (min 1).
- Double delays and caps.
- Park new leases 10 min; keep one canary worker probing every 2 min.
- Auto-half-open on 3 consecutive canary successes.

Record breaker transitions in logs with reason and counts.

## Checkpointing and resume

- Append every validated record to `records.jsonl` immediately.
- Add `job_id` to done-set only after fsync.
- Persist done-set to `checkpoint.json` every 25 jobs and on SIGTERM/SIGINT.
- On startup, rebuild seen `record_id` set from `records.jsonl` to guarantee exactly-once emission even if checkpoint lagged.

Lease window: 10 minutes. A killed worker loses at most one window of in-flight jobs, which safely requeue because jobs are idempotent.
