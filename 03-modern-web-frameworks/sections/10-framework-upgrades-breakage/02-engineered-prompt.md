# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 03 Modern Web Frameworks → Section: Framework Upgrades and Breakage Triage

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Framework Upgrades and Breakage Triage”** as part of an advanced course in modern web frameworks, SPA rendering, and API-first extraction. How to track framework and site upgrades, detect extractor breakage from DOM and contract diffs, classify breakage scope, and recover with versioned fixes plus backfills.

The material should teach how to maintain extractors through site upgrades with diff-driven triage and clean backfills. Go beyond surface-level tips and examine framework-aware extraction as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong framework behavior balances **robustness, speed, maintainability, politeness, and API preference**. Show how these principles apply differently to single-page reverse engineering, template-wide extraction, and continuous monitoring. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to monitor deploy signals such as buildId rotation, chunk renames, and header changes

Teach how to diff DOM contracts and payload schemas across runs to catch breakage early

Teach how to classify breakage as template, route, locale, or data-source scoped

Teach how to ship versioned extractor fixes with dual-read transitions

Teach how to backfill affected windows without duplicates or gaps

Include practical methods for real projects. Cover:

* Deploy-signal watching
* Contract snapshotting
* Schema diffing
* Scope classification
* Versioned fixing
* Dual-read transitions
* Windowed backfills
* Drift alerting

Explain how practitioners can avoid diffs too noisy (timestamps, ads, and a/b noise).
Explain how practitioners can avoid backfill duplicates (non-idempotent writes or changed ids).
Explain how practitioners can avoid fix works then breaks again (rolling deploy with mixed versions).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover N, e, x, t, ., j, s,  , s, t, o, r, e, f, r, o, n, t, s, ,,  , N, u, x, t,  , c, o, n, t, e, n, t,  , s, i, t, e, s, ,,  , A, n, g, u, l, a, r,  , e, n, t, e, r, p, r, i, s, e,  , p, o, r, t, a, l, s, ,,  , S, v, e, l, t, e, K, i, t,  , a, p, p, s, ,,  , a, n, d,  , h, e, a, d, l, e, s, s, -, C, M, S,  , f, r, o, n, t, e, n, d, s. Keep examples focused on framework behavior rather than generic advice.

Include practical exercises that require the learner to:

1. Set up deploy-signal checks for one site.
2. Snapshot contracts for three templates.
3. Classify one real breakage by scope.
4. Ship a versioned fix with dual-read.
5. Backfill one window cleanly.
6. Tune drift alerts to rare-and-real.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from rendering models, hydration, routing, state management, and API design where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize framework official docs (Next.js, Nuxt, SvelteKit, Angular), Web.dev rendering guides, HTTP API design literature, and bundle-analysis tooling docs. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **signal-watch checklist**, a **contract-snap checklist**, a **scope-class checklist**, a **version-fix checklist**, a **backfill-proof checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
