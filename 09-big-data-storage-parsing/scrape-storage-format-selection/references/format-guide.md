# Format Guide

Raw layer: JSONL (one record per line) gzipped; appendable, streamable, diffable; immutable once written; checksummed. Never CSV for raw (quoting pain) or pretty JSON (unstreamable).

Clean layer: SQLite under ~100GB with indexes (single-file, queryable, portable); Parquet beyond or for analytics scans (10-100x scan wins, predicate pushdown). Validate every record entering clean; quarantine rejects with reasons.

Serve layer: shaped per consumer (API dumps, search indexes, aggregates); rebuildable from clean; versioned snapshots. Encoding UTF-8, timestamps UTC ISO-8601, nulls explicit, money in minor units with currency.

Evolution: schema versions (v1, v2) with changelogs; readers declare supported versions; dual-read windows minimum 30 days; backfills verified by counts and hashes; retire with notice and archive.
