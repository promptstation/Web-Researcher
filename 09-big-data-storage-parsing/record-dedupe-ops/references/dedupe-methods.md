# Dedupe Methods

IDs: hash(canonical URL or natural key + extractor version); stable across runs; collisions handled by content check; indexed unique. Exact: ledger check before write, upsert on ID, reconcile nightly.

Near: normalize text (lower, strip, collapse space); shingle k=5 words; Jaccard threshold 0.8-0.9 start; blocking by category/brand/price-band to cut pairs; MinHash+LSH (datasketch) beyond ~1M records. Sample 200+ pairs per threshold tune; target precision over 95 percent.

Merge: survivorship per field (newest non-null wins default; price from trusted source; images union); audit (kept ID, merged IDs, rule, time); low-confidence band to humans; never cross entity types; restore path from audit.

Proof: dup rate = dup pairs / records, trended; exact zero after gates; near under target (e.g., 1 percent); backfill reports with before/after; dashboard forever.
