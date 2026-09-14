# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 01 Browser Engineering → Section: Security Model: SOP, CORS, CSP and Sandboxing

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Security Model: SOP, CORS, CSP and Sandboxing”** as part of an advanced course in browser engineering, rendering internals, and web runtime behavior. How same-origin policy, CORS, content security policy, frame controls, and sandboxing constrain pages, how to read and test each control from headers and behavior, and how to fix misconfigurations without opening holes.

The material should teach how to audit origin-scoped browser controls and tighten them without breaking legitimate function. Go beyond surface-level tips and examine browser internals analysis as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong browser behavior balances **correctness, performance, compatibility, observability, and security**. Show how these principles apply differently to single-page debugging, fleet-wide scraping, and long-lived monitoring. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how same-origin policy scopes DOM access, storage, and network reads differently, and where developers most often misjudge the boundary

Teach how to trace CORS from Origin header through preflight to credentialed response, naming each failure mode

Teach how to write content security policies that block injection while allowing real dependencies, then verify with violation reports

Teach how to audit framing controls, cross-origin isolation, and iframe sandboxing as one coherent embedding policy

Teach how to fix permissive wildcards, missing directives, and credential mistakes with compatibility proof per change

Include practical methods for real projects. Cover:

* Origin and trust-boundary mapping
* Preflight tracing with curl and DevTools
* CSP drafting from violation reports
* Header audits across routes
* Framing and embedding matrix
* Sandbox attribute selection
* Credential-mode review
* Report-only rollout protocol

Explain how practitioners can avoid preflight passes but response blocked (actual response missing acao or vary mishandling).
Explain how practitioners can avoid csp blocks blob or data workers (worker-src or script-src missing schemes).
Explain how practitioners can avoid sandboxed frame lost needed ability (missing allow token for scripts, forms, or same-origin).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover e, -, c, o, m, m, e, r, c, e,  , p, r, o, d, u, c, t,  , p, a, g, e, s, ,,  , n, e, w, s,  , a, r, t, i, c, l, e,  , t, e, m, p, l, a, t, e, s, ,,  , a, u, t, h, e, n, t, i, c, a, t, e, d,  , d, a, s, h, b, o, a, r, d, s, ,,  , s, i, n, g, l, e, -, p, a, g, e,  , a, p, p, l, i, c, a, t, i, o, n, s, ,,  , a, n, d,  , m, e, d, i, a, -, h, e, a, v, y,  , l, a, n, d, i, n, g,  , p, a, g, e, s. Keep examples focused on browser behavior rather than generic advice.

Include practical exercises that require the learner to:

1. Map origins and trust boundaries for one multi-subdomain app.
2. Trace a failing CORS call and name the exact failing check.
3. Draft a CSP from report-only data; ship with zero new violations.
4. Audit framing controls and close one clickjacking gap.
5. Sandbox a third-party embed without breaking its function.
6. Roll out one policy change with compatibility proof.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from browser architecture, rendering pipelines, JavaScript runtimes, networking, and web security where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize Chromium design documentation, WHATWG and W3C specifications, V8 and WebKit engineering blogs, MDN Web Docs, and peer-reviewed web performance literature. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **origin-map checklist**, a **cors-trace checklist**, a **csp-rollout checklist**, a **framing-matrix checklist**, a **compat-proof checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
