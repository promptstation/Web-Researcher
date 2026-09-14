# Egress Economics

Attribution: cost per pool = invoice share by GB or requests; cost per 1k successes = pool cost / (successes/1000); attribute by pool x target-class x team monthly; reconcile to invoice within 2 percent or find the gap.

Budgets: per-pool unit budget from trailing 3-month p50; warn at 80, throttle-or-shift at 100; owners paged on breach; success-rate guard blocks savings that hurt outcomes. Forecast quarterly from volume plans.

Levers ranked: retry discipline (cap attempts, backoff) often 20-40 percent; type right-sizing (DC where fits) 10-50 percent; change detection and caching 20-60 percent of fetches; schedule right-sizing; idle-pool retirement. Stack monthly.

Forbidden savings: consent-free supply, politeness cuts, quota overruns, success-guard violations. Report: unit trend, savings shipped with proof, forecast, risks. Finance-friendly one-pager.
