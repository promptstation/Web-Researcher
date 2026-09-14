# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 09 Big Data Storage & Parsing → Section: Storage Formats and Selection

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Storage Formats and Selection”** as part of an advanced course in big data storage, parsing, and dataset operations. How JSON, JSONL, CSV, SQLite, and Parquet compare for scraped data on appendability, schema evolution, size, and queryability, and how to choose formats per stage of the pipeline.

The material should teach how to select and layer storage formats for scraped data. Go beyond surface-level tips and examine dataset engineering as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong dataset quality balances **volume, quality, freshness, cost, and retrievability**. Show how these principles apply differently to single-file scrapes, growing datasets, and archival corpora. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to compare JSON, JSONL, and CSV on append, schema, size, and tooling

Teach how to use SQLite as the default queryable store under 100GB

Teach how to adopt Parquet for columnar analytics and cheap scans

Teach how to separate raw, clean, and serve layers with clear contracts

Teach how to evolve schemas with versioned readers and backfill plans

Include practical methods for real projects. Cover:

* Format comparison
* Layer separation
* SQLite sizing
* Parquet adoption
* Schema versioning
* Compression policy
* Encoding discipline
* Migration runbooks

Explain how practitioners can avoid encoding soup (mixed source encodings).
Explain how practitioners can avoid sqlite too slow (missing indexes or oversized).
Explain how practitioners can avoid parquet unreadable (writer version skew).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover p, r, o, d, u, c, t,  , c, a, t, a, l, o, g, s, ,,  , n, e, w, s,  , a, r, c, h, i, v, e, s, ,,  , l, i, s, t, i, n, g,  , c, o, r, p, o, r, a, ,,  , d, o, c, u, m, e, n, t,  , c, o, l, l, e, c, t, i, o, n, s, ,,  , a, n, d,  , p, r, i, c, e,  , h, i, s, t, o, r, i, e, s. Keep examples focused on dataset quality rather than generic advice.

Include practical exercises that require the learner to:

1. Compare formats for one dataset.
2. Split one pipeline into 3 layers.
3. Size SQLite for one corpus.
4. Convert one JSONL to Parquet.
5. Version one schema change.
6. Migrate one layer cleanly.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from formats, schemas, dedupe, quality, and retention where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize data-engineering literature, format specs (Parquet/JSONL/CSV), SQLite docs, and data-quality frameworks. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **compared-5 checklist**, a **layered-3 checklist**, a **sized-ok checklist**, a **converted-1 checklist**, a **versioned-live checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
