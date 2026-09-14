# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 01 Browser Engineering → Section: Fingerprinting Surfaces and Identity Signals

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Fingerprinting Surfaces and Identity Signals”** as part of an advanced course in browser engineering, rendering internals, and web runtime behavior. Which browser signals form fingerprints (user agent, navigator, screen, canvas, WebGL, audio, fonts, TLS, behavior), how entropy combines across layers, how to audit your own exposure, and how to test changes without building deception tooling for abuse.

The material should teach how to audit fingerprint exposure and signal consistency for legitimate research and defensive hardening. Go beyond surface-level tips and examine browser internals analysis as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong browser behavior balances **correctness, performance, compatibility, observability, and security**. Show how these principles apply differently to single-page debugging, fleet-wide scraping, and long-lived monitoring. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to enumerate fingerprint surfaces across JavaScript properties, canvas and WebGL rendering, audio pipelines, fonts, TLS handshakes, and interaction behavior

Teach how to measure exposure with established test pages plus a local probe snippet, recording before/after deltas

Teach how weak signals stack into identifying entropy, and why single-property spoofing usually increases uniqueness

Teach how to audit a research setup for signal consistency so measurements reflect the intended configuration

Teach how to recommend defensive exposure reduction such as standard viewports, reduced motion, and minimal plugin surfaces

Include practical methods for real projects. Cover:

* Surface inventory per layer
* Test-page measurement protocol
* Local probe dumps with hashing
* Entropy-stacking analysis
* Consistency checks across signals
* Configuration delta testing
* Defensive hardening lists
* Research ethics and scope notes

Explain how practitioners can avoid test pages disagree (different signal sets, datasets, or visit timing).
Explain how practitioners can avoid one spoofed value increased uniqueness (incoherent tuple draws attention).
Explain how practitioners can avoid canvas hash differs per run (gpu driver variance, font updates, or noise injection).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover e, -, c, o, m, m, e, r, c, e,  , p, r, o, d, u, c, t,  , p, a, g, e, s, ,,  , n, e, w, s,  , a, r, t, i, c, l, e,  , t, e, m, p, l, a, t, e, s, ,,  , a, u, t, h, e, n, t, i, c, a, t, e, d,  , d, a, s, h, b, o, a, r, d, s, ,,  , s, i, n, g, l, e, -, p, a, g, e,  , a, p, p, l, i, c, a, t, i, o, n, s, ,,  , a, n, d,  , m, e, d, i, a, -, h, e, a, v, y,  , l, a, n, d, i, n, g,  , p, a, g, e, s. Keep examples focused on browser behavior rather than generic advice.

Include practical exercises that require the learner to:

1. Inventory 30 signals across four layers for one browser profile.
2. Measure exposure on two test pages and record the verdicts.
3. Change one signal and show the consistency delta.
4. Explain why a spoofed property increased uniqueness in one case.
5. Write a defensive hardening list for a research workstation.
6. Document scope limits for fingerprint research in one page.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from browser architecture, rendering pipelines, JavaScript runtimes, networking, and web security where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize Chromium design documentation, WHATWG and W3C specifications, V8 and WebKit engineering blogs, MDN Web Docs, and peer-reviewed web performance literature. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **surface-inventory checklist**, a **exposure-measure checklist**, a **consistency-audit checklist**, a **defense-list checklist**, a **scope-note checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
