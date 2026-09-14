# Course 07 — Distributed Systems & Concurrency
## Curriculum Content Outlook (Researching-Outline workflow, compressed to ≤15 sections)

Source course list: `Web researcher and scrapper.txt` — Course 7: Distributed Systems & Concurrency
Method: Researching-Outline.md workflow (Steps 1–8) + beginner→expert progression research + compression into groups.
Sections: 10 (within the ≤15 limit). Each section = Summary (what it teaches) + Absorbed Skill (capability gained).

---

**Concurrency Models and Selection**

**Summary:** How threads, asyncio, multiprocessing, and worker processes compare for IO-bound scraping, how to measure the GIL's real impact, and how to choose and combine models per workload with benchmarks.

**Absorbed Skill:** Select and combine concurrency models per workload using measured benchmarks.

---

**Queues and Task Distribution**

**Summary:** How durable queues with leases, acknowledgments, priorities, and dead-letter paths distribute scraping work, how to choose backends by scale, and how to operate them without losing or duplicating jobs.

**Absorbed Skill:** Distribute work over durable queues with leases, priorities, and dead-letter discipline.

---

**Idempotency and Exactly-Once Effects**

**Summary:** How idempotency keys, dedupe ledgers, conditional writes, and transactional outboxes turn at-least-once delivery into exactly-once effects for scraping pipelines.

**Absorbed Skill:** Deliver exactly-once effects with idempotency keys, ledgers, and conditional writes.

---

**Rate Limiting and Backpressure**

**Summary:** How token buckets, leaky buckets, fixed windows, and adaptive limiters shape traffic, how backpressure propagates through pipelines, and how to respect Retry-After and rate headers precisely.

**Absorbed Skill:** Shape traffic with precise limiters and propagate backpressure end to end.

---

**Retries, Deadlines and Circuit Breakers**

**Summary:** How retry budgets, exponential backoff with jitter, deadlines, timeouts, hedged requests, and circuit breakers compose into clients that fail fast, recover automatically, and never amplify outages.

**Absorbed Skill:** Compose retries, deadlines, and breakers into self-protecting clients.

---

**Coordination: Locks, Leaders and Schedulers**

**Summary:** How distributed locks with fencing, leader election for schedulers, and exactly-once scheduling prevent duplicate crawls and conflicting writes across worker fleets.

**Absorbed Skill:** Coordinate fleets with fenced locks, single leaders, and exactly-once schedules.

---

**Observability: Logs, Metrics and Traces**

**Summary:** How structured JSON logs with correlation IDs, RED/USE metrics, distributed traces, and run reports make pipeline failures cheap to find, explain, and prevent.

**Absorbed Skill:** Observe pipelines with correlated logs, metrics, traces, and run reports.

---

**Containers and Deployment for Workers**

**Summary:** How to containerize browser and API workers with pinned browsers, reproduce fleets with compose files, manage secrets and volumes, and roll out updates with canary verification.

**Absorbed Skill:** Containerize workers reproducibly and roll out updates with canary verification.

---

**Scheduling and Freshness at Scale**

**Summary:** How to schedule collections by freshness SLAs with cron discipline, priority aging, change detection, and catch-up policies that keep data fresh without redundant fetching.

**Absorbed Skill:** Schedule collections by freshness SLAs with aging priorities and catch-up discipline.

---

**Failure Drills and Chaos Practice**

**Summary:** How game days, failure injection, kill tests, partition drills, and load spikes prove pipelines recover automatically, with blameless postmortems that convert each drill into permanent hardening.

**Absorbed Skill:** Prove recovery with drills and convert every lesson into permanent hardening.
