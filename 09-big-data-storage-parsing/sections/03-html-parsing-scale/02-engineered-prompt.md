# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 09 Big Data Storage & Parsing → Section: HTML Parsing at Scale

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“HTML Parsing at Scale”** as part of an advanced course in big data storage, parsing, and dataset operations. How to parse HTML fast and correctly with streaming, selector discipline, encoding handling, and boilerplate removal, from thousands to millions of pages.

The material should teach how to parse HTML at scale correctly and fast. Go beyond surface-level tips and examine dataset engineering as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong dataset quality balances **volume, quality, freshness, cost, and retrievability**. Show how these principles apply differently to single-file scrapes, growing datasets, and archival corpora. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to choose html.parser, lxml, and BeautifulSoup by speed and tolerance needs

Teach how to stream and chunk large documents without memory blowups

Teach how to handle encodings, entities, and malformed markup robustly

Teach how to remove nav, ads, and boilerplate with content scoring

Teach how to benchmark parsing throughput and parallelize safely

Include practical methods for real projects. Cover:

* Parser selection
* Streaming design
* Encoding normalization
* Boilerplate scoring
* Selector discipline
* Throughput benches
* Parallel parsing
* Golden fixtures

Explain how practitioners can avoid parser crashes on pages (malformed markup or huge docs).
Explain how practitioners can avoid selectors rot (template changes).
Explain how practitioners can avoid memory grows (dom retention or leaks).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover p, r, o, d, u, c, t,  , c, a, t, a, l, o, g, s, ,,  , n, e, w, s,  , a, r, c, h, i, v, e, s, ,,  , l, i, s, t, i, n, g,  , c, o, r, p, o, r, a, ,,  , d, o, c, u, m, e, n, t,  , c, o, l, l, e, c, t, i, o, n, s, ,,  , a, n, d,  , p, r, i, c, e,  , h, i, s, t, o, r, i, e, s. Keep examples focused on dataset quality rather than generic advice.

Include practical exercises that require the learner to:

1. Benchmark 3 parsers.
2. Stream one 50MB page set.
3. Fix one encoding mess.
4. Strip boilerplate measurably.
5. Parallelize one job.
6. Lock golden fixtures.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from formats, schemas, dedupe, quality, and retention where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize data-engineering literature, format specs (Parquet/JSONL/CSV), SQLite docs, and data-quality frameworks. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **benched-3 checklist**, a **streamed-big checklist**, a **encoded-clean checklist**, a **boilerplate-gone checklist**, a **fixtures-locked checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
