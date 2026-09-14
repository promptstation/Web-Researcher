# Routing Policy

Table shape: ordered rules of (match dimensions -> pool, priority, caps); first match wins; explicit default last (usually cheapest vetted pool, never unvetted). Dimensions: target class, geo need, sensitivity tier, cost tier, account pin. Version every change with reason.

Failover: pool health gate (success over 20+ outcomes, ban rate, latency); trip shifts new assignments, drains in-flight; hysteresis (trip 50, return 75) plus 15-min cooldown; alert on every shift with cause. RTO target under 5 min; drill quarterly.

Decisions: log request class, matched rule, pool, health at decision, and outcome; retain 90 days; weekly audit (default share under 5 percent, sensitive never misrouted); monthly cost and compliance rollups.

Changes: shadow-test new tables on 7 days of replayed decisions; diff rule hits and cost; canary 5 percent live; full rollout on clean 48h. Roll back on any sensitivity violation instantly.
