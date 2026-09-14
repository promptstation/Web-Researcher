# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 09 Big Data Storage & Parsing → Section: Schema Design and Validation

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Schema Design and Validation”** as part of an advanced course in big data storage, parsing, and dataset operations. How to design record schemas with required fields, types, enums, and identities, how to validate every record at layer boundaries, and how to quarantine rejects with actionable reasons.

The material should teach how to design schemas and validation for scraped records. Go beyond surface-level tips and examine dataset engineering as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong dataset quality balances **volume, quality, freshness, cost, and retrievability**. Show how these principles apply differently to single-file scrapes, growing datasets, and archival corpora. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to design minimal complete schemas with identities and timestamps

Teach how to type fields strictly (money, dates, URLs, enums)

Teach how to validate at every layer boundary with fast failure

Teach how to quarantine rejects with codes owners can act on

Teach how to track validation rates as a quality signal

Include practical methods for real projects. Cover:

* Schema authoring
* Identity design
* Type discipline
* Boundary validation
* Reject taxonomy
* Quarantine review
* Rate dashboards
* Contract testing

Explain how practitioners can avoid validation too strict (optional reality marked required).
Explain how practitioners can avoid quarantine floods (source change or extractor bug).
Explain how practitioners can avoid identity collisions (weak key derivation).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover p, r, o, d, u, c, t,  , c, a, t, a, l, o, g, s, ,,  , n, e, w, s,  , a, r, c, h, i, v, e, s, ,,  , l, i, s, t, i, n, g,  , c, o, r, p, o, r, a, ,,  , d, o, c, u, m, e, n, t,  , c, o, l, l, e, c, t, i, o, n, s, ,,  , a, n, d,  , p, r, i, c, e,  , h, i, s, t, o, r, i, e, s. Keep examples focused on dataset quality rather than generic advice.

Include practical exercises that require the learner to:

1. Author one schema fully.
2. Validate 10k records.
3. Quarantine with codes.
4. Review one reject batch.
5. Dashboard one rate.
6. Contract-test one consumer.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from formats, schemas, dedupe, quality, and retention where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize data-engineering literature, format specs (Parquet/JSONL/CSV), SQLite docs, and data-quality frameworks. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **schema-v1 checklist**, a **validated-10k checklist**, a **quarantined-coded checklist**, a **reviewed-batch checklist**, a **rate-live checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
