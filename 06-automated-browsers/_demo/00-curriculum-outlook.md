# Course 06 — Automated Browsers
## Curriculum Content Outlook (Researching-Outline workflow, compressed to ≤15 sections)

Source course list: `Web researcher and scrapper.txt` — Course 6: Automated Browsers
Method: Researching-Outline.md workflow (Steps 1–8) + beginner→expert progression research + compression into groups.
Sections: 12 (within the ≤15 limit). Each section = Summary (what it teaches) + Absorbed Skill (capability gained).

---

**Browser Internals for Automation**

**Summary:** How modern browsers render and run the web for automation purposes: Chromium/Firefox/WebKit differences, DOM and CSSOM, JavaScript event loop, navigation lifecycle, HTTP(S) requests, cookies, storage, DevTools inspection, headed vs headless execution, and how automation drivers (CDP, WebDriver, Playwright protocol) control a browser.

**Absorbed Skill:** Explain how a page loads and renders, inspect DOM/network/storage with DevTools, distinguish headed from headless behavior, and select the right browser engine and control protocol for a scraping or testing task.

---

**Tooling Setup and First Automations**

**Summary:** Installing and configuring Playwright, Puppeteer, and Selenium in Python and Node.js, managing browsers and drivers, launching pages, navigating, taking screenshots, saving HTML/PDF, running headed for debugging and headless for scale, and structuring a first reliable script with proper cleanup.

**Absorbed Skill:** Configure Playwright, Puppeteer, and Selenium environments, launch and navigate browsers, capture screenshots and page data, and execute clean, repeatable first automations with correct startup and teardown.

---

**Reliable Locators and Element Strategy**

**Summary:** User-facing locators (role, text, label, placeholder, test-id) versus brittle CSS/XPath, Playwright locators vs ElementHandles, Puppeteer query patterns, selector strictness, shadow DOM and iframes, dynamic lists, and locator review habits that prevent breakage on minor UI changes.

**Absorbed Skill:** Construct resilient locators from user-visible semantics, diagnose brittle selectors, handle shadow DOM and dynamic content, and apply strictness and fallback rules that keep scripts stable over time.

---

**Waiting, Synchronization and Flake Elimination**

**Summary:** Auto-waiting in Playwright, explicit waits in Puppeteer/Selenium, load states (commit, domcontentloaded, load, networkidle), waiting for selectors vs assertions, eliminating hard sleeps, retry-assertion patterns, timeout tuning, and debugging race conditions and intermittent failures.

**Absorbed Skill:** Apply correct wait strategies for static, client-rendered, and streaming pages, eliminate arbitrary sleeps, tune timeouts, and diagnose and fix flaky automations using traces, logs, and deterministic waits.

---

**Realistic Interaction: Forms, Uploads, Frames, Tabs and Downloads**

**Summary:** Typing with realistic delays, clicking, hovering, scrolling, keyboard shortcuts, file uploads and downloads, handling new tabs/popups, frames, dialogs, date pickers, infinite scroll, drag-and-drop, and verifying each interaction succeeded before proceeding.

**Absorbed Skill:** Execute complete interaction flows across forms, files, frames, tabs, and downloads, simulate human-like input timing, and verify state changes so multi-step journeys complete reliably.

---

**Sessions, Authentication and State Reuse**

**Summary:** Cookie jars, localStorage/sessionStorage, Playwright storageState, Puppeteer session persistence, login-once-and-reuse patterns, token refresh, multi-account isolation with separate contexts, and secure handling of credentials without hardcoding secrets.

**Absorbed Skill:** Implement login-once-and-reuse sessions, persist and restore authenticated state, isolate accounts with separate browser contexts, and manage credentials and tokens securely across runs.

---

**Network Control: Interception, Blocking, Mocking and API Capture**

**Summary:** Request interception and routing, blocking trackers/heavy assets for speed, mocking API responses for deterministic runs, capturing XHR/fetch calls to extract structured JSON directly, HAR recording, and combining DOM scraping with API-level extraction when it is more robust.

**Absorbed Skill:** Intercept and modify requests, block or mock resources, capture underlying APIs for cleaner data extraction, and use HAR files to reverse-engineer efficient scraping paths.

---

**Stealth and Anti-Detection Hardening**

**Summary:** Common detection vectors (navigator.webdriver, headless fingerprints, TLS/JA3, canvas/WebGL/audio fingerprints, automation flags, behavioral signals), Playwright and Puppeteer hardening (playwright-stealth, user-agent/viewport/locale/timezone alignment, plugin and language spoofing), behavioral humanization (mouse curves, typing variance, random delays), and when to escalate to patched builds (Patchright/Rebrowser), Camoufox/Nodriver, or managed anti-detect services.

**Absorbed Skill:** Diagnose why a target blocks automation using fingerprint test pages, apply layered stealth hardening to browser contexts, simulate human-like behavior, and select the appropriate escalation path for Cloudflare, DataDome, and PerimeterX-class protections.

---

**Resilient Production Scraping Pipelines**

**Summary:** Production scraping architecture with automated browsers: job queues and idempotent jobs, per-domain throttling and concurrency limits, exponential-backoff retries with jitter, proxy rotation and sticky sessions, CAPTCHA/challenge triage and graceful degradation, structured logging and tracing, metrics and alerting, result validation and deduping, and checkpointing so failed runs resume without data loss.

**Absorbed Skill:** Design and operate resilient scraping pipelines that throttle politely, retry intelligently, rotate proxies, triage blocks and CAPTCHAs without data loss, validate and dedupe results, and expose logs, traces, and metrics for debugging and monitoring.

---

**Scaling with Contexts, Concurrency and Distributed Queues**

**Summary:** Browser contexts vs pages vs browser instances, parallel workers with Playwright/Puppeteer, asyncio and worker pools in Python, Node worker threads and queues (BullMQ/Celery/RQ), container-per-worker patterns, memory/CPU limits, graceful shutdown, and backpressure when targets slow down.

**Absorbed Skill:** Architect concurrent scraping with isolated contexts, implement worker pools and distributed queues, enforce resource limits and graceful shutdown, and scale throughput without collapsing targets or workers.

---

**Test-Grade Framework Design: Page Objects, CI and Visual Checks**

**Summary:** Page Object Models and fixture patterns shared between testing and scraping, data-driven suites, Playwright Test and Jest/Cucumber integration, CI/CD execution (GitHub Actions/Jenkins), artifact collection (traces, videos, screenshots), visual regression basics, and treating scrapers with the same rigor as end-to-end tests.

**Absorbed Skill:** Construct maintainable automation frameworks with page objects and fixtures, integrate runs into CI/CD, collect traces and artifacts for failure review, and apply visual checks to detect layout-driven breakage.

---

**Operations, Maintenance and Long-Lived Scraper Health**

**Summary:** Operating scrapers over months: change detection for selectors and layouts, scheduled health checks, fingerprint and proxy hygiene, dependency and browser-version pinning, runbooks for blocks and bans, cost and politeness budgets (rate limits, robots.txt, Terms of Service), documentation, and deciding when to switch from DOM scraping to official APIs.

**Absorbed Skill:** Maintain long-lived scrapers through site changes and browser updates, run scheduled health checks and runbooks for blocks, enforce politeness and cost budgets, and evaluate when to migrate from browser scraping to sanctioned APIs.
