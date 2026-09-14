# Observability and Data Quality

Use this reference when defining schemas, record IDs, logs, metrics, artifacts, and alerts.

## Record schema

Version every schema. Example `v3` product record:

```json
{
  "record_id": "9f2c7a1b4e8d03aa",
  "job_id": "a1b2c3d4e5f60718",
  "url": "https://example.com/p/123",
  "title": "Acme Kettle 1.7L",
  "price": 49.99,
  "currency": "USD",
  "availability": "in_stock",
  "scraped_at": "2026-09-14T11:00:00Z",
  "version": "v3"
}
```

Validation rules:

- Required: `record_id`, `job_id`, `url`, `title`, `scraped_at`, `version`.
- Types and ranges: price >= 0 when present, URL is http(s), title length 3-300.
- Content floors: HTML length > 5k, extracted text > 200 chars, list pages return >=1 item or explicit empty-page signal.
- Challenge guard: extracted text must not contain challenge markers.
- Bump `version` on selector or field changes; keep old extractors runnable for 7 days for diffing.

Count `validation_failed_total` by reason. A jump after a deploy or at a fixed hour usually means layout change or A/B variant.

## Stable IDs and deduping

- `job_id = sha1(canonical_url + "|" + version)[:16]`
- `record_id = sha1(canonical_url + "|" + page_key + "|" + version)[:16]` where `page_key` is SKU/slug or `main` for single-record pages.
- Canonicalize: lowercase host, strip `utm_*`, `fbclid`, `gclid`, sort remaining query, drop empty fragment.
- Seen-store: in-memory set plus `records.jsonl` rebuild on startup; Redis SET for multi-worker fleets.
- Emit exactly once: skip write when `record_id` seen, but still mark job done and count `deduped_total`.

## Structured logs

One JSON line per job attempt:

```json
{"ts": "2026-09-14T11:00:01Z", "trace_id": "7f3a…", "job_id": "a1b2…", "domain": "example.com", "attempt": 1, "outcome": "success", "latency_ms": 4200, "proxy_pool": "residential-rotating", "challenge_class": null, "error_class": null, "artifact_path": null}
```

Rules:

- Include `trace_id` from queue to browser to record for end-to-end joins.
- Never log passwords, full cookies, auth headers, or raw PII. Hash or redact.
- Log at INFO per job, DEBUG per action, WARN on retriable, ERROR on terminal/dead-letter.
- Ship logs to file plus stdout; aggregate with Loki/ELK/Datadog in production.

## Metrics

Counters (per domain + outcome):

- `jobs_total`, `success_total`, `retriable_total`, `terminal_total`
- `challenges_total{challenge_class}`, `proxy_failures_total{pool}`
- `emitted_total`, `deduped_total`, `validation_failed_total{reason}`
- `breaker_open_total`, `parked_total`

Gauges and histograms:

- `queue_depth`, `queue_age_seconds`, `inflight_contexts`
- `job_latency_ms` histogram, `egress_latency_ms` by pool
- `cost_usd_estimate` counter (proxy + compute per 1k pages)

Print or expose Prometheus text every 60s. The bundled script writes `metrics.json` with the same shape.

## Failure artifacts

On failure only:

- Screenshot (viewport, PII-conscious; blur or mask form inputs).
- HTML snippet hash + first 2k chars for classifier debugging (redact scripts containing tokens).
- HAR when network forensics needed; video only for flake reproduction.
- Store under `./out/failures/<date>/<job_id>-attempt<N>/` with 14-day retention default.

Link `artifact_path` from the job log and dead-letter record.

## Alerts

Warn:

- Success rate <90% over 15 min.
- Challenge rate >5% over 15 min.
- Queue age >2x SLA.
- Validation failures >3% over 1h.

Page:

- Success rate <85% over 15 min.
- Challenge rate >10% over 15 min.
- Dead-letter growth >50 jobs in 10 min.
- Cost burn >150% of daily budget pace.
- Multi-domain spike (ban-wave pattern).

Every alert links to runbook section: halve concurrency, check artifacts, quarantine egress, decide park vs fix vs stop.
