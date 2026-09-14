# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 03 Modern Web Frameworks → Section: JavaScript Bundle Analysis

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“JavaScript Bundle Analysis”** as part of an advanced course in modern web frameworks, SPA rendering, and API-first extraction. How to inventory bundles, rank weight, find source maps, trace module boundaries, and scan for leaked secrets and endpoints, turning opaque chunks into mapped attack and extraction surfaces.

The material should teach how to analyze production JS bundles for structure, weight, secrets, and endpoint surfaces. Go beyond surface-level tips and examine framework-aware extraction as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong framework behavior balances **robustness, speed, maintainability, politeness, and API preference**. Show how these principles apply differently to single-page reverse engineering, template-wide extraction, and continuous monitoring. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to inventory chunks from HTML and manifests and rank them by weight and role

Teach how to find and use published source maps for structure without touching unprovided sources

Teach how to trace vendor versus app boundaries from chunk names and module wrappers

Teach how to scan for leaked secrets with pattern evidence and responsible disclosure paths

Teach how to extract endpoint and configuration surfaces for mapping, not exploitation

Include practical methods for real projects. Cover:

* Chunk census
* Weight ranking
* Map discovery
* Boundary tracing
* Secret-pattern scanning
* Config extraction
* Endpoint surfacing
* Disclosure handling

Explain how practitioners can avoid no source maps found (maps withheld or external-pathed).
Explain how practitioners can avoid secret scanner noise (hashes and test fixtures matching patterns).
Explain how practitioners can avoid chunks rename each deploy (content hashing working as designed).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover N, e, x, t, ., j, s,  , s, t, o, r, e, f, r, o, n, t, s, ,,  , N, u, x, t,  , c, o, n, t, e, n, t,  , s, i, t, e, s, ,,  , A, n, g, u, l, a, r,  , e, n, t, e, r, p, r, i, s, e,  , p, o, r, t, a, l, s, ,,  , S, v, e, l, t, e, K, i, t,  , a, p, p, s, ,,  , a, n, d,  , h, e, a, d, l, e, s, s, -, C, M, S,  , f, r, o, n, t, e, n, d, s. Keep examples focused on framework behavior rather than generic advice.

Include practical exercises that require the learner to:

1. Census chunks for one app with weight ranks.
2. Recover module structure from one source map.
3. Separate vendor from app code with evidence.
4. Scan one bundle for secrets and triage hits.
5. Extract the config surface for mapping.
6. Write a disclosure note for one finding.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from rendering models, hydration, routing, state management, and API design where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize framework official docs (Next.js, Nuxt, SvelteKit, Angular), Web.dev rendering guides, HTTP API design literature, and bundle-analysis tooling docs. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **chunk-census checklist**, a **map-recovery checklist**, a **boundary-trace checklist**, a **secret-triage checklist**, a **surface-list checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
