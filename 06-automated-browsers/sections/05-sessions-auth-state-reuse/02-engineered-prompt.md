# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 06 Automated Browsers → Section: Sessions, Auth and State Reuse

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Sessions, Auth and State Reuse”** as part of an advanced course in automated browsers, Playwright and Puppeteer operations, and production scraping. How to authenticate once and reuse state across runs with storage snapshots, how to isolate accounts, refresh tokens, and handle secrets without leaks.

The material should teach how to operate authenticated automation with safe session reuse. Go beyond surface-level tips and examine browser automation operations as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong automation reliability balances **reliability, speed, politeness, observability, and maintainability**. Show how these principles apply differently to first scripts, suite automation, and fleet operations. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to capture storage state after real logins with minimal necessary scope

Teach how to isolate accounts with one context and state file each

Teach how to refresh tokens before expiry with re-login fallbacks

Teach how to handle MFA with human-in-the-loop where permitted, never bypassed

Teach how to audit state files and artifacts so secrets never leak

Include practical methods for real projects. Cover:

* Login-once design
* State capture protocol
* Account isolation
* Refresh scheduling
* MFA handling policy
* Secret auditing
* Rotation drills
* Access reviews

Explain how practitioners can avoid state expires mid-suite (short tokens, long suites).
Explain how practitioners can avoid accounts cross-contaminate (shared context or state file).
Explain how practitioners can avoid mfa blocks automation (policy requires human verification).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover s, t, o, r, e, f, r, o, n, t, s, ,,  , n, e, w, s,  , s, i, t, e, s, ,,  , t, r, a, v, e, l,  , l, i, s, t, i, n, g, s, ,,  , j, o, b,  , b, o, a, r, d, s, ,,  , a, n, d,  , a, u, t, h, e, n, t, i, c, a, t, e, d,  , d, a, s, h, b, o, a, r, d, s. Keep examples focused on automation reliability rather than generic advice.

Include practical exercises that require the learner to:

1. Build one login-once pipeline.
2. Isolate three accounts cleanly.
3. Schedule proactive refresh.
4. Handle one MFA flow lawfully.
5. Audit artifacts for secrets.
6. Drill one credential rotation.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from locators, waits, contexts, interception, and pipeline reliability where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize Playwright and Puppeteer official docs, WebDriver BiDi specs, testing best-practice guides, and SRE literature. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **login-once-live checklist**, a **isolation-proof checklist**, a **refresh-scheduled checklist**, a **mfa-lawful checklist**, a **secrets-clean checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
