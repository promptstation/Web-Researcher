# Vision Serving

Cards: purpose, data (sources, sizes, licenses, splits), eval (headline + slices + calibration + robustness + fairness), limits (known failures, OOD behavior), ethics (sensitive uses, mitigations), owner + review date. No card, no prod.

Serving: latency budget p95 (e.g., 200ms); ladder: batching, FP16/INT8, distillation, caching, smaller backbone; verify metrics kept at each step; load-test to knee; autoscale tested. Version every artifact in a registry.

Releases: shadow 100 percent with offline comparison; canary 5-25-100 with gates (error proxies, latency, drift); auto-rollback armed; one-command rollback drilled quarterly. Releases off-hours for risky changes.

Monitoring: input drift (embedding or stat distance), confidence distribution shifts, slice proxies, latency, error rates; human sample audits weekly; alert on burn; postmortem every rollback into prevention.
