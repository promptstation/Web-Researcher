# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 06 Automated Browsers → Section: Scaling with Contexts and Queues

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Scaling with Contexts and Queues”** as part of an advanced course in automated browsers, Playwright and Puppeteer operations, and production scraping. How to scale browser fleets with isolated contexts, worker pools, distributed queues, resource guards, and backpressure, without collapsing targets, proxies, or hosts.

The material should teach how to scale browser automation from one worker to sharded fleets safely. Go beyond surface-level tips and examine browser automation operations as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong automation reliability balances **reliability, speed, politeness, observability, and maintainability**. Show how these principles apply differently to first scripts, suite automation, and fleet operations. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to size contexts and browsers per host from measured memory footprints

Teach how to design worker pools over queues with leases and acknowledgments

Teach how to enforce CPU, memory, and file-handle guards with graceful shedding

Teach how to apply backpressure from targets, queues, and workers without deadlock

Teach how to shard by domain and scale horizontally with independent throttles

Include practical methods for real projects. Cover:

* Memory-based sizing
* Queue selection
* Lease design
* Guard thresholds
* Backpressure signals
* Shard planning
* Autoscale rules
* Load testing

Explain how practitioners can avoid throughput flat as workers rise (ceiling elsewhere: target, egress, queue).
Explain how practitioners can avoid queue grows unbounded (producers outpace guarded workers).
Explain how practitioners can avoid noisy-neighbor shards (shared throttles or hosts).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover s, t, o, r, e, f, r, o, n, t, s, ,,  , n, e, w, s,  , s, i, t, e, s, ,,  , t, r, a, v, e, l,  , l, i, s, t, i, n, g, s, ,,  , j, o, b,  , b, o, a, r, d, s, ,,  , a, n, d,  , a, u, t, h, e, n, t, i, c, a, t, e, d,  , d, a, s, h, b, o, a, r, d, s. Keep examples focused on automation reliability rather than generic advice.

Include practical exercises that require the learner to:

1. Size one host from measurements.
2. Build a queued worker pool.
3. Enforce guards under load.
4. Demonstrate backpressure working.
5. Shard one fleet by domain.
6. Load-test to the knee.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from locators, waits, contexts, interception, and pipeline reliability where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize Playwright and Puppeteer official docs, WebDriver BiDi specs, testing best-practice guides, and SRE literature. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **size-math checklist**, a **queue-live checklist**, a **guards-armed checklist**, a **pressure-proof checklist**, a **scale-tested checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
