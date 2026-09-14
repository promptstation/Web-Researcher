# Limiter Math

Token bucket: capacity C burst, refill R per second; take(1) blocks or fails when empty; refill with monotonic clock; test: burst C instant, then R/s sustained. Leaky bucket for smooth output; fixed window for quota alignment; sliding window for strict APIs.

Headers: Retry-After seconds or HTTP date (sleep exactly); X-RateLimit-Remaining/Reset (pace to reset); RateLimit-Policy (size buckets under it). On 429 without headers: exponential backoff 1-60s with jitter.

Adaptation: AIMD per scope (halve on 429, +10 percent per clean minute); latency guard (slow when p95 doubles); separate controllers per domain, key, and endpoint class. Never share budgets across tenants.

Backpressure: bounded queues (drop or block producers); pressure signals (queue depth, sink latency, error rate); shed order (bulk, fresh, urgent last); alert on sustained shed. Drill quarterly.
