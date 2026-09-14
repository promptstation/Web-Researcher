# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 09 Big Data Storage & Parsing → Section: Document Parsing Operations

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Document Parsing Operations”** as part of an advanced course in big data storage, parsing, and dataset operations. How to triage, extract text and tables from PDFs and Office documents, handle scanned pages with OCR decisions, and preserve layout signals that matter.

The material should teach how to parse document collections operationally. Go beyond surface-level tips and examine dataset engineering as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong dataset quality balances **volume, quality, freshness, cost, and retrievability**. Show how these principles apply differently to single-file scrapes, growing datasets, and archival corpora. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to triage document sets by type, size, native-vs-scanned, and value

Teach how to extract native text with tools per format (pdf, docx, xlsx, pptx)

Teach how to decide OCR by value with cost and quality sampling

Teach how to recover tables with structure preservation

Teach how to preserve headings, lists, and reading order that downstream needs

Include practical methods for real projects. Cover:

* Corpus triage
* Tool selection
* Text extraction
* OCR sampling
* Table recovery
* Layout preservation
* Quality scoring
* Reprocess queues

Explain how practitioners can avoid text order scrambled (multi-column or absolute positioning).
Explain how practitioners can avoid ocr garbage (low dpi or skew).
Explain how practitioners can avoid tables merge/split (borderless or spanning cells).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover p, r, o, d, u, c, t,  , c, a, t, a, l, o, g, s, ,,  , n, e, w, s,  , a, r, c, h, i, v, e, s, ,,  , l, i, s, t, i, n, g,  , c, o, r, p, o, r, a, ,,  , d, o, c, u, m, e, n, t,  , c, o, l, l, e, c, t, i, o, n, s, ,,  , a, n, d,  , p, r, i, c, e,  , h, i, s, t, o, r, i, e, s. Keep examples focused on dataset quality rather than generic advice.

Include practical exercises that require the learner to:

1. Triage 100 documents.
2. Extract native text cleanly.
3. Sample OCR quality.
4. Recover 10 tables.
5. Preserve one complex layout.
6. Score one corpus.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from formats, schemas, dedupe, quality, and retention where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize data-engineering literature, format specs (Parquet/JSONL/CSV), SQLite docs, and data-quality frameworks. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **triaged-100 checklist**, a **native-clean checklist**, a **ocr-decided checklist**, a **tables-10 checklist**, a **scored-corpus checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
