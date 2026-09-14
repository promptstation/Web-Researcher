# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 07 Distributed Systems & Concurrency → Section: Observability: Logs, Metrics and Traces

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Observability: Logs, Metrics and Traces”** as part of an advanced course in distributed systems, concurrency, and reliable data-pipeline operations. How structured JSON logs with correlation IDs, RED/USE metrics, distributed traces, and run reports make pipeline failures cheap to find, explain, and prevent.

The material should teach how to observe distributed pipelines completely. Go beyond surface-level tips and examine distributed pipeline engineering as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong pipeline reliability balances **throughput, correctness, resilience, observability, and cost**. Show how these principles apply differently to single-worker scripts, multi-worker fleets, and scheduled platforms. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to log structured JSON with run, job, and correlation IDs

Teach how to emit RED (rate, errors, duration) and USE (utilization, saturation, errors) metrics

Teach how to trace jobs across queues and workers with propagated context

Teach how to summarize every run automatically with counts, tails, and top errors

Teach how to alert on burn rates and SLOs instead of raw error noise

Include practical methods for real projects. Cover:

* JSON logging
* Correlation IDs
* RED/USE metrics
* Context propagation
* Run reports
* Burn-rate alerting
* Dashboard standards
* Postmortem loops

Explain how practitioners can avoid correlation gaps (ids dropped at boundaries).
Explain how practitioners can avoid metric cardinality explosion (high-card labels (url, id)).
Explain how practitioners can avoid reports ignored (too long or no owner).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover c, r, a, w, l,  , q, u, e, u, e, s, ,,  , A, P, I,  , h, a, r, v, e, s, t, e, r, s, ,,  , m, e, d, i, a,  , p, i, p, e, l, i, n, e, s, ,,  , f, e, e, d,  , a, g, g, r, e, g, a, t, o, r, s, ,,  , a, n, d,  , m, o, n, i, t, o, r, i, n, g,  , f, l, e, e, t, s. Keep examples focused on pipeline reliability rather than generic advice.

Include practical exercises that require the learner to:

1. Structure logs for one pipeline.
2. Emit RED for one service.
3. Trace one job end to end.
4. Auto-report one run.
5. Alert on one burn rate.
6. Postmortem one incident.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from queues, idempotency, backpressure, coordination, and resilience where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize distributed-systems literature, queue docs (Celery/RQ/BullMQ), SRE workbook, and Python concurrency docs. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **logs-json checklist**, a **red-live checklist**, a **trace-e2e checklist**, a **report-auto checklist**, a **alerts-signal checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
