# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 06 Automated Browsers → Section: Waiting and Synchronization

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Waiting and Synchronization”** as part of an advanced course in automated browsers, Playwright and Puppeteer operations, and production scraping. How auto-waiting, assertion retries, load states, and response waits compose into flake-free synchronization, how to classify flakes by cause, and how to eliminate sleeps systematically.

The material should teach how to synchronize browser automation deterministically and end flakiness. Go beyond surface-level tips and examine browser automation operations as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong automation reliability balances **reliability, speed, politeness, observability, and maintainability**. Show how these principles apply differently to first scripts, suite automation, and fleet operations. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to layer URL, locator, assertion, and response waits for each interaction

Teach how to size assertion retries and timeouts from measured timing

Teach how to scope network waits so polling never deadlocks suites

Teach how to classify flakes into timing, selector, data, environment, and product causes

Teach how to run sleep-elimination sprints with repeat-run proof

Include practical methods for real projects. Cover:

* Wait layering
* Retry sizing
* Network scoping
* Flake taxonomy
* Trace reading
* Sleep hunts
* Repeat-run proof
* Quarantine policy

Explain how practitioners can avoid assertion timeout spikes (undersized retries on slow env).
Explain how practitioners can avoid fixed locally, flakes in ci (resource or parallelism gaps).
Explain how practitioners can avoid one flake resists classification (product race or a/b variant).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover s, t, o, r, e, f, r, o, n, t, s, ,,  , n, e, w, s,  , s, i, t, e, s, ,,  , t, r, a, v, e, l,  , l, i, s, t, i, n, g, s, ,,  , j, o, b,  , b, o, a, r, d, s, ,,  , a, n, d,  , a, u, t, h, e, n, t, i, c, a, t, e, d,  , d, a, s, h, b, o, a, r, d, s. Keep examples focused on automation reliability rather than generic advice.

Include practical exercises that require the learner to:

1. Layer waits for one flow from scratch.
2. Size retries from timing data.
3. Fix one networkidle deadlock.
4. Classify ten flakes correctly.
5. Eliminate five sleeps with proof.
6. Prove 50 clean runs.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from locators, waits, contexts, interception, and pipeline reliability where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize Playwright and Puppeteer official docs, WebDriver BiDi specs, testing best-practice guides, and SRE literature. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **layer-map checklist**, a **retry-size checklist**, a **scope-safe checklist**, a **flake-classes checklist**, a **sleep-zero checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
