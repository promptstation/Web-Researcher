# Incremental Design

Signal ladder: sitemap lastmod (cheapest, discovery), HEAD/conditional GET with etag (cheap, per-URL), content hash compare (authoritative), full parse (last resort). Log skips with signal proof; periodic full verification (weekly/monthly) catches signal lies.

Normalization: strip timestamps, session IDs, ads, view counts, A/B noise before hashing; hash per-field for partial updates; store (id -> hash, fetched_at) in SQLite; re-baseline after extractor changes with versioned hashes.

Deltas: emit {op: insert|update|delete, id, before_hash, after, at}; deletes confirmed on 2 consecutive absences; watermarks per source (last fully-processed marker); resume from marks; bound backfills.

Reconciliation: inputs (seen URLs) = emitted + skipped + quarantined; lag per record; gap list with reasons; file per increment. Full re-crawl runbook kept warm for corruption recovery.
