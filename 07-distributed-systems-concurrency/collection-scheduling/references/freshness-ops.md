# Freshness Ops

SLAs: measure change cadence (sample hourly for a week); SLA = business need or half median-change-interval, whichever looser; schedule slightly inside SLA for margin. Review quarterly; loosen before tightening infra.

Cron: UTC always; validate fields and next-runs before deploy; ledger slots for exactly-once; alert on missed slots within one period; DST test yearly. Prefer scheduler UIs with history over raw crontabs at team scale.

Aging: priority = base + staleness/SLA * weight, capped; bands keep bulk from starving fresh; change detection (etag, lastmod, content hash of normalized regions) gates full fetches; sitemap lastmods drive discovery scheduling.

Backfill: triage SLA-breach first, then revenue, then rest; cap at 2x normal rate or target-safe max; publish ETA; stop expanding scope mid-recovery. Log every outage with cause and prevention.
