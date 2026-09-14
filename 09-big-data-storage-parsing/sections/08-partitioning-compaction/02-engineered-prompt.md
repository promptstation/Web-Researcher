# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 09 Big Data Storage & Parsing → Section: Partitioning and Compaction

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Partitioning and Compaction”** as part of an advanced course in big data storage, parsing, and dataset operations. How date, source, and entity partitions, file sizing, compaction, and manifests keep large datasets fast to scan, cheap to store, and easy to expire.

The material should teach how to partition and compact datasets operationally. Go beyond surface-level tips and examine dataset engineering as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong dataset quality balances **volume, quality, freshness, cost, and retrievability**. Show how these principles apply differently to single-file scrapes, growing datasets, and archival corpora. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to design partition keys from query and expiry patterns

Teach how to size files (64-512MB) for scan efficiency

Teach how to compact small files without rewriting history

Teach how to write manifests that make datasets self-describing

Teach how to expire and archive whole partitions cheaply

Include practical methods for real projects. Cover:

* Partition design
* File sizing
* Compaction jobs
* Manifest authoring
* Expiry by partition
* Skew handling
* Backfill isolation
* Cost tracking

Explain how practitioners can avoid partition skew (hot source or date).
Explain how practitioners can avoid compaction churn (compacting live partitions).
Explain how practitioners can avoid manifest drift (writes bypass manifest).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover p, r, o, d, u, c, t,  , c, a, t, a, l, o, g, s, ,,  , n, e, w, s,  , a, r, c, h, i, v, e, s, ,,  , l, i, s, t, i, n, g,  , c, o, r, p, o, r, a, ,,  , d, o, c, u, m, e, n, t,  , c, o, l, l, e, c, t, i, o, n, s, ,,  , a, n, d,  , p, r, i, c, e,  , h, i, s, t, o, r, i, e, s. Keep examples focused on dataset quality rather than generic advice.

Include practical exercises that require the learner to:

1. Design partitions for one dataset.
2. Repartition one messy store.
3. Compact 1k small files.
4. Write one manifest.
5. Expire one quarter.
6. Measure scan wins.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from formats, schemas, dedupe, quality, and retention where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize data-engineering literature, format specs (Parquet/JSONL/CSV), SQLite docs, and data-quality frameworks. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **designed-keys checklist**, a **files-sized checklist**, a **compacted-1k checklist**, a **manifest-live checklist**, a **expired-cheap checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
