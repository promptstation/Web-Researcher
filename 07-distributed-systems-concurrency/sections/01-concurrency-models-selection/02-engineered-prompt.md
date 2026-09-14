# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 07 Distributed Systems & Concurrency → Section: Concurrency Models and Selection

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Concurrency Models and Selection”** as part of an advanced course in distributed systems, concurrency, and reliable data-pipeline operations. How threads, asyncio, multiprocessing, and worker processes compare for IO-bound scraping, how to measure the GIL's real impact, and how to choose and combine models per workload with benchmarks.

The material should teach how to select concurrency models from measurements. Go beyond surface-level tips and examine distributed pipeline engineering as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong pipeline reliability balances **throughput, correctness, resilience, observability, and cost**. Show how these principles apply differently to single-worker scripts, multi-worker fleets, and scheduled platforms. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to compare threads, asyncio, and multiprocessing for IO-bound collection

Teach how to measure GIL impact so choices rest on data not folklore

Teach how to benchmark each workload with realistic targets and payloads

Teach how to combine models (async IO plus process pools) with clean boundaries

Teach how to avoid shared-state races with queues and immutable handoffs

Include practical methods for real projects. Cover:

* Model comparison
* GIL measurement
* Workload benchmarks
* Hybrid design
* Race prevention
* Pool sizing
* Shutdown discipline
* Perf regression checks

Explain how practitioners can avoid async slower than threads (blocking calls inside the loop).
Explain how practitioners can avoid more workers, same speed (ceiling elsewhere or lock contention).
Explain how practitioners can avoid shutdown hangs (dangling tasks or unjoined pools).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover c, r, a, w, l,  , q, u, e, u, e, s, ,,  , A, P, I,  , h, a, r, v, e, s, t, e, r, s, ,,  , m, e, d, i, a,  , p, i, p, e, l, i, n, e, s, ,,  , f, e, e, d,  , a, g, g, r, e, g, a, t, o, r, s, ,,  , a, n, d,  , m, o, n, i, t, o, r, i, n, g,  , f, l, e, e, t, s. Keep examples focused on pipeline reliability rather than generic advice.

Include practical exercises that require the learner to:

1. Benchmark one workload three ways.
2. Measure GIL impact on your parser.
3. Size one pool from data.
4. Build one hybrid async-plus-pool worker.
5. Fix one shared-state race.
6. Regression-check one change.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from queues, idempotency, backpressure, coordination, and resilience where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize distributed-systems literature, queue docs (Celery/RQ/BullMQ), SRE workbook, and Python concurrency docs. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **bench-three checklist**, a **gil-measured checklist**, a **pool-sized checklist**, a **hybrid-clean checklist**, a **race-free checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
