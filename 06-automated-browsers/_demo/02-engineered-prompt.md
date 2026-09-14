# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Input: 01-reusable-prompt.md → Output: RESULT prompt below

The RESULT below is the engineered prompt. It follows the Prompt Engineering.md example RESULT pattern (Task + Instructions + Context fused into one production-ready prompt). In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Resilient Production Scraping Pipelines with Automated Browsers”** as part of an advanced course in web research, automated browsers, and production web scraping. The module should explain how to move from a single Playwright or Puppeteer script that works once on a laptop to a fleet of polite, observable, resumable scraping pipelines that run for months against real, defended, rate-limited websites.

The material should teach how to design scraping as a distributed system in which every URL is an idempotent job, every domain has a politeness budget, every failure is classified and retried with discipline, and every run leaves structured logs, traces, and metrics that make the next failure cheaper to fix. Go beyond basic “loop over URLs and save HTML” demos and examine scraping as an operations discipline where throughput, politeness, cost, data quality, and maintainability are traded off explicitly.

Explain how strong pipelines balance **throughput, politeness, resilience, data quality, observability, cost, and legal/ethical compliance**. Show how these principles apply differently to small research crawls, continuous price/news monitoring, and large-scale multi-domain collections. Discuss how queues, throttles, retries, proxies, browser contexts, checkpoints, validators, and dedupers should be composed as one coherent pipeline rather than as disconnected tricks copied from blog posts.

Explore the relationship between browser automation and **pipeline architecture at scale**. Explain how teams can run hundreds of concurrent browser contexts without collapsing targets or workers, how to isolate domains, accounts, and geographies, and how to degrade gracefully when a site introduces a new challenge, layout change, or rate limit. Demonstrate how disciplined backoff and queue design preserve both the target and the operator’s proxy and compute budget while keeping data freshness commitments.

Teach the principles of designing **idempotent queued jobs with per-domain throttling and concurrency limits**. Explain how job identity should be derived from canonical URL plus extraction version plus parameters, rather than invented arbitrarily. Show how to distinguish retriable failures (timeouts, 429, 503, navigation resets, challenge pages) from terminal failures (404, permanent blocks, schema-breaking layout changes). Explain how per-domain token buckets, concurrent-context caps, crawl-delay awareness, and queue priorities interact, and how job state (queued, leased, succeeded, failed, dead-lettered) should be modeled for resume and audit. Provide a practical framework for choosing queue backends (Celery/Redis/RabbitMQ, BullMQ, RQ, PostgreSQL-backed queues) based on scale, team skill, and operational burden.

Teach how to implement **exponential-backoff retries with jitter and graceful degradation on blocks**. Explain what a retry policy should accomplish, what it should not attempt to accomplish, and how retry decisions affect target load, proxy burn, data freshness, and cost. Include a practical framework for setting base delay, multiplier, max delay, max attempts, jitter strategy (full vs equal vs decorrelated), circuit-breaker thresholds, and cooldowns per domain. Explain how retries should remain subordinate to politeness and how to degrade by reducing concurrency, switching to API capture or cached data, or parking a domain instead of hammering it.

Teach how to **rotate proxies with sticky sessions for login flows and per-domain isolation**. Explain when a job should or should not rotate IP, user-agent, and egress geography. Examine the advantages, risks, cost implications, and compliance implications of datacenter vs residential vs mobile proxies, sticky vs rotating sessions, and per-account vs per-domain pools. Provide a decision-making framework that allows an engineer to justify proxy choices based on target sensitivity, login requirements, ban history, budget, and data-quality needs rather than personal preference. Show how to detect proxy failure (elevated 403 rates, CAPTCHA spikes, latency shifts) and quarantine bad egress automatically.

Teach **challenge triage** and demonstrate how CAPTCHAs, Cloudflare Turnstile, DataDome, PerimeterX, and generic rate-limit pages should be detected, classified, logged, and handled without data loss. Explain how the same underlying block may need different responses depending on frequency, account impact, legal risk, and business priority. Show how automated handling (backoff, context recycle, proxy rotation, API fallback) can be combined with human-in-the-loop queues for manual solves where permitted, without normalizing aggressive evasion or Terms-of-Service violations. Emphasize preferring official APIs, reducing scope, and stopping when continued collection is inappropriate.

Teach how to maintain **data quality across retries and re-crawls**. Explain the difference between re-fetching a page and re-emitting a record. Show how to validate extracted records with schemas, checksums, and freshness timestamps, how to dedupe by stable record IDs across runs, and how to handle partial page renders, truncated lists, and infinite-scroll gaps. Include examples of validation failures, silent schema drift, duplicate emission after resume, and inappropriate “success” signals that hide missing fields.

Teach how to build **observability that makes failures cheap: structured logs, traces, metrics, and artifacts**. Explain how pipeline events should be organized by job, domain, worker, proxy pool, browser context, and extraction version. Show how to distinguish between signals that must be alerted (success-rate collapse, challenge-rate spike, queue growth, cost spike) and signals that can be sampled or aggregated. Explain how controlled verbosity can be introduced through log levels, trace sampling, screenshot-on-failure, HAR-on-failure, and video-on-flake while preserving debuggability without drowning storage or leaking PII. Cover correlation IDs from queue to browser to record.

Include practical methods for developing and governing production scraping operations. Cover:

* Job modeling and idempotency keys
* Queue design, priorities, delays, and dead-letter queues
* Per-domain throttles, concurrency caps, and crawl-delay handling
* Retry taxonomies, backoff with jitter, and circuit breakers
* Proxy pools, rotation policies, sticky sessions, and egress health checks
* Browser context lifecycle, reuse vs recycle, and memory/CPU guards
* Challenge detection, classification, and triage runbooks
* Checkpointing, resume, and exactly-once-emission patterns
* Schema validation, record IDs, checksums, and deduping
* Structured logging, OpenTelemetry traces, and Prometheus-style metrics
* Screenshot/HAR/video artifacts on failure with retention policies
* Alerting thresholds, dashboards, and on-call runbooks
* Cost tracking per 1k pages by domain, proxy type, and compute
* Browser-version pinning, dependency hygiene, and change detection
* Politeness budgets, robots.txt awareness, and Terms-of-Service review
* PII minimization, retention limits, and access controls
* Load testing against staging mirrors and dark launches
* Incident reviews and pipeline tuning loops

Explain how engineers can avoid common failure modes such as retry storms that get entire subnets banned, unbounded concurrency that OOMs workers, rotating away sticky login sessions mid-flow, treating a CAPTCHA page as a successful scrape, silent field loss after a layout change, duplicate records after resume, storing PII in logs and screenshots, alert fatigue from noisy thresholds, and “it worked on my laptop” pipelines with no checkpoints or metrics.

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover e-commerce price and availability monitoring, news/article collection, travel/hospitality listings, public-procurement portals, job boards, real-estate listings, and authenticated B2B dashboards where appropriate. Keep examples focused on pipeline behavior and browser control rather than merely demonstrating generic Python or JavaScript.

Include practical exercises that require the learner to:

1. Model idempotent jobs for a 50k-URL crawl with versions and priorities.
2. Implement per-domain throttling with a token bucket and concurrency cap.
3. Implement exponential backoff with full jitter and a circuit breaker.
4. Build a proxy pool with rotation, sticky sessions, and automatic quarantine.
5. Implement challenge detection and triage with backoff and human-review queue.
6. Add checkpointing and resume so a killed worker loses no more than one lease window.
7. Add schema validation, stable record IDs, and cross-run deduping.
8. Add structured logs, traces, and metrics with correlation IDs.
9. Capture screenshot plus HAR on failure with PII redaction and retention rules.
10. Build a miniature pipeline with queue + workers + dashboard that survives a simulated ban wave and layout change.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with single-script reliability (timeouts, waits, cleanup) and moving toward fleet operations (queues, workers, proxies, observability, incident response). Establish clear conceptual distinctions between **retries, backoff, throttling, concurrency control, circuit breaking, checkpointing, validation, deduplication, and observability** before showing how they interact.

Use professional terminology from browser automation, distributed systems, reliability engineering, and data engineering where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize authoritative sources such as Playwright and Puppeteer official documentation, WebDriver/BiDi specifications, SRE and distributed-systems literature, queue and stream-processing documentation (Celery, BullMQ, RabbitMQ, Redis), OpenTelemetry and Prometheus documentation, and reputable engineering blogs with production incident detail. Avoid relying primarily on low-quality SEO articles, generic scraping blogs, content farms, or unsupported “best practice” claims. Where useful, distinguish established reliability findings from professional conventions, operational heuristics, and informed recommendations.

Pay particular attention to the relationship between pipeline design and principles such as **idempotency, backpressure, least-privilege egress, graceful degradation, observability, queueing theory, caching, and politeness-first crawling**. Connect these concepts to concrete engineering decisions rather than discussing them only theoretically.

Create a professional framework that a scraping engineer or data-platform team could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Throughout the module, prioritize pipelines that are:

* Polite without being glacial
* Fast without being abusive
* Resilient without retry-storming
* Observable without leaking PII
* Resumable without duplicating records
* Stealthy without violating Terms of Service
* Scalable without becoming unmaintainable
* Cost-aware without sacrificing freshness
* Strict about schemas without being brittle
* Automated without hiding the need for human judgment

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **pre-flight checklist**, a **throttle-and-retry checklist**, a **proxy-and-challenge checklist**, an **observability checklist**, and a **data-quality-and-resume checklist** that can be used by a professional team before a pipeline is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical scraping work.
