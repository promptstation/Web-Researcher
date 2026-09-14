# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 01 Browser Engineering → Section: JavaScript Engines and Runtime Behavior

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“JavaScript Engines and Runtime Behavior”** as part of an advanced course in browser engineering, rendering internals, and web runtime behavior. How V8, JavaScriptCore, and SpiderMonkey parse, compile, and optimize JavaScript, how the event loop schedules macro and micro tasks, how promises, async functions, and workers behave, and how to profile main-thread cost and memory with heap and allocation timelines.

The material should teach how to profile JavaScript runtime behavior and fix scheduling, layout, and memory faults from trace evidence. Go beyond surface-level tips and examine browser internals analysis as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong browser behavior balances **correctness, performance, compatibility, observability, and security**. Show how these principles apply differently to single-page debugging, fleet-wide scraping, and long-lived monitoring. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how engine tiers move code from parse to baseline to optimized compilation, and what deoptimization looks like in traces

Teach how the event loop orders rendering, timers, promises, and I/O, so scheduling bugs become predictable instead of mysterious

Teach how to profile main-thread cost with long-task entries, bottom-up handler tables, and forced-layout warnings

Teach how to diagnose leaks with comparative heap snapshots, allocation timelines, and detached-DOM checks

Teach how to offload parsing, crypto, and search indexing to workers and idle callbacks without breaking ordering or state

Include practical methods for real projects. Cover:

* Event-loop order prediction drills
* Long-task and INP attribution
* Bottom-up handler cost tables
* Forced synchronous layout detection
* Comparative heap snapshots
* Allocation timeline leak hunts
* Detached DOM and listener audits
* Worker and scheduleriment offload patterns

Explain how practitioners can avoid deopt warnings and slow optimized code (hidden-class churn or mixed-type hot paths).
Explain how practitioners can avoid microtask starvation of rendering (promise chains that never yield to the render step).
Explain how practitioners can avoid worker slower than main thread (serialization cost or chatty messaging).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover e, -, c, o, m, m, e, r, c, e,  , p, r, o, d, u, c, t,  , p, a, g, e, s, ,,  , n, e, w, s,  , a, r, t, i, c, l, e,  , t, e, m, p, l, a, t, e, s, ,,  , a, u, t, h, e, n, t, i, c, a, t, e, d,  , d, a, s, h, b, o, a, r, d, s, ,,  , s, i, n, g, l, e, -, p, a, g, e,  , a, p, p, l, i, c, a, t, i, o, n, s, ,,  , a, n, d,  , m, e, d, i, a, -, h, e, a, v, y,  , l, a, n, d, i, n, g,  , p, a, g, e, s. Keep examples focused on browser behavior rather than generic advice.

Include practical exercises that require the learner to:

1. Predict then verify execution order for a mixed timer/promise/script snippet.
2. Attribute a page's worst long task to a handler with bottom-up proof.
3. Find and fix one forced layout with before/after layout counts.
4. Hunt a leak with three snapshots and name the retaining path.
5. Move one heavy transform to a worker; prove main thread freed.
6. Schedule non-critical hydration in idle time without shifting layout.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from browser architecture, rendering pipelines, JavaScript runtimes, networking, and web security where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize Chromium design documentation, WHATWG and W3C specifications, V8 and WebKit engineering blogs, MDN Web Docs, and peer-reviewed web performance literature. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **loop-model checklist**, a **longtask-attribution checklist**, a **layout-guard checklist**, a **leak-proof checklist**, a **offload-verify checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
