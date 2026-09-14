# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 09 Big Data Storage & Parsing → Section: Search and Retrieval over Corpora

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Search and Retrieval over Corpora”** as part of an advanced course in big data storage, parsing, and dataset operations. How SQLite FTS, field indexes, faceted filters, and snippet ranking turn scraped corpora into searchable products with relevance users trust.

The material should teach how to build search over scraped corpora. Go beyond surface-level tips and examine dataset engineering as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong dataset quality balances **volume, quality, freshness, cost, and retrievability**. Show how these principles apply differently to single-file scrapes, growing datasets, and archival corpora. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to index corpora with SQLite FTS5 (tokenizers, triggers, rebuilds)

Teach how to rank with BM25 and boost by freshness and authority

Teach how to facet by category, date, source, and price for navigation

Teach how to snippet with highlighted matches and context

Teach how to evaluate relevance with judged queries and iterate

Include practical methods for real projects. Cover:

* FTS indexing
* BM25 tuning
* Boost design
* Facet design
* Snippet policy
* Query judging
* Relevance iteration
* Scale planning

Explain how practitioners can avoid index bloat (unused columns or no vacuum).
Explain how practitioners can avoid slow queries (leading wildcards or huge facets).
Explain how practitioners can avoid judging churn (vague relevance grades).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover p, r, o, d, u, c, t,  , c, a, t, a, l, o, g, s, ,,  , n, e, w, s,  , a, r, c, h, i, v, e, s, ,,  , l, i, s, t, i, n, g,  , c, o, r, p, o, r, a, ,,  , d, o, c, u, m, e, n, t,  , c, o, l, l, e, c, t, i, o, n, s, ,,  , a, n, d,  , p, r, i, c, e,  , h, i, s, t, o, r, i, e, s. Keep examples focused on dataset quality rather than generic advice.

Include practical exercises that require the learner to:

1. Index 100k docs.
2. Tune BM25 roughly.
3. Add 3 facets.
4. Snippet 20 queries.
5. Judge 50 queries.
6. Iterate once measurably.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from formats, schemas, dedupe, quality, and retention where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize data-engineering literature, format specs (Parquet/JSONL/CSV), SQLite docs, and data-quality frameworks. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **indexed-100k checklist**, a **ranked-ok checklist**, a **facets-3 checklist**, a **judged-50 checklist**, a **iterated-1 checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
