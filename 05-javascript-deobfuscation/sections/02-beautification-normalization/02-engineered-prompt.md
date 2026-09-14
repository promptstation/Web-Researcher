# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 05 JavaScript Deobfuscation → Section: Beautification and Normalization

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Beautification and Normalization”** as part of an advanced course in JavaScript analysis, deobfuscation, and lawful reverse engineering. How to format minified code readably, normalize quotes and unicode escapes, unwrap trivial packers, and produce stable baselines that later decoding and AST passes can build on.

The material should teach how to normalize obfuscated-adjacent code into stable readable baselines. Go beyond surface-level tips and examine obfuscated-code analysis as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong code obscurity balances **speed, accuracy, safety, documentation, and lawful purpose**. Show how these principles apply differently to single-file triage, bundle-wide mapping, and ongoing monitoring. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to format minified code with brace-aware indentation without changing semantics

Teach how to normalize unicode escapes, hex escapes, and quote styles for readability

Teach how to unwrap eval-packed layers safely by emulation-free decoding

Teach how to split giant lines into statements for review and diffing

Teach how to produce stable baselines so later passes show clean diffs

Include practical methods for real projects. Cover:

* Brace-aware formatting
* Escape normalization
* Packer unwrapping
* Statement splitting
* Baseline snapshotting
* Diff-driven review
* Idempotency checks
* Corpus formatting

Explain how practitioners can avoid formatter mangles strings (regex formatting inside template literals).
Explain how practitioners can avoid unwrap output will not parse (partial decode or multi-layer pack).
Explain how practitioners can avoid non-idempotent output (stateful rules or line-length churn).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover p, a, c, k, e, d,  , m, a, r, k, e, t, i, n, g,  , t, a, g, s, ,,  , p, r, o, t, e, c, t, e, d,  , m, e, d, i, a,  , p, l, a, y, e, r, s, ,,  , b, u, n, d, l, e,  , c, h, u, n, k, s, ,,  , s, u, s, p, i, c, i, o, u, s,  , r, e, d, i, r, e, c, t, s, ,,  , a, n, d,  , t, h, i, r, d, -, p, a, r, t, y,  , w, i, d, g, e, t, s. Keep examples focused on code obscurity rather than generic advice.

Include practical exercises that require the learner to:

1. Format three minified files readably.
2. Normalize one escape-heavy file.
3. Unwrap one packed layer safely.
4. Split one 5k-char line file.
5. Baseline before/after for one sample.
6. Verify idempotent formatting.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from parsers, ASTs, encodings, control flow, and dynamic analysis where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize ECMAScript spec, parser and compiler literature, sandbox tooling docs, and malware-analysis methodology. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **format-clean checklist**, a **escapes-sane checklist**, a **unwrapped-safe checklist**, a **baseline-saved checklist**, a **idempotent-ok checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
