# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 07 Distributed Systems & Concurrency → Section: Retries, Deadlines and Circuit Breakers

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Retries, Deadlines and Circuit Breakers”** as part of an advanced course in distributed systems, concurrency, and reliable data-pipeline operations. How retry budgets, exponential backoff with jitter, deadlines, timeouts, hedged requests, and circuit breakers compose into clients that fail fast, recover automatically, and never amplify outages.

The material should teach how to compose client-side resilience that protects both sides. Go beyond surface-level tips and examine distributed pipeline engineering as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong pipeline reliability balances **throughput, correctness, resilience, observability, and cost**. Show how these principles apply differently to single-worker scripts, multi-worker fleets, and scheduled platforms. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to budget retries per operation so failures cost a known amount

Teach how to back off exponentially with full jitter and honor Retry-After

Teach how to set connect, read, and end-to-end deadlines that fail fast

Teach how to trip circuit breakers on error budgets with half-open probes

Teach how to hedge tail latency without doubling load blindly

Include practical methods for real projects. Cover:

* Retry budgets
* Jittered backoff
* Deadline layering
* Breaker tuning
* Half-open probing
* Hedging policy
* Error classification
* Recovery drills

Explain how practitioners can avoid breaker flaps (thresholds near noise floor).
Explain how practitioners can avoid deadlines too tight (p99 underestimated).
Explain how practitioners can avoid hedging doubles load (hedge too early or always).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover c, r, a, w, l,  , q, u, e, u, e, s, ,,  , A, P, I,  , h, a, r, v, e, s, t, e, r, s, ,,  , m, e, d, i, a,  , p, i, p, e, l, i, n, e, s, ,,  , f, e, e, d,  , a, g, g, r, e, g, a, t, o, r, s, ,,  , a, n, d,  , m, o, n, i, t, o, r, i, n, g,  , f, l, e, e, t, s. Keep examples focused on pipeline reliability rather than generic advice.

Include practical exercises that require the learner to:

1. Budget retries for one client.
2. Add jittered backoff everywhere.
3. Layer three deadlines.
4. Tune one breaker.
5. Drill one outage recovery.
6. Hedge one tail safely.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from queues, idempotency, backpressure, coordination, and resilience where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize distributed-systems literature, queue docs (Celery/RQ/BullMQ), SRE workbook, and Python concurrency docs. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **budget-set checklist**, a **jitter-live checklist**, a **deadlines-layered checklist**, a **breaker-tuned checklist**, a **drill-clean checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
