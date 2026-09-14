# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 06 Automated Browsers → Section: Resilient Production Pipelines

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Resilient Production Pipelines”** as part of an advanced course in automated browsers, Playwright and Puppeteer operations, and production scraping. Production scraping architecture with automated browsers: job queues and idempotent jobs, per-domain throttling and concurrency limits, exponential-backoff retries with jitter, proxy rotation and sticky sessions, CAPTCHA/challenge triage and graceful degradation, structured logging and tracing, metrics and alerting, result validation and deduping, and checkpointing so failed runs resume without data loss.

The material should teach how to design and operate resilient scraping pipelines that throttle politely, retry intelligently, and observe everything. Go beyond surface-level tips and examine browser automation operations as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong automation reliability balances **reliability, speed, politeness, observability, and maintainability**. Show how these principles apply differently to first scripts, suite automation, and fleet operations. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to design idempotent queued jobs with per-domain throttling and concurrency limits, modeling job identity, state machines, leases, and dead-letter paths

Teach how to implement exponential-backoff retries with full jitter, circuit breakers, and graceful degradation that protects targets and budgets

Teach how to rotate proxies with sticky sessions for logins, per-domain isolation, and automatic quarantine of failing egress

Teach how to triage CAPTCHAs and challenges with detection, backoff, parking, and lawful human-in-the-loop review

Teach how to build observability with structured logs, traces, metrics, validation, and deduping that make failures cheap

Include practical methods for real projects. Cover:

* Job modeling and idempotency keys
* Queue design with dead-letter paths
* Per-domain throttles and concurrency caps
* Backoff with jitter and circuit breakers
* Proxy pools with sticky sessions
* Challenge detection and triage
* Checkpointing and resume
* Schema validation and deduping
* Structured logging and metrics
* Alerting and runbooks

Explain how practitioners can avoid retry storm (no jitter or breaker).
Explain how practitioners can avoid duplicates after resume (done marked before write).
Explain how practitioners can avoid challenge flood (too fast or burned egress).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover s, t, o, r, e, f, r, o, n, t, s, ,,  , n, e, w, s,  , s, i, t, e, s, ,,  , t, r, a, v, e, l,  , l, i, s, t, i, n, g, s, ,,  , j, o, b,  , b, o, a, r, d, s, ,,  , a, n, d,  , a, u, t, h, e, n, t, i, c, a, t, e, d,  , d, a, s, h, b, o, a, r, d, s. Keep examples focused on automation reliability rather than generic advice.

Include practical exercises that require the learner to:

1. Model idempotent jobs for a 50k-URL crawl with versions and priorities.
2. Implement per-domain throttling with a token bucket and concurrency cap.
3. Implement exponential backoff with full jitter and a circuit breaker.
4. Build a proxy pool with rotation, sticky sessions, and automatic quarantine.
5. Implement challenge detection and triage with backoff and human-review queue.
6. Add checkpointing and resume so a killed worker loses at most one lease window.
7. Add schema validation, stable record IDs, and cross-run deduping.
8. Add structured logs, traces, and metrics with correlation IDs.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from locators, waits, contexts, interception, and pipeline reliability where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize Playwright and Puppeteer official docs, WebDriver BiDi specs, testing best-practice guides, and SRE literature. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **pre-flight checklist**, a **throttle-and-retry checklist**, a **proxy-and-challenge checklist**, a **observability checklist**, a **data-quality-and-resume checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
