# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 01 Browser Engineering → Section: Headless Internals and Automation Hooks

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Headless Internals and Automation Hooks”** as part of an advanced course in browser engineering, rendering internals, and web runtime behavior. How headless modes differ from headed rendering (GPU paths, media, permissions, lifecycle), how automation hooks attach via CDP, WebDriver, and BiDi, and how to prove headed/headless parity before trusting automated results.

The material should teach how to verify headless configurations and prove automation parity with headed behavior. Go beyond surface-level tips and examine browser internals analysis as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong browser behavior balances **correctness, performance, compatibility, observability, and security**. Show how these principles apply differently to single-page debugging, fleet-wide scraping, and long-lived monitoring. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how headless modes differ in GPU compositing, media codecs, font rendering, and permission prompts, and which differences actually matter for your task

Teach how to verify launch configurations flag by flag instead of copying snippets, confirming each flag's effect

Teach how automation hooks attach at different privilege levels, and what each hook can observe or change

Teach how to build parity checks that diff screenshots, DOM, console, and network between headed and headless

Teach how to decide when headless suffices, when xvfb or headed is required, and how to document the decision

Include practical methods for real projects. Cover:

* Launch matrix per task class
* Flag-by-flag verification
* GPU path confirmation
* Media and permission probes
* Parity diff protocol
* Hook privilege mapping
* Failure-mode comparison
* Mode decision records

Explain how practitioners can avoid media never loads headless (missing codecs, autoplay policy, or gpu-dependent pipeline).
Explain how practitioners can avoid permission prompts stall automation (headless permission defaults differ from headed grants).
Explain how practitioners can avoid timing flakes only in automation (faster execution exposing races, not rendering differences).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover e, -, c, o, m, m, e, r, c, e,  , p, r, o, d, u, c, t,  , p, a, g, e, s, ,,  , n, e, w, s,  , a, r, t, i, c, l, e,  , t, e, m, p, l, a, t, e, s, ,,  , a, u, t, h, e, n, t, i, c, a, t, e, d,  , d, a, s, h, b, o, a, r, d, s, ,,  , s, i, n, g, l, e, -, p, a, g, e,  , a, p, p, l, i, c, a, t, i, o, n, s, ,,  , a, n, d,  , m, e, d, i, a, -, h, e, a, v, y,  , l, a, n, d, i, n, g,  , p, a, g, e, s. Keep examples focused on browser behavior rather than generic advice.

Include practical exercises that require the learner to:

1. Build a launch matrix for scraping, testing, and screenshot tasks.
2. Verify five common flags and document each one's real effect.
3. Run a parity diff on three pages and explain every delta.
4. Map three hooks to their privilege levels with proof.
5. Decide headed vs headless for one defended target with evidence.
6. Write a mode decision record a teammate can audit.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from browser architecture, rendering pipelines, JavaScript runtimes, networking, and web security where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize Chromium design documentation, WHATWG and W3C specifications, V8 and WebKit engineering blogs, MDN Web Docs, and peer-reviewed web performance literature. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **launch-matrix checklist**, a **flag-verify checklist**, a **parity-diff checklist**, a **hook-map checklist**, a **mode-decision checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
