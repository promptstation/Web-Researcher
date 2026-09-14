# Chunking Guide

Sizing: 200-800 tokens per chunk for QA; smaller (100-300) for precise lookup, larger (800-1500) for synthesis; overlap 10-20 percent or 1-2 sentences; never split mid-sentence except hard caps. Section-aware splits beat fixed windows.

Metadata: doc_id, source_url, title, section_path, lang, date, version — every chunk, filterable. Parent-child: small retrieval chunks pointing to larger context; summaries for long docs. Tables/lists kept whole or skipped deliberately.

Embeddings: pin model version; dedupe texts before embedding; batch for cost; track tokens and dollars; version index as (corpus_version, chunk_spec, model). Rebuild or upsert on corpus change with freshness SLA.

Eval: 50+ judged queries with known-good chunks; recall@5/10 primary; failure taxonomy (chunking, embedding, ranking); one fix at a time; ship judged winners. Filters (date/source) tested as first-class.
