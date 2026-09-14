# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 11 Natural Language Processing (NLP) & LLMs → Section: Text Cleaning and Normalization

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Text Cleaning and Normalization”** as part of an advanced course in natural language processing, LLMs, and text pipelines. How to clean scraped text with encoding repair, whitespace and boilerplate removal, dedupe, and language-aware normalization that preserves meaning.

The material should teach how to clean and normalize scraped text. Go beyond surface-level tips and examine language engineering as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong text quality balances **accuracy, cost, latency, safety, and provenance**. Show how these principles apply differently to sample texts, labeled corpora, and production language pipelines. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to repair mojibake and mixed encodings with detection and logging

Teach how to normalize whitespace, quotes, and dashes without flattening structure

Teach how to remove nav, cookie, and template boilerplate with block scoring

Teach how to dedupe repeated lines and syndicated copies

Teach how to verify cleaning preserves meaning with before/after sampling

Include practical methods for real projects. Cover:

* Encoding repair
* Unicode normalization
* Boilerplate scoring
* Line dedupe
* Structure preservation
* Before/after sampling
* Cleaning configs
* Regression fixtures

Explain how practitioners can avoid over-cleaning (aggressive rules eat content).
Explain how practitioners can avoid mixed languages mangled (one-size normalization).
Explain how practitioners can avoid cleaning drifts (unversioned ad-hoc fixes).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover r, e, v, i, e, w, s, ,,  , a, r, t, i, c, l, e, s, ,,  , l, i, s, t, i, n, g, s, ,,  , t, i, c, k, e, t, s, ,,  , a, n, d,  , t, r, a, n, s, c, r, i, p, t, s. Keep examples focused on text quality rather than generic advice.

Include practical exercises that require the learner to:

1. Repair one mojibake corpus.
2. Normalize 10k docs.
3. Strip boilerplate measurably.
4. Dedupe one feed.
5. Sample 100 before/after.
6. Lock fixtures.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from cleaning, chunking, extraction, RAG, and eval where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize NLP literature, LLM provider docs, RAG references, and eval frameworks. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **repaired-1 checklist**, a **normalized-10k checklist**, a **stripped-ok checklist**, a **deduped-1 checklist**, a **fixtures-locked checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
