# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 05 JavaScript Deobfuscation → Section: Renaming and AST-Level Cleanup

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Renaming and AST-Level Cleanup”** as part of an advanced course in JavaScript analysis, deobfuscation, and lawful reverse engineering. How to rename mangled identifiers deterministically, inline trivial aliases, fold constants, and clean AST-shaped patterns so analysis and diffs stay stable across builds.

The material should teach how to restore readable, stable identifiers to mangled JavaScript. Go beyond surface-level tips and examine obfuscated-code analysis as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong code obscurity balances **speed, accuracy, safety, documentation, and lawful purpose**. Show how these principles apply differently to single-file triage, bundle-wide mapping, and ongoing monitoring. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to scope identifiers to functions and blocks so renames never collide

Teach how to rename hex and single-letter identifiers deterministically from usage roles

Teach how to inline trivial aliases and single-use wrappers safely

Teach how to fold provably safe constants while preserving behavior

Teach how to keep renaming stable across builds for diffable outputs

Include practical methods for real projects. Cover:

* Scope mapping
* Role inference
* Deterministic naming
* Alias inlining
* Constant folding
* Stability hashing
* Diff verification
* Rule freezing

Explain how practitioners can avoid rename collision (same name across scopes merged).
Explain how practitioners can avoid inlined alias breaks code (hidden second use or side effect).
Explain how practitioners can avoid builds still undiffable (nondeterministic ordering or timestamps).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover p, a, c, k, e, d,  , m, a, r, k, e, t, i, n, g,  , t, a, g, s, ,,  , p, r, o, t, e, c, t, e, d,  , m, e, d, i, a,  , p, l, a, y, e, r, s, ,,  , b, u, n, d, l, e,  , c, h, u, n, k, s, ,,  , s, u, s, p, i, c, i, o, u, s,  , r, e, d, i, r, e, c, t, s, ,,  , a, n, d,  , t, h, i, r, d, -, p, a, r, t, y,  , w, i, d, g, e, t, s. Keep examples focused on code obscurity rather than generic advice.

Include practical exercises that require the learner to:

1. Rename one file deterministically.
2. Inline ten aliases with proof.
3. Fold constants in one module.
4. Prove rename stability across rebuilds.
5. Diff two builds after renaming.
6. Freeze one rule set.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from parsers, ASTs, encodings, control flow, and dynamic analysis where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize ECMAScript spec, parser and compiler literature, sandbox tooling docs, and malware-analysis methodology. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **scope-map checklist**, a **rename-stable checklist**, a **inline-proof checklist**, a **fold-safe checklist**, a **diff-clean checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
