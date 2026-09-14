# LLM Economics

Accounting: tokens in/out per call per task per model; cost = tokens x tier rates; attribute 100 percent to tasks weekly; unit = cost per 1k tasks; alert 80 warn / 100 throttle-or-escalate. Dashboards per team.

Levers ranked: prompt trimming (20-50 percent), caching (30-70 percent on repeats), small-model routing (50-80 percent on easy), batch APIs (50 percent off-peak), context pruning (summarize, retrieve-less). Stack monthly with quality guards.

Latency: SLO p95 per surface (chat 2s, batch hours); stream online; batch offline; fallback chains (small-fast on timeout); cap context and max-tokens; hedge only past p95 with cost caps. Measure end-to-end, not model-only.

Guards: quality suite per task gates every change; silent downgrades forbidden; routing audited weekly; savings reported with quality deltas. Finance-friendly monthly one-pager.
