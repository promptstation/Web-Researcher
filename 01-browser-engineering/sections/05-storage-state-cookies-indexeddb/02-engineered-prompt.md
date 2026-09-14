# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 01 Browser Engineering → Section: Storage and State: Cookies, Web Storage, IndexedDB

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Storage and State: Cookies, Web Storage, IndexedDB”** as part of an advanced course in browser engineering, rendering internals, and web runtime behavior. How browsers persist state across cookies, localStorage, sessionStorage, IndexedDB, Cache Storage, and service workers, how partitioning and expiry bound tracking, and how to inspect, migrate, and clear state without breaking sessions or leaking secrets.

The material should teach how to audit browser storage tiers for correctness, capacity, and secrecy, and manage state changes without breakage. Go beyond surface-level tips and examine browser internals analysis as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong browser behavior balances **correctness, performance, compatibility, observability, and security**. Show how these principles apply differently to single-page debugging, fleet-wide scraping, and long-lived monitoring. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to compare storage tiers by lifetime, scope, capacity, and script access, and pick the right tier for session, preference, cache, and offline data

Teach how to audit cookie flags so session cookies are Secure, HttpOnly, SameSite-scoped, and minimally lived

Teach how to measure per-origin usage and quota with the Storage API and DevTools application panel

Teach how to migrate IndexedDB schemas and clear caches without logging users out or orphaning in-flight writes

Teach how third-party storage partitioning changes embedded flows, and how to test partitioned behavior before users feel it

Include practical methods for real projects. Cover:

* Cookie flag audit across session and analytics cookies
* Storage census: usage, quota, and per-store breakdown
* Expiry and eviction policy review
* IndexedDB version and migration testing
* Cache Storage key hygiene
* Service-worker state separation checks
* Partitioned-storage behavior tests
* Secret-free storage verification

Explain how practitioners can avoid users logged out after deploy (clear-all on version change or cookie scope narrowed).
Explain how practitioners can avoid embedded widget broke recently (third-party storage now partitioned or blocked).
Explain how practitioners can avoid quotaexceedederror on repeat visits (unbounded cache keys without eviction).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover e, -, c, o, m, m, e, r, c, e,  , p, r, o, d, u, c, t,  , p, a, g, e, s, ,,  , n, e, w, s,  , a, r, t, i, c, l, e,  , t, e, m, p, l, a, t, e, s, ,,  , a, u, t, h, e, n, t, i, c, a, t, e, d,  , d, a, s, h, b, o, a, r, d, s, ,,  , s, i, n, g, l, e, -, p, a, g, e,  , a, p, p, l, i, c, a, t, i, o, n, s, ,,  , a, n, d,  , m, e, d, i, a, -, h, e, a, v, y,  , l, a, n, d, i, n, g,  , p, a, g, e, s. Keep examples focused on browser behavior rather than generic advice.

Include practical exercises that require the learner to:

1. Audit every cookie on one login flow and fix missing flags.
2. Census storage for three origins and chart usage versus quota.
3. Migrate an IndexedDB store across versions without data loss.
4. Clear site data selectively while preserving the session.
5. Reproduce a partitioned-storage break and document the fix.
6. Prove no tokens or PII persist in the wrong tier.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from browser architecture, rendering pipelines, JavaScript runtimes, networking, and web security where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize Chromium design documentation, WHATWG and W3C specifications, V8 and WebKit engineering blogs, MDN Web Docs, and peer-reviewed web performance literature. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **cookie-flags checklist**, a **storage-census checklist**, a **migration-proof checklist**, a **partition-test checklist**, a **secret-sweep checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
