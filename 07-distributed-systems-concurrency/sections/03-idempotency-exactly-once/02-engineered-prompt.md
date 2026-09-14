# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 07 Distributed Systems & Concurrency → Section: Idempotency and Exactly-Once Effects

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Idempotency and Exactly-Once Effects”** as part of an advanced course in distributed systems, concurrency, and reliable data-pipeline operations. How idempotency keys, dedupe ledgers, conditional writes, and transactional outboxes turn at-least-once delivery into exactly-once effects for scraping pipelines.

The material should teach how to design idempotent jobs with exactly-once effects. Go beyond surface-level tips and examine distributed pipeline engineering as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong pipeline reliability balances **throughput, correctness, resilience, observability, and cost**. Show how these principles apply differently to single-worker scripts, multi-worker fleets, and scheduled platforms. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to derive stable idempotency keys from URLs, extractions, and versions

Teach how to keep dedupe ledgers that survive restarts and scale reads

Teach how to write conditionally so replays converge instead of duplicating

Teach how to use transactional outboxes for side effects like notifications

Teach how to prove exactly-once with kill tests and reconciliation counts

Include practical methods for real projects. Cover:

* Key derivation
* Ledger design
* Conditional writes
* Outbox pattern
* Replay testing
* Reconciliation
* TTL policies
* Version discipline

Explain how practitioners can avoid keys unstable across runs (volatile fields in derivation).
Explain how practitioners can avoid ledger grows forever (no ttl or retention).
Explain how practitioners can avoid check-then-write races (non-atomic gate).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover c, r, a, w, l,  , q, u, e, u, e, s, ,,  , A, P, I,  , h, a, r, v, e, s, t, e, r, s, ,,  , m, e, d, i, a,  , p, i, p, e, l, i, n, e, s, ,,  , f, e, e, d,  , a, g, g, r, e, g, a, t, o, r, s, ,,  , a, n, d,  , m, o, n, i, t, o, r, i, n, g,  , f, l, e, e, t, s. Keep examples focused on pipeline reliability rather than generic advice.

Include practical exercises that require the learner to:

1. Derive keys for one pipeline.
2. Build one dedupe ledger.
3. Convert writes to conditional.
4. Add one outbox.
5. Kill-test one pipeline.
6. Reconcile one full run.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from queues, idempotency, backpressure, coordination, and resilience where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize distributed-systems literature, queue docs (Celery/RQ/BullMQ), SRE workbook, and Python concurrency docs. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **keys-stable checklist**, a **ledger-live checklist**, a **writes-conditional checklist**, a **outbox-once checklist**, a **proof-filed checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
