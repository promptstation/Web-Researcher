# Text Mining

TF-IDF: tokenize per language, lowercase, DF over full corpus with min_df floors (5-10) and max_df ceilings (50-80 percent); sublinear TF; boilerplate cleaned first or template terms dominate. Top terms per doc + per corpus baselined.

Keyphrases: candidate noun n-grams + TF-IDF/TextRank scoring; judge 100+ for precision; keep winners; per-doc top-10 typical. Topics: cluster (k-means over TF-IDF/SBERT) + label from top terms + human rename; stability across seeds; K tuned by coherence + utility, not just metrics.

Trends: baseline per term (4+ weeks); burst = today vs baseline z-score; confirm with slope over 3+ points and actual reads; normalize by corpus volume; alert on confirmed only. Distinguish news spikes (real, fast) from data artifacts (crawl changes).

Eval: judged samples for phrases/topics/trends; precision reported; dashboards show evidence (quotes, counts, charts); refresh scheduled; methods versioned. Unjudged mining never drives decisions.
