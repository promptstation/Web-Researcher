# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 09 Big Data Storage & Parsing → Section: Incremental and Delta Pipelines

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Incremental and Delta Pipelines”** as part of an advanced course in big data storage, parsing, and dataset operations. How change detection, content hashing, high-water marks, and delta emission keep corpora fresh at minimal fetch and compute cost.

The material should teach how to run incremental collection pipelines. Go beyond surface-level tips and examine dataset engineering as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong dataset quality balances **volume, quality, freshness, cost, and retrievability**. Show how these principles apply differently to single-file scrapes, growing datasets, and archival corpora. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to detect changes with etags, lastmod, sitemaps, and hashes before full fetches

Teach how to hash normalized content so volatile noise never flags changes

Teach how to track high-water marks per source for resumable increments

Teach how to emit inserts, updates, and deletes as clean deltas

Teach how to prove completeness with reconciliation after every increment

Include practical methods for real projects. Cover:

* Change signals
* Normalization
* Content hashing
* Watermarking
* Delta emission
* Delete detection
* Reconciliation
* Backfill bounds

Explain how practitioners can avoid hash churn (volatile regions unnormalized).
Explain how practitioners can avoid missed changes (weak signals trusted blindly).
Explain how practitioners can avoid watermark stuck (poison item blocks advance).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover p, r, o, d, u, c, t,  , c, a, t, a, l, o, g, s, ,,  , n, e, w, s,  , a, r, c, h, i, v, e, s, ,,  , l, i, s, t, i, n, g,  , c, o, r, p, o, r, a, ,,  , d, o, c, u, m, e, n, t,  , c, o, l, l, e, c, t, i, o, n, s, ,,  , a, n, d,  , p, r, i, c, e,  , h, i, s, t, o, r, i, e, s. Keep examples focused on dataset quality rather than generic advice.

Include practical exercises that require the learner to:

1. Add etag checks to one feed.
2. Hash one corpus normalized.
3. Watermark one source.
4. Emit one clean delta.
5. Detect deletes once.
6. Reconcile one increment.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from formats, schemas, dedupe, quality, and retention where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize data-engineering literature, format specs (Parquet/JSONL/CSV), SQLite docs, and data-quality frameworks. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **signals-live checklist**, a **hashed-clean checklist**, a **watermarked-1 checklist**, a **delta-pure checklist**, a **reconciled-ok checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
