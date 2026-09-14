# Entity Resolution

Normalize: lowercase, strip punctuation/legal suffixes (Inc/LLC/GmbH tables per locale), expand abbreviations via alias tables, unicode-fold. Aliases versioned; never regex-away distinguishing tokens (Jr/Sr, model numbers).

Block: keys like brand+category, phone, domain, geo-cell; multiple passes (recall via union); measure pair reduction (target 99 percent+) and missed-match rate on judged pairs. Score: exact-alias > fuzzy-name + attribute agreement (phone/address/price-band); weights tuned on 500+ judged pairs for 0.95+ precision.

Cluster: connected components on match edges; review band (0.5-0.8) to humans; audit (members, scores, decider, time); never merge across types. Survivorship: per-attribute (trusted-source wins, newest for volatile, union for aliases); provenance: every fact -> source records + extraction versions.

Eval: sample 300+ clusters, judge precision; sample singletons for recall misses; track over time; re-tune quarterly. KB versioned with entity ids stable across rebuilds.
