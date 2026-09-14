# Structured Discovery

Sitemaps: parse index -> URL sets with namespaces (urlset/sitemapindex); handle .gz; 50k/50MB limits per file; record loc+lastmod+changefreq+priority; inventory counts per map; re-fetch daily-ish with etag. News/video/image extensions where offered.

Feeds: poll RSS/Atom with etag/last-modified; extract item links + dates; per-item lag tracked (published->fetched); death detection (no items 2x period -> alert); backfill via sitemap on gaps. Respect TTL/skipHours.

Robots: parse per host (user-agent match, allow/disallow longest-match, crawl-delay, sitemap directives); cache 24h; test parser against edge cases. Lastmod: verify on samples (fetch + hash-compare) before scheduling; trust score per source; liar sources demoted.

Coverage: known = union(sitemaps, feeds, frontier-seen, prior); crawled diffed; gaps triaged (blocked/js/trap/error with counts); report filed per cycle. Discovery fetching polite like crawling.
