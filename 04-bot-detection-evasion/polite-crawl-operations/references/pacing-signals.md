# Pacing Signals

Signal order: Retry-After (seconds or HTTP date) first; 429/503 status second; RateLimit-* and quota headers third; robots crawl-delay fourth; local budget last. Parse dates with timezone care; treat unparseable as 60s and log.

Backoff: full jitter uniform(0, min(cap, base * 2^n)); base 2s, cap 300s default; cut concurrency alongside delays; never retry non-idempotent writes blindly. Recover one step per clean minute, full restore after 10 clean minutes.

Adaptive controller: error rate over 5 percent tightens 50 percent; 429 observed sets floor delay; sustained clean windows relax 10 percent. Couple workers to rate: workers = max(1, rate * latency_target). Log every adaptation with cause.

Quotas: track per window with 20 percent headroom; alert at 70 percent; stop at 100 percent and wait for reset. Parallelism never excuses quota math.
