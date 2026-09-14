# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 01 Browser Engineering → Section: Rendering Performance and the Critical Path

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Rendering Performance and the Critical Path”** as part of an advanced course in browser engineering, rendering internals, and web runtime behavior. How to budget, measure, and fix rendering performance end to end: Core Web Vitals, critical request chains, resource prioritization, image and font strategy, and build-time guards that stop regressions before deploy.

The material should teach how to deliver rendering performance through measurement, critical-path fixes, and enforced budgets. Go beyond surface-level tips and examine browser internals analysis as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong browser behavior balances **correctness, performance, compatibility, observability, and security**. Show how these principles apply differently to single-page debugging, fleet-wide scraping, and long-lived monitoring. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to read Largest Contentful Paint, Interaction to Next Paint, and Cumulative Layout Shift, and why field data often disagrees with lab runs

Teach how to map critical request chains from waterfalls so each millisecond of delay has an owner

Teach how to prioritize hero images, fonts, and API calls while deferring everything provably non-critical

Teach how to right-size images, subset fonts, and contain third parties with facades and delayed hydration

Teach how to enforce transfer, count, and timing budgets in builds and reviews so wins survive future deploys

Include practical methods for real projects. Cover:

* Vitals triage: lab versus field
* Critical-chain mapping
* Priority and fetchpriority tuning
* Responsive image auditing
* Font subsetting and display strategy
* Third-party facade patterns
* Budget definition per template
* Regression drill on failure

Explain how practitioners can avoid lab green but field red (device, network, or cache-state gaps between lab and users).
Explain how practitioners can avoid lcp element shifts between runs (racing hero candidates or a/b variants).
Explain how practitioners can avoid budget failures ignored (noisy guard or no owner for failures).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover e, -, c, o, m, m, e, r, c, e,  , p, r, o, d, u, c, t,  , p, a, g, e, s, ,,  , n, e, w, s,  , a, r, t, i, c, l, e,  , t, e, m, p, l, a, t, e, s, ,,  , a, u, t, h, e, n, t, i, c, a, t, e, d,  , d, a, s, h, b, o, a, r, d, s, ,,  , s, i, n, g, l, e, -, p, a, g, e,  , a, p, p, l, i, c, a, t, i, o, n, s, ,,  , a, n, d,  , m, e, d, i, a, -, h, e, a, v, y,  , l, a, n, d, i, n, g,  , p, a, g, e, s. Keep examples focused on browser behavior rather than generic advice.

Include practical exercises that require the learner to:

1. Triage one page's vitals and separate lab-only from field-real issues.
2. Map the critical chain and name each hop's owner and cost.
3. Fix one LCP image with priority plus sizing; measure the delta.
4. Cut one third party with a facade; prove interaction preserved.
5. Define budgets for two templates and wire one guard.
6. Run a regression drill: detect, bisect, and fix a planted slowdown.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from browser architecture, rendering pipelines, JavaScript runtimes, networking, and web security where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize Chromium design documentation, WHATWG and W3C specifications, V8 and WebKit engineering blogs, MDN Web Docs, and peer-reviewed web performance literature. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **vitals-triage checklist**, a **chain-map checklist**, a **hero-fix checklist**, a **budget-guard checklist**, a **regression-drill checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
