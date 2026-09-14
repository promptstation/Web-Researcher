# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 07 Distributed Systems & Concurrency → Section: Queues and Task Distribution

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Queues and Task Distribution”** as part of an advanced course in distributed systems, concurrency, and reliable data-pipeline operations. How durable queues with leases, acknowledgments, priorities, and dead-letter paths distribute scraping work, how to choose backends by scale, and how to operate them without losing or duplicating jobs.

The material should teach how to distribute scraping work over durable queues. Go beyond surface-level tips and examine distributed pipeline engineering as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong pipeline reliability balances **throughput, correctness, resilience, observability, and cost**. Show how these principles apply differently to single-worker scripts, multi-worker fleets, and scheduled platforms. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to model jobs with identity, payload, priority, and retry budgets

Teach how to choose file, SQLite, Redis, or RabbitMQ backends by scale and team

Teach how to lease with timeouts, heartbeats, and safe redelivery

Teach how to prioritize urgent, fresh, and bulk work without starvation

Teach how to dead-letter poison jobs with review loops and requeue paths

Include practical methods for real projects. Cover:

* Job modeling
* Backend ladder
* Lease design
* Ack discipline
* Priority bands
* Dead-letter review
* Depth alerting
* Drain procedures

Explain how practitioners can avoid jobs processed twice (ack before write or short leases).
Explain how practitioners can avoid jobs stuck invisible (dead worker holding lease).
Explain how practitioners can avoid dlq floods (target change or bug in handler).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover c, r, a, w, l,  , q, u, e, u, e, s, ,,  , A, P, I,  , h, a, r, v, e, s, t, e, r, s, ,,  , m, e, d, i, a,  , p, i, p, e, l, i, n, e, s, ,,  , f, e, e, d,  , a, g, g, r, e, g, a, t, o, r, s, ,,  , a, n, d,  , m, o, n, i, t, o, r, i, n, g,  , f, l, e, e, t, s. Keep examples focused on pipeline reliability rather than generic advice.

Include practical exercises that require the learner to:

1. Model jobs for one pipeline.
2. Pick a backend with reasons.
3. Implement leases with redelivery.
4. Prove priority fairness.
5. Review one dead-letter batch.
6. Drain one queue cleanly.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from queues, idempotency, backpressure, coordination, and resilience where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize distributed-systems literature, queue docs (Celery/RQ/BullMQ), SRE workbook, and Python concurrency docs. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **jobs-modeled checklist**, a **backend-fit checklist**, a **leases-safe checklist**, a **fair-proven checklist**, a **dlq-reviewed checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
