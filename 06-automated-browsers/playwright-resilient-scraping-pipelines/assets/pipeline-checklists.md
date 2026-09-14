# Pipeline Checklists (copy into delivery PR)

## Pre-flight

- [ ] Scope and freshness SLA stated (URLs, domains, refresh cadence).
- [ ] Politeness budget set per domain (rate, burst, concurrency, crawl-delay honored).
- [ ] Storage decided: records JSONL, checkpoint, failures dir, retention days.
- [ ] PII handling defined: minimization, redaction, access, retention.
- [ ] Terms of Service and robots.txt reviewed; API-first alternative considered.
- [ ] Cost budget set per 1k pages by domain and proxy tier.

## Throttle-and-retry

- [ ] Token bucket + global semaphore enforced before context creation.
- [ ] Retry taxonomy implemented (retriable vs terminal + error_class logging).
- [ ] Backoff uses full jitter; base/cap/max-attempts documented.
- [ ] Retry-After honored when present.
- [ ] Circuit breaker trips on consecutive failures / challenge / 429 spikes.
- [ ] Dead-letter queue captures terminal failures with reason + artifact.

## Proxy-and-challenge

- [ ] Pool per tier selected; login traffic isolated with sticky sessions.
- [ ] Context identity aligned (UA, viewport, locale, timezone); hardening justified.
- [ ] Challenge detectors active (URL + title + body markers + selectors).
- [ ] Triage path: backoff → rotate → recycle → park after 3 hits.
- [ ] Egress quarantine + canary probe implemented.
- [ ] Human-review queue defined; no auto-solve where prohibited.

## Observability

- [ ] JSON logs per attempt with trace_id, job_id, domain, outcome, latency, pool, challenge/error class.
- [ ] No secrets or raw PII in logs or artifacts.
- [ ] Metrics emitted: success/challenge/terminal/dedupe/validation/cost.
- [ ] Failure artifacts captured (screenshot + HTML hash; HAR/video only when needed).
- [ ] Alerts set: success-rate, challenge-rate, queue age, dead-letter, cost.
- [ ] End-of-run summary generated with next actions.

## Data-quality-and-resume

- [ ] Schema versioned; required fields + content floors validated.
- [ ] Stable job_id and record_id from canonical URL + version.
- [ ] Exactly-once emission via seen-store rebuilt from records file.
- [ ] Checkpoint fsynced every ≤25 jobs and on SIGTERM/SIGINT.
- [ ] Kill-and-resume tested: no loss beyond one lease window, zero duplicates.
- [ ] Layout-change drill documented: detect via validation spike → pin fix → bump version → requeue affected IDs.
