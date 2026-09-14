# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 01 Browser Engineering → Section: HTML and CSS Parsing with Render Tree Construction

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“HTML and CSS Parsing with Render Tree Construction”** as part of an advanced course in browser engineering, rendering internals, and web runtime behavior. How parsers build DOM and CSSOM under speculative and blocking rules, how render, style, and layout trees relate, how render-blocking scripts and styles delay pixels, and how to measure DOM weight and style cost on real pages.

The material should teach how to diagnose render-tree cost and remove render-blocking work with paint-timing proof. Go beyond surface-level tips and examine browser internals analysis as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong browser behavior balances **correctness, performance, compatibility, observability, and security**. Show how these principles apply differently to single-page debugging, fleet-wide scraping, and long-lived monitoring. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to distinguish DOM, CSSOM, render tree, and layout tree, and which DevTools counters prove bloat in each

Teach how to identify render-blocking scripts, stylesheets, and fonts from waterfall position plus parser state

Teach how to measure DOM node counts, tree depth, and style recalculation cost with traces instead of guesses

Teach how to apply defer, async, preload, preconnect, and media-gated CSS so ordering stays correct while pixels arrive sooner

Teach how to verify every fix with first paint, largest paint, and layout-shift readings taken the same way before and after

Include practical methods for real projects. Cover:

* DOM census: node count, depth, and listener totals
* Waterfall reading for parser-blocking positions
* Coverage runs to find unused CSS and JS
* Defer/async placement with execution-order proof
* Preload and preconnect for critical fonts and APIs
* Media-gated and split stylesheets for non-critical CSS
* Containment and content-visibility for long lists
* Before/after paint timing protocol

Explain how practitioners can avoid defer broke page behavior (order-dependent scripts or dom-ready assumptions violated).
Explain how practitioners can avoid flash of unstyled content after css split (above-fold rules moved to deferred bundle).
Explain how practitioners can avoid paint improved but interaction still slow (main-thread script cost after paint, not parse blocking).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover e, -, c, o, m, m, e, r, c, e,  , p, r, o, d, u, c, t,  , p, a, g, e, s, ,,  , n, e, w, s,  , a, r, t, i, c, l, e,  , t, e, m, p, l, a, t, e, s, ,,  , a, u, t, h, e, n, t, i, c, a, t, e, d,  , d, a, s, h, b, o, a, r, d, s, ,,  , s, i, n, g, l, e, -, p, a, g, e,  , a, p, p, l, i, c, a, t, i, o, n, s, ,,  , a, n, d,  , m, e, d, i, a, -, h, e, a, v, y,  , l, a, n, d, i, n, g,  , p, a, g, e, s. Keep examples focused on browser behavior rather than generic advice.

Include practical exercises that require the learner to:

1. Census a product page: nodes, depth, listeners, and the three heaviest subtrees.
2. Find every render-blocking request and rank by paint delay caused.
3. Convert blocking scripts to defer/async without breaking order; prove order with logs.
4. Split one stylesheet into critical and deferred parts; measure paint deltas.
5. Apply content-visibility to a long list and quantify layout cost reduction.
6. Produce a before/after report with identical measurement steps.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from browser architecture, rendering pipelines, JavaScript runtimes, networking, and web security where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize Chromium design documentation, WHATWG and W3C specifications, V8 and WebKit engineering blogs, MDN Web Docs, and peer-reviewed web performance literature. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **dom-census checklist**, a **blocker-rank checklist**, a **ordering-proof checklist**, a **paint-verify checklist**, a **regression-guard checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
