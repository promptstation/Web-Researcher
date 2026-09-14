# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 03 Modern Web Frameworks → Section: SPA Automation: Waits and Selectors

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“SPA Automation: Waits and Selectors”** as part of an advanced course in modern web frameworks, SPA rendering, and API-first extraction. How to automate SPAs reliably with route-aware waits, network-aware assertions, resilient selectors, and hydration checks, so Playwright and Puppeteer suites survive framework timing instead of fighting it.

The material should teach how to automate single-page applications reliably with framework-aware waits and selectors. Go beyond surface-level tips and examine framework-aware extraction as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong framework behavior balances **robustness, speed, maintainability, politeness, and API preference**. Show how these principles apply differently to single-page reverse engineering, template-wide extraction, and continuous monitoring. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to wait on route changes, DOM states, and assertions instead of fixed sleeps

Teach how to use network idle and response waits without deadlocking on polling or streams

Teach how to choose role, text, and test-id selectors that survive refactors

Teach how to verify hydration completed before clicking or typing

Teach how to structure page objects around user flows rather than component trees

Include practical methods for real projects. Cover:

* Route-wait patterns
* Assertion-retry design
* Network-wait scoping
* Selector ladder
* Hydration checks
* Flow-based page objects
* Flake taxonomy
* Trace-driven debugging

Explain how practitioners can avoid click misses after navigation (detached element across route change).
Explain how practitioners can avoid strict-mode violations (duplicate matches from lists or portals).
Explain how practitioners can avoid hydration double-render flake (interacting before client takeover).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover N, e, x, t, ., j, s,  , s, t, o, r, e, f, r, o, n, t, s, ,,  , N, u, x, t,  , c, o, n, t, e, n, t,  , s, i, t, e, s, ,,  , A, n, g, u, l, a, r,  , e, n, t, e, r, p, r, i, s, e,  , p, o, r, t, a, l, s, ,,  , S, v, e, l, t, e, K, i, t,  , a, p, p, s, ,,  , a, n, d,  , h, e, a, d, l, e, s, s, -, C, M, S,  , f, r, o, n, t, e, n, d, s. Keep examples focused on framework behavior rather than generic advice.

Include practical exercises that require the learner to:

1. Replace five sleeps with route or assertion waits.
2. Scope one network wait that avoids polling deadlock.
3. Rewrite ten selectors up the resilience ladder.
4. Add hydration gates to one suite.
5. Refactor one page object to flow-based design.
6. Debug one flake from trace to fix.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from rendering models, hydration, routing, state management, and API design where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize framework official docs (Next.js, Nuxt, SvelteKit, Angular), Web.dev rendering guides, HTTP API design literature, and bundle-analysis tooling docs. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **wait-audit checklist**, a **network-scope checklist**, a **selector-ladder checklist**, a **hydrate-gate checklist**, a **flake-fix checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
