# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 01 Browser Engineering → Section: DevTools and CDP for Reverse Engineering

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“DevTools and CDP for Reverse Engineering”** as part of an advanced course in browser engineering, rendering internals, and web runtime behavior. How to wield Elements, Network, Sources, Performance, Memory, and Application panels plus the Chrome DevTools Protocol to reverse-engineer page behavior, capture APIs, override responses, and script observations that the UI cannot repeat.

The material should teach how to reverse-engineer web behavior with panels and protocol automation and preserve findings as runnable scripts. Go beyond surface-level tips and examine browser internals analysis as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong browser behavior balances **correctness, performance, compatibility, observability, and security**. Show how these principles apply differently to single-page debugging, fleet-wide scraping, and long-lived monitoring. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to work each DevTools panel as one instrument: elements for structure, network for truth, sources for breakpoints, performance for cost, memory for retention, application for state

Teach how to capture complete traffic including fetch, XHR, WebSockets, and event streams, and export HAR plus curl replays

Teach how to override headers, bodies, and block patterns to test hypotheses without touching source

Teach how to drive CDP domains for page lifecycle, network interception, runtime evaluation, and target management from scripts

Teach how to convert a manual finding into a repeatable script with selectors, waits, and assertions a teammate can rerun

Include practical methods for real projects. Cover:

* Panel-by-panel flow walkthroughs
* HAR capture with preserved logs and disabled cache
* WebSocket frame inspection
* Request blocking and response overrides
* Breakpoint strategies: DOM, XHR, event listener
* CDP target discovery via the HTTP endpoint
* Fetch-domain interception patterns
* Finding-to-script conversion protocol

Explain how practitioners can avoid har misses early requests (recording started after navigation or cache served silently).
Explain how practitioners can avoid cdp endpoint refuses connection (browser not launched with remote debugging or wrong port/profile).
Explain how practitioners can avoid override has no effect (wrong url pattern, cached response, or worker bypass).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover e, -, c, o, m, m, e, r, c, e,  , p, r, o, d, u, c, t,  , p, a, g, e, s, ,,  , n, e, w, s,  , a, r, t, i, c, l, e,  , t, e, m, p, l, a, t, e, s, ,,  , a, u, t, h, e, n, t, i, c, a, t, e, d,  , d, a, s, h, b, o, a, r, d, s, ,,  , s, i, n, g, l, e, -, p, a, g, e,  , a, p, p, l, i, c, a, t, i, o, n, s, ,,  , a, n, d,  , m, e, d, i, a, -, h, e, a, v, y,  , l, a, n, d, i, n, g,  , p, a, g, e, s. Keep examples focused on browser behavior rather than generic advice.

Include practical exercises that require the learner to:

1. Reverse-engineer a login flow and name every API call with purpose.
2. Capture a checkout HAR and extract the pricing API contract.
3. Override one API response and document the UI behavior change.
4. List CDP targets for a debugging-enabled browser and attach to one.
5. Convert a manual override experiment into a runnable script.
6. Write a reverse-engineering report a second analyst can verify.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from browser architecture, rendering pipelines, JavaScript runtimes, networking, and web security where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize Chromium design documentation, WHATWG and W3C specifications, V8 and WebKit engineering blogs, MDN Web Docs, and peer-reviewed web performance literature. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **panel-walk checklist**, a **traffic-capture checklist**, a **override-proof checklist**, a **cdp-attach checklist**, a **script-conversion checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
