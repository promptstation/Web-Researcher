# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 05 JavaScript Deobfuscation → Section: Sandboxed Dynamic Analysis

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Sandboxed Dynamic Analysis”** as part of an advanced course in JavaScript analysis, deobfuscation, and lawful reverse engineering. How to observe obfuscated code safely in isolated sandboxes with stubbed globals, logged calls, timeouts, and network denial, turning runtime behavior into documented evidence.

The material should teach how to capture obfuscated-code behavior through isolated, logged execution. Go beyond surface-level tips and examine obfuscated-code analysis as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong code obscurity balances **speed, accuracy, safety, documentation, and lawful purpose**. Show how these principles apply differently to single-file triage, bundle-wide mapping, and ongoing monitoring. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to isolate execution with VMs, timeouts, and no host or network access

Teach how to stub document, window, fetch, and storage so payloads run far enough to reveal intent

Teach how to log function calls, DOM writes, and exfil attempts with full arguments

Teach how to enforce time, memory, and loop budgets that stop runaway payloads

Teach how to document behavior as evidence with hashes, versions, and transcripts

Include practical methods for real projects. Cover:

* Isolation checklists
* Stub libraries
* Call logging
* Budget enforcement
* Transcript capture
* Artifact hashing
* Environment matrices
* Report templates

Explain how practitioners can avoid sample exits silently (missing stub or environment gate).
Explain how practitioners can avoid infinite loop burns budget (anti-analysis delay loops).
Explain how practitioners can avoid different behavior per run (time, random, or remote keying).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover p, a, c, k, e, d,  , m, a, r, k, e, t, i, n, g,  , t, a, g, s, ,,  , p, r, o, t, e, c, t, e, d,  , m, e, d, i, a,  , p, l, a, y, e, r, s, ,,  , b, u, n, d, l, e,  , c, h, u, n, k, s, ,,  , s, u, s, p, i, c, i, o, u, s,  , r, e, d, i, r, e, c, t, s, ,,  , a, n, d,  , t, h, i, r, d, -, p, a, r, t, y,  , w, i, d, g, e, t, s. Keep examples focused on code obscurity rather than generic advice.

Include practical exercises that require the learner to:

1. Sandbox one sample with full logs.
2. Stub a new global convincingly.
3. Capture one exfil attempt transcript.
4. Enforce budgets on a looping sample.
5. Matrix-test two environments.
6. Write one behavior report.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from parsers, ASTs, encodings, control flow, and dynamic analysis where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize ECMAScript spec, parser and compiler literature, sandbox tooling docs, and malware-analysis methodology. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **isolated-ok checklist**, a **stubs-logged checklist**, a **budgets-hit checklist**, a **transcript-saved checklist**, a **report-filed checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
