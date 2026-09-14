# Resilience Composition

Composition order per call: deadline context -> breaker check -> attempt loop (try, classify, budget-check, backoff+jitter, retry) -> record outcome. Hedge: after p95 delay, fire second attempt; first result wins; cancel loser; cap hedged ratio under 5 percent.

Numbers: attempts 3-5 total; backoff base 0.5-1s doubling to 30-60s cap with full jitter; breaker trips at 50 percent errors over 20+ calls or budget burn 10x; half-open after 30-60s with single probe; cooldown before full close.

Deadlines: connect 3-5s, read 10-30s, operation end-to-end per SLO; propagate remaining budget in headers; never retry past deadline. Classify: retry timeouts/5xx/429; fail fast on 4xx (except 408/429) and auth errors.

Drills: inject latency, errors, and blackholes monthly; assert breaker trips, degradation serves, recovery auto, pages only on budget burn. Record MTTR per drill.
