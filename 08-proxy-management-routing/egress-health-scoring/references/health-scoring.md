# Health Scoring

Signals: success rate (40), p95 latency vs baseline (20), ban signals (20), geo/ASN drift (10), cost per success (10). Decay: half-life 24h for successes, 6h for bans. Score 0-100 per egress per day minimum; per hour for large fleets.

Thresholds: warn 70 (watch), quarantine 50 (auto-hold 1-2h), retire after 3 failed canary cycles. Minimum 20 outcomes before trips; new egress start at 60 neutral. Tune: cost of false quarantine vs cost of bad traffic.

Lifecycle: active -> warned -> quarantined -> canary -> graduating (5/25/100 percent steps, 30 clean min each) -> active; or -> retired (7-day cool, then release). Every transition logged with reason and actor.

Dashboards: fleet histogram, bottom-10 table, quarantine timeline, provider comparison, cost-per-success trend. Weekly review; monthly provider scorecards from the same data.
