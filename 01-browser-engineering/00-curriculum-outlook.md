# Course 01 — Browser Engineering
## Curriculum Content Outlook (Researching-Outline workflow, compressed to ≤15 sections)

Source course list: `Web researcher and scrapper.txt` — Course 1: Browser Engineering
Method: Researching-Outline.md workflow (Steps 1–8) + beginner→expert progression research + compression into groups.
Sections: 10 (within the ≤15 limit). Each section = Summary (what it teaches) + Absorbed Skill (capability gained).

---

**Browser Architecture and the Multi-Process Model**

**Summary:** How Chromium, Firefox, and WebKit structure work across browser, renderer, GPU, network, and utility processes, how the rendering pipeline flows from navigation to pixels, how site isolation and sandboxing contain failures, and how automation protocols attach to each layer.

**Absorbed Skill:** Explain process boundaries and the navigation-to-pixels pipeline, map a symptom to the responsible process or layer, and choose the correct inspection or automation hook for each.

---

**HTML and CSS Parsing with Render Tree Construction**

**Summary:** How parsers build DOM and CSSOM under speculative and blocking rules, how render, style, and layout trees relate, how render-blocking scripts and styles delay pixels, and how to measure DOM weight and style cost on real pages.

**Absorbed Skill:** Explain parse, style, and layout dependencies, identify render-blocking resources, and reduce DOM and style cost with measured before/after evidence.

---

**JavaScript Engines and Runtime Behavior**

**Summary:** How V8, JavaScriptCore, and SpiderMonkey parse, compile, and optimize JavaScript, how the event loop schedules macro and micro tasks, how promises, async functions, and workers behave, and how to profile main-thread cost and memory with heap and allocation timelines.

**Absorbed Skill:** Explain engine tiers and event-loop scheduling, profile main-thread and memory cost, and fix long tasks, leaks, and worker misuse with trace evidence.

---

**Network Stack: DNS, TLS, HTTP/2/3 and Caching**

**Summary:** How browsers resolve, connect, secure, and multiplex fetches across HTTP/1.1, HTTP/2, and HTTP/3, how TLS handshakes, certificates, and ALPN negotiate security, and how memory, disk, and service-worker caches decide freshness without refetching.

**Absorbed Skill:** Explain connection setup and protocol negotiation, audit TLS and caching headers, and cut connection and revalidation cost with header and protocol fixes.

---

**Storage and State: Cookies, Web Storage, IndexedDB**

**Summary:** How browsers persist state across cookies, localStorage, sessionStorage, IndexedDB, Cache Storage, and service workers, how partitioning and expiry bound tracking, and how to inspect, migrate, and clear state without breaking sessions or leaking secrets.

**Absorbed Skill:** Explain storage tiers and lifetimes, audit cookie flags and storage quotas, and manage sessions and migrations without data loss or secret leakage.

---

**DevTools and CDP for Reverse Engineering**

**Summary:** How to wield Elements, Network, Sources, Performance, Memory, and Application panels plus the Chrome DevTools Protocol to reverse-engineer page behavior, capture APIs, override responses, and script observations that the UI cannot repeat.

**Absorbed Skill:** Reverse-engineer any page flow with panels and protocol domains, capture underlying APIs, and script repeatable observations via CDP.

---

**Fingerprinting Surfaces and Identity Signals**

**Summary:** Which browser signals form fingerprints (user agent, navigator, screen, canvas, WebGL, audio, fonts, TLS, behavior), how entropy combines across layers, how to audit your own exposure, and how to test changes without building deception tooling for abuse.

**Absorbed Skill:** Enumerate fingerprint surfaces, measure exposure with test pages and probes, and evaluate consistency of identity signals for research and defense.

---

**Security Model: SOP, CORS, CSP and Sandboxing**

**Summary:** How same-origin policy, CORS, content security policy, frame controls, and sandboxing constrain pages, how to read and test each control from headers and behavior, and how to fix misconfigurations without opening holes.

**Absorbed Skill:** Explain origin-scoped controls, audit security headers and CORS behavior, and tighten policies with compatibility proof.

---

**Headless Internals and Automation Hooks**

**Summary:** How headless modes differ from headed rendering (GPU paths, media, permissions, lifecycle), how automation hooks attach via CDP, WebDriver, and BiDi, and how to prove headed/headless parity before trusting automated results.

**Absorbed Skill:** Explain headless differences, verify launch configurations, and prove parity between automated and human-driven renders.

---

**Rendering Performance and the Critical Path**

**Summary:** How to budget, measure, and fix rendering performance end to end: Core Web Vitals, critical request chains, resource prioritization, image and font strategy, and build-time guards that stop regressions before deploy.

**Absorbed Skill:** Budget and measure rendering performance, fix critical-path waste, and guard releases with performance budgets.
