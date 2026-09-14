# KG Building

Schema: predicates with domain/range, cardinality, temporal validity; closed core relations + open extension with review. Extract: patterns + LLM-schema for text, direct for tables/infoboxes; eval 300+ triples for precision per predicate.

Linking: mentions -> canonical entities (aliases, blocking, review band); confidence = source trust x agreement x extractor precision; floor for serving (e.g., 0.7), band for review. Provenance: every triple -> (source URLs, extracted_at, extractor version).

Conflicts: policy per predicate (recency for prices, authority for official, multi-truth for subjective); surface conflicts to consumers with sources; human-review top-100 by impact; log resolutions. Never silent average.

Serve: query by entity/relation with confidence + provenance; eval answers judged; refresh change-driven with SLA; version snapshots. KG precision target 0.9+ on served triples.
