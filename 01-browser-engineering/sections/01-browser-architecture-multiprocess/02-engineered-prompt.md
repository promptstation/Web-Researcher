# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 01 Browser Engineering → Section: Browser Architecture and the Multi-Process Model

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Browser Architecture and the Multi-Process Model”** as part of an advanced course in browser engineering, rendering internals, and web runtime behavior. How Chromium, Firefox, and WebKit structure work across browser, renderer, GPU, network, and utility processes, how the rendering pipeline flows from navigation to pixels, how site isolation and sandboxing contain failures, and how automation protocols attach to each layer.

The material should teach how to map browser architecture to observable symptoms and correct automation hooks, so every diagnosis starts at the responsible layer. Go beyond surface-level tips and examine browser internals analysis as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong browser behavior balances **correctness, performance, compatibility, observability, and security**. Show how these principles apply differently to single-page debugging, fleet-wide scraping, and long-lived monitoring. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to map each process type to its responsibilities, IPC boundaries, and failure blast radius, using chrome task manager and about:memory style evidence

Teach how to trace a navigation through network fetch, commit, parser, style, layout, paint, and composite, naming which stage each common symptom implicates

Teach how site isolation and sandboxing contain compromised renderers, and what that implies for automation privileges and file access

Teach how to choose between DevTools UI, CDP domains, WebDriver classic, and WebDriver BiDi based on which layer must be observed or driven

Teach how to diagnose hangs, white screens, and renderer kills from process signals, exit codes, and sampling profiles rather than guessing

Include practical methods for real projects. Cover:

* Process inventory via task manager and command-line type flags
* Navigation lifecycle mapping: pending, commit,DOMContentLoaded, load
* Rendering pipeline walk: parse, style, layout, paint, composite
* Site isolation checks per origin and frame
* Sandbox capability review for automation contexts
* Protocol selection matrix: CDP vs WebDriver vs BiDi
* Crash triage from exit codes and dump summaries
* Memory-per-process budgeting for fleet sizing

Explain how practitioners can avoid renderer uses gigabytes on one page (leaking dom/js heap or unbounded canvas buffers in that site's renderer).
Explain how practitioners can avoid aw snap / renderer kill under load (oom, stack exhaustion, or sandbox-triggered termination).
Explain how practitioners can avoid automation sees different behavior than headed user (different gpu path, user agent, viewport, or missing human-behavior pacing).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover e, -, c, o, m, m, e, r, c, e,  , p, r, o, d, u, c, t,  , p, a, g, e, s, ,,  , n, e, w, s,  , a, r, t, i, c, l, e,  , t, e, m, p, l, a, t, e, s, ,,  , a, u, t, h, e, n, t, i, c, a, t, e, d,  , d, a, s, h, b, o, a, r, d, s, ,,  , s, i, n, g, l, e, -, p, a, g, e,  , a, p, p, l, i, c, a, t, i, o, n, s, ,,  , a, n, d,  , m, e, d, i, a, -, h, e, a, v, y,  , l, a, n, d, i, n, g,  , p, a, g, e, s. Keep examples focused on browser behavior rather than generic advice.

Include practical exercises that require the learner to:

1. Inventory the processes of a loaded news page and label each one's role and memory share.
2. Trace one navigation and produce a stage-by-stage timeline with commit markers.
3. Reproduce a renderer kill and document exit code, recovery behavior, and user-visible symptom.
4. Compare CDP, WebDriver, and BiDi for intercepting one request, and justify the pick.
5. Size a scraping worker: contexts per browser given per-renderer memory measurements.
6. Write a one-page runbook: blank page triage from process signals to fix.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from browser architecture, rendering pipelines, JavaScript runtimes, networking, and web security where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize Chromium design documentation, WHATWG and W3C specifications, V8 and WebKit engineering blogs, MDN Web Docs, and peer-reviewed web performance literature. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **architecture-map checklist**, a **navigation-trace checklist**, a **sandbox-review checklist**, a **protocol-choice checklist**, a **crash-triage checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
