# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 07 Distributed Systems & Concurrency → Section: Failure Drills and Chaos Practice

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Failure Drills and Chaos Practice”** as part of an advanced course in distributed systems, concurrency, and reliable data-pipeline operations. How game days, failure injection, kill tests, partition drills, and load spikes prove pipelines recover automatically, with blameless postmortems that convert each drill into permanent hardening.

The material should teach how to prove distributed recovery with disciplined drills. Go beyond surface-level tips and examine distributed pipeline engineering as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong pipeline reliability balances **throughput, correctness, resilience, observability, and cost**. Show how these principles apply differently to single-worker scripts, multi-worker fleets, and scheduled platforms. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to plan game days with hypotheses, blast radius, and abort criteria

Teach how to inject latency, errors, kills, and partitions with guardrails

Teach how to kill-test workers and prove zero loss with bounded duplicates

Teach how to drill network partitions and leader failovers safely

Teach how to run blameless postmortems that produce dated hardening actions

Include practical methods for real projects. Cover:

* Game-day planning
* Blast-radius control
* Injection tooling
* Kill testing
* Partition drills
* Abort criteria
* Blameless postmortems
* Hardening backlogs

Explain how practitioners can avoid drill finds nothing (too gentle or wrong layer).
Explain how practitioners can avoid abort triggered (blast radius breached).
Explain how practitioners can avoid lessons rot (actions unowned or undated).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover c, r, a, w, l,  , q, u, e, u, e, s, ,,  , A, P, I,  , h, a, r, v, e, s, t, e, r, s, ,,  , m, e, d, i, a,  , p, i, p, e, l, i, n, e, s, ,,  , f, e, e, d,  , a, g, g, r, e, g, a, t, o, r, s, ,,  , a, n, d,  , m, o, n, i, t, o, r, i, n, g,  , f, l, e, e, t, s. Keep examples focused on pipeline reliability rather than generic advice.

Include practical exercises that require the learner to:

1. Plan one game day.
2. Inject latency into staging.
3. Kill-test one pipeline.
4. Drill one partition.
5. Postmortem one drill.
6. Ship three hardenings.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from queues, idempotency, backpressure, coordination, and resilience where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize distributed-systems literature, queue docs (Celery/RQ/BullMQ), SRE workbook, and Python concurrency docs. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **day-planned checklist**, a **injected-safe checklist**, a **kill-clean checklist**, a **partition-ok checklist**, a **actions-shipped checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
