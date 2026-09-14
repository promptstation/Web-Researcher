# Frontier Design

Priority: score = w1*value + w2*inlinks + w3*change_rate - w4*depth; normalize per host to avoid starvation; re-score on revisit with measured change. Budgets: max pages per host per day; max per URL pattern; global stop conditions.

Politeness: fetch robots.txt per host (cache 24h); delay = max(crawl-delay, 1s default, adaptive on errors); concurrency 1-2 per host; identify with UA + contact; honor 429/Retry-After strictly. Log (host, url, delay, status) for every fetch.

Seen: canonicalize (lower host, strip tracking params, sort query, drop fragments, normalize path); sharded seen-store (sqlite per shard, bloom prefilter at scale); trap patterns (calendars, facets, sessions) capped per pattern with regex rules.

Revisit: change-rate per URL class from history; revisit interval = min(SLA, k/rate); sitemap lastmod as hint; lag dashboard per class; full recrawl path for corruption. Coverage = fetched / known(sitemap+seen+seed); report gaps with reasons.
