# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 03 Modern Web Frameworks → Section: Rendering Models: CSR, SSR, SSG and Hydration

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Rendering Models: CSR, SSR, SSG and Hydration”** as part of an advanced course in modern web frameworks, SPA rendering, and API-first extraction. How client-side, server-side, static, and incremental rendering differ in HTML evidence, how hydration attaches behavior to server HTML, and how to pick fetch-first versus browser-first extraction from markers instead of guesses.

The material should teach how to classify rendering models from evidence and route extraction to the cheapest working path. Go beyond surface-level tips and examine framework-aware extraction as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong framework behavior balances **robustness, speed, maintainability, politeness, and API preference**. Show how these principles apply differently to single-page reverse engineering, template-wide extraction, and continuous monitoring. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to distinguish rendering models from root HTML: empty roots, payload scripts, meta generators, and header clues

Teach how hydration attaches events to server HTML, and which mismatches cause visible or silent faults

Teach how to measure fetch-side completeness with text length, link counts, and data-presence checks

Teach how to choose fetch-first extraction when data ships in HTML or payloads, and browser-first only when proven necessary

Teach how to verify verdicts across routes since frameworks mix models per page

Include practical methods for real projects. Cover:

* Marker inventory per route
* Fetch-side completeness scoring
* Payload-script inspection
* Header and meta evidence
* Route-by-route model mapping
* Hydration-mismatch reading
* Extraction-path decision tree
* Verdict re-verification

Explain how practitioners can avoid payload present but data missing (client-only fetch after hydrate or auth-gated props).
Explain how practitioners can avoid ssr verdict but empty fetch (bot-gated ssr or geo/consent wall).
Explain how practitioners can avoid hydration errors in console (nondeterministic render: dates, random, extensions).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover N, e, x, t, ., j, s,  , s, t, o, r, e, f, r, o, n, t, s, ,,  , N, u, x, t,  , c, o, n, t, e, n, t,  , s, i, t, e, s, ,,  , A, n, g, u, l, a, r,  , e, n, t, e, r, p, r, i, s, e,  , p, o, r, t, a, l, s, ,,  , S, v, e, l, t, e, K, i, t,  , a, p, p, s, ,,  , a, n, d,  , h, e, a, d, l, e, s, s, -, C, M, S,  , f, r, o, n, t, e, n, d, s. Keep examples focused on framework behavior rather than generic advice.

Include practical exercises that require the learner to:

1. Classify rendering models for five routes of one site.
2. Score fetch-side completeness for a product page.
3. Find the payload script carrying listing data.
4. Justify fetch-first versus browser-first for one flow.
5. Reproduce a hydration mismatch and explain it.
6. Map models across an entire storefront section.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from rendering models, hydration, routing, state management, and API design where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize framework official docs (Next.js, Nuxt, SvelteKit, Angular), Web.dev rendering guides, HTTP API design literature, and bundle-analysis tooling docs. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **marker-inventory checklist**, a **completeness-score checklist**, a **payload-find checklist**, a **path-decision checklist**, a **route-map checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
