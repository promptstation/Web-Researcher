# Pool Policy

Rotation: per-request for bulk APIs and tolerant pages; sticky 10-30 min for sessions, carts, and multi-step flows; dedicated egress per account for logins. Never rotate inside an authenticated flow. Document per target class with reasons.

Caps: start 1-5 rpm per egress per sensitive domain, 10-60 for tolerant; measure ban-free ceiling over 2 weeks; alert at 80 percent; hard-cap in code. Concurrency 1-3 per egress for browsers, higher for APIs with quota headroom.

Quarantine: trip on 3 consecutive failures, any ban signal, or success under 50 percent over 20 requests; hold 30-120 min; canary-probe with 3 cheap requests; return on 3 green or retire after 3 failed probes. Log every transition.

Spares: 20 percent warm minimum; rebalance in 10 percent steps with 30 clean minutes between; retire egress with 7-day cool observation. Pool metrics: success, p95, quarantine share, rotation rate, cost per 1k.
