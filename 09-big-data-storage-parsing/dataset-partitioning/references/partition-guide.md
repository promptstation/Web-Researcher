# Partition Guide

Keys: date (fetched_date, monthly or daily by volume) first for expiry and recency queries; source or class second for isolation; never high-cardinality IDs (millions of partitions kill listings). Keep total partitions under ~10k per dataset.

Files: 128-512MB each (row groups ~128MB for Parquet); compact sealed partitions below 64MB; never rewrite live partitions; verify row counts and hashes across compaction. Naming: {key=value}/part-{n}.{ext} (Hive style) for tool compatibility.

Manifests: JSON per dataset version listing files, counts, byte sizes, hashes, schema version, written_at; readers load manifest (no directory listings); regenerate atomically per commit; retain old manifests for time travel.

Expiry: drop whole partition dirs; manifest diff as deletion proof; archive-to-cold before delete per retention; backfills write to staging partitions then swap. Scan benchmarks before/after every layout change.
