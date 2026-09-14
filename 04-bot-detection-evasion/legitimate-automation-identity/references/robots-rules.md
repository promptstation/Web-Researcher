# Robots Rules

Parsing: groups start with User-agent lines; rules apply to the most specific matching group; Allow overrides Disallow on longest match; * wildcards match sequences; $ anchors ends; Crawl-delay is non-standard but honored politely; Sitemap lines list indexes. Fetch robots per host daily; cache with the delay in mind.

UA standard: Product/Version (+https://purpose-url; contact@email). Purpose pages state operator, purpose, scope, rate, retention, and opt-out. Keep one identity per crawler fleet.

Planning: sitemaps first for URL discovery; crawl-delay as minimum gap; disallowed paths never fetched, linked, or brute-forced; ambiguous matches treated as disallow pending operator reply.

Terms: read automation, aggregation, and redistribution clauses; explicit bans end scope immediately; seek API or written permission as the only escalations. Log every verdict with quotes.
