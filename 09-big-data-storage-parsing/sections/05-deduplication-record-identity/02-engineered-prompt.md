# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 09 Big Data Storage & Parsing → Section: Deduplication and Record Identity

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Deduplication and Record Identity”** as part of an advanced course in big data storage, parsing, and dataset operations. How stable record IDs, exact dedupe with ledgers, near-duplicate detection with shingles and MinHash, and merge rules keep corpora clean at scale.

The material should teach how to deduplicate scraped corpora reliably. Go beyond surface-level tips and examine dataset engineering as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong dataset quality balances **volume, quality, freshness, cost, and retrievability**. Show how these principles apply differently to single-file scrapes, growing datasets, and archival corpora. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to derive stable record IDs from canonical inputs and versions

Teach how to dedupe exactly with ledgers and conditional writes

Teach how to detect near-duplicates with shingles, Jaccard, and MinHash

Teach how to merge duplicates with survivorship rules and audit trails

Teach how to measure dup rates and prove corpus cleanliness

Include practical methods for real projects. Cover:

* ID derivation
* Exact dedupe
* Shingling
* MinHash/LSH
* Survivorship rules
* Merge audits
* Dup dashboards
* Backfill dedupe

Explain how practitioners can avoid ids unstable (volatile derivation inputs).
Explain how practitioners can avoid near-dup noise (threshold too loose).
Explain how practitioners can avoid merge regret (rules too aggressive).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover p, r, o, d, u, c, t,  , c, a, t, a, l, o, g, s, ,,  , n, e, w, s,  , a, r, c, h, i, v, e, s, ,,  , l, i, s, t, i, n, g,  , c, o, r, p, o, r, a, ,,  , d, o, c, u, m, e, n, t,  , c, o, l, l, e, c, t, i, o, n, s, ,,  , a, n, d,  , p, r, i, c, e,  , h, i, s, t, o, r, i, e, s. Keep examples focused on dataset quality rather than generic advice.

Include practical exercises that require the learner to:

1. Derive IDs for one corpus.
2. Dedupe 100k exactly.
3. Find near-dupes in samples.
4. Merge 100 pairs with rules.
5. Dashboard dup rate.
6. Backfill-dedupe one archive.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from formats, schemas, dedupe, quality, and retention where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize data-engineering literature, format specs (Parquet/JSONL/CSV), SQLite docs, and data-quality frameworks. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **ids-stable checklist**, a **exact-clean checklist**, a **near-found checklist**, a **merged-ruled checklist**, a **rate-low checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
