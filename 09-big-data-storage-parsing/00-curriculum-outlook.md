# Course 09 — Big Data Storage & Parsing
## Curriculum Content Outlook (Researching-Outline workflow, compressed to ≤15 sections)

Source course list: `Web researcher and scrapper.txt` — Course 9: Big Data Storage & Parsing
Method: Researching-Outline.md workflow (Steps 1–8) + beginner→expert progression research + compression into groups.
Sections: 10 (within the ≤15 limit). Each section = Summary (what it teaches) + Absorbed Skill (capability gained).

---

**Storage Formats and Selection**

**Summary:** How JSON, JSONL, CSV, SQLite, and Parquet compare for scraped data on appendability, schema evolution, size, and queryability, and how to choose formats per stage of the pipeline.

**Absorbed Skill:** Select storage formats per pipeline stage with honest tradeoff reasoning.

---

**Schema Design and Validation**

**Summary:** How to design record schemas with required fields, types, enums, and identities, how to validate every record at layer boundaries, and how to quarantine rejects with actionable reasons.

**Absorbed Skill:** Design record schemas and validate every record with quarantined rejects.

---

**HTML Parsing at Scale**

**Summary:** How to parse HTML fast and correctly with streaming, selector discipline, encoding handling, and boilerplate removal, from thousands to millions of pages.

**Absorbed Skill:** Parse HTML at scale with fast, correct, boilerplate-free extraction.

---

**Document Parsing Operations**

**Summary:** How to triage, extract text and tables from PDFs and Office documents, handle scanned pages with OCR decisions, and preserve layout signals that matter.

**Absorbed Skill:** Extract text and tables from documents with triage, OCR decisions, and layout care.

---

**Deduplication and Record Identity**

**Summary:** How stable record IDs, exact dedupe with ledgers, near-duplicate detection with shingles and MinHash, and merge rules keep corpora clean at scale.

**Absorbed Skill:** Keep corpora clean with stable IDs, exact and near-dedupe, and merge rules.

---

**Data Quality Monitoring**

**Summary:** How field-fill rates, type/range/enum checks, freshness lag, distribution drift, and golden-record tests combine into continuous data-quality monitoring with alerts.

**Absorbed Skill:** Monitor data quality continuously with fill, validity, freshness, and drift signals.

---

**Incremental and Delta Pipelines**

**Summary:** How change detection, content hashing, high-water marks, and delta emission keep corpora fresh at minimal fetch and compute cost.

**Absorbed Skill:** Run incremental pipelines that fetch, compare, and emit only what changed.

---

**Partitioning and Compaction**

**Summary:** How date, source, and entity partitions, file sizing, compaction, and manifests keep large datasets fast to scan, cheap to store, and easy to expire.

**Absorbed Skill:** Partition and compact datasets for fast scans, cheap storage, and easy expiry.

---

**Search and Retrieval over Corpora**

**Summary:** How SQLite FTS, field indexes, faceted filters, and snippet ranking turn scraped corpora into searchable products with relevance users trust.

**Absorbed Skill:** Build trusted search over scraped corpora with FTS, facets, and snippets.

---

**Retention, Archival and Deletion**

**Summary:** How retention schedules, cold archival, verifiable deletion, and DSAR handling keep datasets compliant and cheap across their full lifecycle.

**Absorbed Skill:** Govern dataset lifecycles with retention, archival, and provable deletion.
