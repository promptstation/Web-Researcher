# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 07 Distributed Systems & Concurrency → Section: Coordination: Locks, Leaders and Schedulers

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Coordination: Locks, Leaders and Schedulers”** as part of an advanced course in distributed systems, concurrency, and reliable data-pipeline operations. How distributed locks with fencing, leader election for schedulers, and exactly-once scheduling prevent duplicate crawls and conflicting writes across worker fleets.

The material should teach how to coordinate distributed workers safely. Go beyond surface-level tips and examine distributed pipeline engineering as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong pipeline reliability balances **throughput, correctness, resilience, observability, and cost**. Show how these principles apply differently to single-worker scripts, multi-worker fleets, and scheduled platforms. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to lock across processes and hosts with leases and fencing tokens

Teach how to elect one scheduler leader with safe failover

Teach how to schedule crawls exactly once across restarts and failovers

Teach how to shard work deterministically so ownership never overlaps

Teach how to avoid split-brain with quorums, TTLs, and fail-closed defaults

Include practical methods for real projects. Cover:

* Lease locks
* Fencing tokens
* Leader election
* Schedule ledger
* Consistent sharding
* Fail-closed design
* Failover drills
* Clock-safety

Explain how practitioners can avoid lock expires mid-work (ttl under work time).
Explain how practitioners can avoid two leaders briefly (slow failover detection).
Explain how practitioners can avoid clock skew breaks ttls (ntp drift across hosts).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover c, r, a, w, l,  , q, u, e, u, e, s, ,,  , A, P, I,  , h, a, r, v, e, s, t, e, r, s, ,,  , m, e, d, i, a,  , p, i, p, e, l, i, n, e, s, ,,  , f, e, e, d,  , a, g, g, r, e, g, a, t, o, r, s, ,,  , a, n, d,  , m, o, n, i, t, o, r, i, n, g,  , f, l, e, e, t, s. Keep examples focused on pipeline reliability rather than generic advice.

Include practical exercises that require the learner to:

1. Lock one critical section across hosts.
2. Elect a leader with failover.
3. Schedule one crawl exactly once.
4. Shard one fleet deterministically.
5. Drill one failover.
6. Prove no split-brain.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from queues, idempotency, backpressure, coordination, and resilience where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize distributed-systems literature, queue docs (Celery/RQ/BullMQ), SRE workbook, and Python concurrency docs. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **locked-fenced checklist**, a **leader-single checklist**, a **scheduled-once checklist**, a **shards-clean checklist**, a **failover-drilled checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
