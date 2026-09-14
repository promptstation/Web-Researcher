# DQ Monitoring

Fills: per-field non-null rate per source per batch; bands from 30-day p10/p90; alert on 2 consecutive breaches; price/identity/timestamp fields get tightest bands. Validity: type/range/enum/format suite per batch; block serve promotion on fail; quarantine coded.

Freshness: fetched-to-served lag p50/p95 per dataset; SLA per consumer need; alert at 80 percent of SLA; segment by source to find slow paths. Volume: records per batch banded; drops and spikes both alert (outages vs dupes).

Drift: baseline price/category/geo distributions monthly; chi-square or PSI-ish eyeball on dashboards; investigate moves over 10 percent; confirm real (re-baseline) or bug (fix). Goldens: 20+ hand-verified records per critical feed; exact-match on identity plus tolerance on volatile fields; fail loud.

SLOs: pass rate (e.g., 99.5), fill floors per critical field, lag ceilings, golden 100 percent. Breakage playbook: detect, pause serve, fix extractor, backfill gap, verify goldens, postmortem.
