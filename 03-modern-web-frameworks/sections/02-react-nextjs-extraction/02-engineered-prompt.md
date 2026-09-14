# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 03 Modern Web Frameworks → Section: React and Next.js Extraction Patterns

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“React and Next.js Extraction Patterns”** as part of an advanced course in modern web frameworks, SPA rendering, and API-first extraction. How Next.js ships data via SSR HTML, __NEXT_DATA__, data routes, and server components, how to extract each channel fetch-first, and how to handle build IDs, locales, and ISR revalidation without browsers.

The material should teach how to extract Next.js applications through payloads, data routes, and underlying APIs without browsers. Go beyond surface-level tips and examine framework-aware extraction as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong framework behavior balances **robustness, speed, maintainability, politeness, and API preference**. Show how these principles apply differently to single-page reverse engineering, template-wide extraction, and continuous monitoring. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to parse __NEXT_DATA__ into pageProps with schema checks and version stamps

Teach how to construct _next/data URLs from buildId plus route plus locale, and refresh buildId safely

Teach how to handle locales, base paths, zones, and rewrites so URLs stay valid across regions

Teach how to read server-component streaming hints and decide when HTML parsing beats flight parsing

Teach how to fall back to underlying REST or GraphQL APIs with pinned versions when payloads shift

Include practical methods for real projects. Cover:

* Payload parsing with schemas
* BuildId discovery and refresh
* Data-route construction
* Locale and basePath handling
* Flight-payload triage
* Underlying-API mapping
* ISR staleness checks
* Version-pinned fallbacks

Explain how practitioners can avoid data routes 404 suddenly (new deploy rotated buildid).
Explain how practitioners can avoid pageprops keys renamed (app refactor changed payload shape).
Explain how practitioners can avoid locale returns default content (wrong prefix or cookie-based locale).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover N, e, x, t, ., j, s,  , s, t, o, r, e, f, r, o, n, t, s, ,,  , N, u, x, t,  , c, o, n, t, e, n, t,  , s, i, t, e, s, ,,  , A, n, g, u, l, a, r,  , e, n, t, e, r, p, r, i, s, e,  , p, o, r, t, a, l, s, ,,  , S, v, e, l, t, e, K, i, t,  , a, p, p, s, ,,  , a, n, d,  , h, e, a, d, l, e, s, s, -, C, M, S,  , f, r, o, n, t, e, n, d, s. Keep examples focused on framework behavior rather than generic advice.

Include practical exercises that require the learner to:

1. Extract one listing page purely from __NEXT_DATA__.
2. Construct data-route URLs for three routes with buildId.
3. Handle two locales without hardcoding paths.
4. Decide HTML versus flight parsing for one page with reasons.
5. Map the underlying API behind one data route.
6. Build a refresh-safe extractor with buildId renewal.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from rendering models, hydration, routing, state management, and API design where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize framework official docs (Next.js, Nuxt, SvelteKit, Angular), Web.dev rendering guides, HTTP API design literature, and bundle-analysis tooling docs. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **payload-parse checklist**, a **dataroute-build checklist**, a **locale-proof checklist**, a **flight-triage checklist**, a **fallback-pin checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
