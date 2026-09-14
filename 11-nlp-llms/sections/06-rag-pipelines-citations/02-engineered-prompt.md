# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 11 Natural Language Processing (NLP) & LLMs → Section: RAG Pipelines with Citations

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“RAG Pipelines with Citations”** as part of an advanced course in natural language processing, LLMs, and text pipelines. How retrieve-rerank-generate pipelines with grounded citations, abstention, freshness filters, and faithfulness eval answer from your corpus honestly.

The material should teach how to build trustworthy RAG pipelines. Go beyond surface-level tips and examine language engineering as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong text quality balances **accuracy, cost, latency, safety, and provenance**. Show how these principles apply differently to sample texts, labeled corpora, and production language pipelines. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to retrieve (dense + filters) and rerank for answer-grade contexts

Teach how to generate with inline citations bound to retrieved chunks

Teach how to abstain when context lacks the answer

Teach how to filter by freshness, source, and permissions

Teach how to evaluate faithfulness, recall, and citation precision

Include practical methods for real projects. Cover:

* Hybrid retrieval
* Reranking
* Citation binding
* Abstention tuning
* Permission filtering
* Freshness filters
* Faithfulness eval
* Failure taxonomy

Explain how practitioners can avoid cites wrong chunks (rerank weak or k too big).
Explain how practitioners can avoid over-abstains (threshold too strict).
Explain how practitioners can avoid slow answers (retrieve+rereank+generate chain).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover r, e, v, i, e, w, s, ,,  , a, r, t, i, c, l, e, s, ,,  , l, i, s, t, i, n, g, s, ,,  , t, i, c, k, e, t, s, ,,  , a, n, d,  , t, r, a, n, s, c, r, i, p, t, s. Keep examples focused on text quality rather than generic advice.

Include practical exercises that require the learner to:

1. Retrieve+rereank 50 queries.
2. Cite 20 answers.
3. Tune abstention.
4. Filter one corpus.
5. Eval faithfulness.
6. Fix top failure class.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from cleaning, chunking, extraction, RAG, and eval where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize NLP literature, LLM provider docs, RAG references, and eval frameworks. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **reranked-50 checklist**, a **cited-20 checklist**, a **abstains-right checklist**, a **filtered-1 checklist**, a **faithful-ok checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
