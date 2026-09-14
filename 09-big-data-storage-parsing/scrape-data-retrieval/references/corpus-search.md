# Corpus Search

FTS5: virtual table with tokenize=porter (English) or unicode61; index title+body+tags; triggers sync on insert/update/delete; optimize nightly, rebuild weekly-or-on-drift; 10M-doc ceiling-ish per DB before sharding or graduating.

Ranking: BM25(title*3, body*1) baseline; boosts: freshness decay (half-life per corpus), source authority tiers, exact-phrase bonus; document every boost with reason. Latency SLO p95 under 300ms; cache top queries.

Facets: category, source, year/month, price buckets; counts per facet; multi-select with AND/OR documented. Snippets: 2-3 fragments, 40 tokens, <mark> highlights, ellipsis; zero results suggest facet loosening and spell variants.

Judging: 50+ real queries, 3-grade rubric (perfect/partial/wrong), two judges, adjudicate splits; score = graded precision@10; every ranking change A/B judged; ship only judged winners. Graduate to ES/OS on measured latency or scale pain.
