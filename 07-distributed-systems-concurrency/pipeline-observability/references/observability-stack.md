# Observability Stack

Logs: one JSON line per event with ts, level, logger, run_id, job_id, trace_id, stage, msg, plus outcome fields; INFO for stage transitions, WARN for retried, ERROR for dead-lettered; DEBUG sampled. Scrub tokens, cookies, PII at emission with tests.

Metrics: RED per stage (requests/s, error ratio, p50/p95/p99 duration); USE per host (CPU, RSS, disk, handles); business (records/s, validation rate, freshness lag). Bound labels: domain class not URL, error class not message.

Traces: propagate traceparent across queue payloads and HTTP; sample 1-10 percent plus all errors; link spans to logs. Run reports: counts, rates, tails, top errors, slow exemplars, one page, auto-attached.

Alerts: burn-rate on error budget (fast 1h, slow 6h), queue age per band, run stall (no progress 2x p99), freshness lag vs SLA. Every alert links a runbook; review noise monthly.
