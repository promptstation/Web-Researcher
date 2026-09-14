# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 05 JavaScript Deobfuscation → Section: Malicious JavaScript Triage

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Malicious JavaScript Triage”** as part of an advanced course in JavaScript analysis, deobfuscation, and lawful reverse engineering. How to risk-score suspicious scripts from static signals, decide detonate versus static-only analysis, extract IOCs safely, and disclose through proper channels with evidence packs.

The material should teach how to triage malicious JavaScript from signals to disclosed, blocked IOCs. Go beyond surface-level tips and examine obfuscated-code analysis as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong code obscurity balances **speed, accuracy, safety, documentation, and lawful purpose**. Show how these principles apply differently to single-file triage, bundle-wide mapping, and ongoing monitoring. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to score risk from eval usage, network calls, obfuscation depth, and exfil shapes

Teach how to decide static-only versus sandboxed detonation from the score

Teach how to extract URLs, endpoints, and payload shapes without touching them live

Teach how to contain via blocks and takedown requests with evidence

Teach how to disclose to owners, vendors, and registries responsibly

Include practical methods for real projects. Cover:

* Risk rubrics
* Detonation criteria
* IOC extraction
* Defanging rules
* Block deployment
* Takedown drafting
* Disclosure tracking
* Victim notification

Explain how practitioners can avoid score borderline (mixed benign and suspicious signals).
Explain how practitioners can avoid iocs rotate fast (dga or fresh infrastructure).
Explain how practitioners can avoid disclosure ignored (wrong contact or abuse-desks flooded).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover p, a, c, k, e, d,  , m, a, r, k, e, t, i, n, g,  , t, a, g, s, ,,  , p, r, o, t, e, c, t, e, d,  , m, e, d, i, a,  , p, l, a, y, e, r, s, ,,  , b, u, n, d, l, e,  , c, h, u, n, k, s, ,,  , s, u, s, p, i, c, i, o, u, s,  , r, e, d, i, r, e, c, t, s, ,,  , a, n, d,  , t, h, i, r, d, -, p, a, r, t, y,  , w, i, d, g, e, t, s. Keep examples focused on code obscurity rather than generic advice.

Include practical exercises that require the learner to:

1. Score ten samples with the rubric.
2. Decide detonation for five borderline.
3. Extract IOCs from three actives.
4. Defang one evidence pack.
5. Draft one takedown request.
6. Track one disclosure to close.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from parsers, ASTs, encodings, control flow, and dynamic analysis where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize ECMAScript spec, parser and compiler literature, sandbox tooling docs, and malware-analysis methodology. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **risk-scored checklist**, a **detonate-call checklist**, a **ioc-list checklist**, a **blocked-done checklist**, a **disclosed-closed checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
