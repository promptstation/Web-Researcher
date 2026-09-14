# Course 03 — Modern Web Frameworks
## Curriculum Content Outlook (Researching-Outline workflow, compressed to ≤15 sections)

Source course list: `Web researcher and scrapper.txt` — Course 3: Modern Web Frameworks
Method: Researching-Outline.md workflow (Steps 1–8) + beginner→expert progression research + compression into groups.
Sections: 10 (within the ≤15 limit). Each section = Summary (what it teaches) + Absorbed Skill (capability gained).

---

**Rendering Models: CSR, SSR, SSG and Hydration**

**Summary:** How client-side, server-side, static, and incremental rendering differ in HTML evidence, how hydration attaches behavior to server HTML, and how to pick fetch-first versus browser-first extraction from markers instead of guesses.

**Absorbed Skill:** Identify rendering models from HTML evidence, explain hydration behavior, and choose fetch-first or browser-first extraction correctly.

---

**React and Next.js Extraction Patterns**

**Summary:** How Next.js ships data via SSR HTML, __NEXT_DATA__, data routes, and server components, how to extract each channel fetch-first, and how to handle build IDs, locales, and ISR revalidation without browsers.

**Absorbed Skill:** Extract Next.js data from HTML, payloads, and data routes fetch-first, handling build IDs and locales correctly.

---

**Vue, Nuxt and Svelte Extraction**

**Summary:** How Nuxt payloads, Pinia state, SvelteKit data, and Astro islands expose fetch-first data, how to inventory embedded state generically, and how to build version-tolerant extractors across these frameworks.

**Absorbed Skill:** Inventory embedded framework state generically and extract Nuxt, Vue, Svelte, and Astro data fetch-first.

---

**Angular and Enterprise SPA Patterns**

**Summary:** How Angular apps structure lazy routes, environment configs, and API layers, how enterprise SSO and session patterns gate data, and how to map APIs and routes for lawful, permissioned extraction.

**Absorbed Skill:** Map Angular routes and APIs, handle enterprise auth patterns lawfully, and extract with permissioned sessions.

---

**API-First Extraction: REST and GraphQL Discovery**

**Summary:** How to discover the APIs behind any frontend from bundles, network logs, and well-known paths, how to document contracts, and how to prefer official endpoints with correct auth and pagination over DOM scraping.

**Absorbed Skill:** Discover hidden APIs from frontend evidence, document contracts, and extract API-first with correct auth and pagination.

---

**JavaScript Bundle Analysis**

**Summary:** How to inventory bundles, rank weight, find source maps, trace module boundaries, and scan for leaked secrets and endpoints, turning opaque chunks into mapped attack and extraction surfaces.

**Absorbed Skill:** Inventory bundles by weight and role, recover structure via maps and manifests, and surface secrets and endpoints responsibly.

---

**Client-Side Routing and State**

**Summary:** How SPA routers resolve paths, guards, and lazy modules, how client state flows through stores and caches, and how to enumerate routes and predict data needs for complete extraction coverage.

**Absorbed Skill:** Enumerate SPA routes from sitemaps and bundles, explain guard and state behavior, and plan extraction coverage per route.

---

**Middleware, Signing and Framework Gatekeeping**

**Summary:** How framework middleware, signed URLs, server-only tokens, and edge checks gate content, how to detect each gate from response evidence, and how to respond with permission requests and API-first alternatives instead of circumvention.

**Absorbed Skill:** Detect middleware and signing gates from evidence and respond with lawful alternatives and permission paths.

---

**SPA Automation: Waits and Selectors**

**Summary:** How to automate SPAs reliably with route-aware waits, network-aware assertions, resilient selectors, and hydration checks, so Playwright and Puppeteer suites survive framework timing instead of fighting it.

**Absorbed Skill:** Automate SPAs with route, network, and hydration-aware waits plus resilient selectors that survive refactors.

---

**Framework Upgrades and Breakage Triage**

**Summary:** How to track framework and site upgrades, detect extractor breakage from DOM and contract diffs, classify breakage scope, and recover with versioned fixes plus backfills.

**Absorbed Skill:** Detect upgrade-driven breakage from diffs, classify scope, and recover with versioned extractor fixes and backfills.
