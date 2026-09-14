# Schema Discipline

Anatomy: record_id (stable identity), source_url + fetched_at + extractor_version (lineage), required business fields, optional enrichments. Required = pipeline fails without it; optional = nullable with documented meaning.

Types: money in minor integer units plus currency enum; timestamps UTC ISO-8601; URLs canonicalized; enums closed with OTHER escape plus review; text trimmed with max lengths; numbers ranged. Strict by default; loosen only with versions.

Validation: every boundary (extract->raw sanity, raw->clean strict, clean->serve contract); per-record fail with codes MISSING/TYPE/RANGE/ENUM/IDENTITY/STALE; quarantine preserves raw plus errors; pass-rate SLO (e.g., 99.5 percent) alerted.

Contracts: consumers pin schema versions; producers announce bumps 14+ days; dual-read windows; breaking changes get migration guides. Schema registry (even a folder) is the source of truth.
