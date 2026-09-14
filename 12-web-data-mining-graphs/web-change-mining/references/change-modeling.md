# Change Modeling

Histories: (url, fetched_at, content_hash, status, bytes) per fetch; normalized hashes only; retain 6-12 months. Timelines per URL show change events; noise (ads, timestamps) normalized away or rates lie.

Rates: lambda = changes / observed time per URL, pooled per class (section/template); Poisson-ish assumption checked on samples; band classes (hot/warm/cold/frozen); revisit interval = min(SLA_need, k/lambda) capped by politeness. Re-model quarterly.

Schedules: fast lanes for hot (hourly-ish), routine for warm (daily/weekly), lazy for cold (monthly), frozen on demand; sitemap/feed hints accelerate; politeness caps everything. Lag: change-to-fetch estimated from timelines; p50/p95 per class; SLA per consumer.

Proof: lag dashboards; quarterly audits (sample URLs, verify served==live within SLA); reports filed. Full re-crawl runbook for model breaks.
