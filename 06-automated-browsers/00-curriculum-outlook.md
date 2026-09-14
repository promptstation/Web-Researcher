# Course 06 — Automated Browsers
## Curriculum Content Outlook (Researching-Outline workflow, compressed to ≤15 sections)

Source course list: `Web researcher and scrapper.txt` — Course 6: Automated Browsers
Method: Researching-Outline.md workflow (Steps 1–8) + beginner→expert progression research + compression into groups.
Sections: 10 (within the ≤15 limit). Each section = Summary (what it teaches) + Absorbed Skill (capability gained).

---

**Foundations and Tooling Setup**

**Summary:** How to install and verify Playwright, Puppeteer, and Selenium with managed browsers, how headed and headless modes differ operationally, and how to write first scripts with correct launch, cleanup, and artifact habits.

**Absorbed Skill:** Install and verify automation stacks and write first scripts with correct lifecycle and artifacts.

---

**Reliable Locators and Element Strategy**

**Summary:** How to choose role, text, label, and test-id locators over brittle CSS and XPath, how to audit pages for locator health, and how to build selector standards that survive redesigns.

**Absorbed Skill:** Design resilient locator strategies and audit pages for selector health with measurable coverage.

---

**Waiting and Synchronization**

**Summary:** How auto-waiting, assertion retries, load states, and response waits compose into flake-free synchronization, how to classify flakes by cause, and how to eliminate sleeps systematically.

**Absorbed Skill:** Synchronize automation with layered waits and eliminate flakes by classified cause.

---

**Interaction Patterns at Scale**

**Summary:** How to automate forms, uploads, downloads, frames, tabs, dialogs, and drag-and-drop reliably, with verification after every action and patterns that scale across suites.

**Absorbed Skill:** Automate complex interactions with per-action verification and reusable patterns.

---

**Sessions, Auth and State Reuse**

**Summary:** How to authenticate once and reuse state across runs with storage snapshots, how to isolate accounts, refresh tokens, and handle secrets without leaks.

**Absorbed Skill:** Run login-once pipelines with isolated, refreshed, secret-safe session state.

---

**Network Control from Browsers**

**Summary:** How to observe, block, mock, and capture browser traffic with route handlers, how to extract APIs from HARs, and how to combine DOM and API channels for robust data collection.

**Absorbed Skill:** Control browser traffic with routes and mocks and extract APIs from captured flows.

---

**Context Hardening and Consistency**

**Summary:** How to configure browser contexts with coherent identity (locale, timezone, viewport, user agent), how to audit configurations for consistency, and how to test automation against your own staging honestly.

**Absorbed Skill:** Configure coherent browser contexts and audit them for consistency in legitimate testing.

---

**Resilient Production Pipelines**

**Summary:** Production scraping architecture with automated browsers: job queues and idempotent jobs, per-domain throttling and concurrency limits, exponential-backoff retries with jitter, proxy rotation and sticky sessions, CAPTCHA/challenge triage and graceful degradation, structured logging and tracing, metrics and alerting, result validation and deduping, and checkpointing so failed runs resume without data loss.

**Absorbed Skill:** Design and operate resilient scraping pipelines that throttle politely, retry intelligently, rotate proxies, triage blocks and CAPTCHAs without data loss, validate and dedupe results, and expose logs, traces, and metrics for debugging and monitoring.

---

**Scaling with Contexts and Queues**

**Summary:** How to scale browser fleets with isolated contexts, worker pools, distributed queues, resource guards, and backpressure, without collapsing targets, proxies, or hosts.

**Absorbed Skill:** Scale browser fleets with isolated contexts, queues, and guards that protect every layer.

---

**Frameworks, CI and Maintenance**

**Summary:** How to structure automation frameworks with fixtures and page objects, run them in CI with sharding and artifacts, and maintain them for years with ownership, docs, and deprecation discipline.

**Absorbed Skill:** Build maintainable automation frameworks with CI integration and long-term ownership.
