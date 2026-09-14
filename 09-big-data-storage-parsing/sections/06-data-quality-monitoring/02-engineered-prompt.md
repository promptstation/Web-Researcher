# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 09 Big Data Storage & Parsing → Section: Data Quality Monitoring

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Data Quality Monitoring”** as part of an advanced course in big data storage, parsing, and dataset operations. How field-fill rates, type/range/enum checks, freshness lag, distribution drift, and golden-record tests combine into continuous data-quality monitoring with alerts.

The material should teach how to monitor scraped-data quality continuously. Go beyond surface-level tips and examine dataset engineering as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong dataset quality balances **volume, quality, freshness, cost, and retrievability**. Show how these principles apply differently to single-file scrapes, growing datasets, and archival corpora. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to track field-fill rates per field per source with alert bands

Teach how to check type, range, enum, and format validity continuously

Teach how to measure freshness lag against SLAs per dataset

Teach how to detect distribution drift in prices, categories, and volumes

Teach how to maintain golden records that catch silent breakage

Include practical methods for real projects. Cover:

* Fill tracking
* Validity suites
* Lag measurement
* Drift detection
* Golden records
* Anomaly bands
* Quality SLOs
* Breakage playbooks

Explain how practitioners can avoid alert storms (bands too tight).
Explain how practitioners can avoid goldens rot (real-world change).
Explain how practitioners can avoid lag hidden (averages mask tails).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover p, r, o, d, u, c, t,  , c, a, t, a, l, o, g, s, ,,  , n, e, w, s,  , a, r, c, h, i, v, e, s, ,,  , l, i, s, t, i, n, g,  , c, o, r, p, o, r, a, ,,  , d, o, c, u, m, e, n, t,  , c, o, l, l, e, c, t, i, o, n, s, ,,  , a, n, d,  , p, r, i, c, e,  , h, i, s, t, o, r, i, e, s. Keep examples focused on dataset quality rather than generic advice.

Include practical exercises that require the learner to:

1. Track fills for one feed.
2. Suite validity for one schema.
3. Measure lag for one SLA.
4. Detect one drift.
5. Lock 20 golden records.
6. Catch one silent break.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from formats, schemas, dedupe, quality, and retention where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize data-engineering literature, format specs (Parquet/JSONL/CSV), SQLite docs, and data-quality frameworks. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **fills-live checklist**, a **suite-green checklist**, a **lag-ok checklist**, a **drift-caught checklist**, a **golden-20 checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
