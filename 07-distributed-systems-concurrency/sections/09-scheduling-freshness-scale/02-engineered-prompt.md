# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 07 Distributed Systems & Concurrency → Section: Scheduling and Freshness at Scale

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Scheduling and Freshness at Scale”** as part of an advanced course in distributed systems, concurrency, and reliable data-pipeline operations. How to schedule collections by freshness SLAs with cron discipline, priority aging, change detection, and catch-up policies that keep data fresh without redundant fetching.

The material should teach how to schedule data collection by freshness need. Go beyond surface-level tips and examine distributed pipeline engineering as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong pipeline reliability balances **throughput, correctness, resilience, observability, and cost**. Show how these principles apply differently to single-worker scripts, multi-worker fleets, and scheduled platforms. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to define freshness SLAs per dataset from real consumer need

Teach how to schedule with validated cron, timezones, and exactly-once slots

Teach how to age priorities so stale items surface without starving fresh ones

Teach how to detect changes with etags, hashes, and sitemaps before full fetches

Teach how to catch up after outages with bounded backfill and SLA triage

Include practical methods for real projects. Cover:

* SLA definition
* Cron validation
* Aging functions
* Change detection
* Sitemap scheduling
* Backfill policy
* Lag dashboards
* SLA reviews

Explain how practitioners can avoid cron drift (timezone or dst confusion).
Explain how practitioners can avoid aging starves fresh (stale backlog dominates).
Explain how practitioners can avoid change checks lie (weak etags or dynamic noise).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover c, r, a, w, l,  , q, u, e, u, e, s, ,,  , A, P, I,  , h, a, r, v, e, s, t, e, r, s, ,,  , m, e, d, i, a,  , p, i, p, e, l, i, n, e, s, ,,  , f, e, e, d,  , a, g, g, r, e, g, a, t, o, r, s, ,,  , a, n, d,  , m, o, n, i, t, o, r, i, n, g,  , f, l, e, e, t, s. Keep examples focused on pipeline reliability rather than generic advice.

Include practical exercises that require the learner to:

1. Define SLAs for three datasets.
2. Validate five cron specs.
3. Implement one aging function.
4. Add change detection to one feed.
5. Backfill after one simulated outage.
6. Dashboard lag for one fleet.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from queues, idempotency, backpressure, coordination, and resilience where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize distributed-systems literature, queue docs (Celery/RQ/BullMQ), SRE workbook, and Python concurrency docs. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **slas-set checklist**, a **cron-valid checklist**, a **aging-live checklist**, a **changed-cheap checklist**, a **backfill-bounded checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
