# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 05 JavaScript Deobfuscation → Section: Encoding and Crypto Layers

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Encoding and Crypto Layers”** as part of an advanced course in JavaScript analysis, deobfuscation, and lawful reverse engineering. How base64, hex, XOR, RC4, and custom ciphers hide payloads in JS, how to identify schemes from shapes, and how to decode layers into readable evidence with key recovery where feasible.

The material should teach how to decode layered JavaScript encodings into verified plaintext. Go beyond surface-level tips and examine obfuscated-code analysis as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong code obscurity balances **speed, accuracy, safety, documentation, and lawful purpose**. Show how these principles apply differently to single-file triage, bundle-wide mapping, and ongoing monitoring. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to recognize base64, hex, unicode, and custom alphabets from blob shapes

Teach how to brute-force single-byte XOR with English scoring

Teach how to implement RC4 including key-scheduling variants found in obfuscators

Teach how to recover embedded keys from adjacent code and decoder arguments

Teach how to chain decodes across layers with verification at each step

Include practical methods for real projects. Cover:

* Alphabet recognition
* Blob extraction
* XOR scoring
* RC4 implementation
* Key harvesting
* Layer chaining
* Plaintext verification
* Codec regression tests

Explain how practitioners can avoid xor scores flat (multi-byte key or non-text plaintext).
Explain how practitioners can avoid rc4 output garbage (wrong variant or key encoding).
Explain how practitioners can avoid decoded but still code-like gibberish (another layer beneath).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover p, a, c, k, e, d,  , m, a, r, k, e, t, i, n, g,  , t, a, g, s, ,,  , p, r, o, t, e, c, t, e, d,  , m, e, d, i, a,  , p, l, a, y, e, r, s, ,,  , b, u, n, d, l, e,  , c, h, u, n, k, s, ,,  , s, u, s, p, i, c, i, o, u, s,  , r, e, d, i, r, e, c, t, s, ,,  , a, n, d,  , t, h, i, r, d, -, p, a, r, t, y,  , w, i, d, g, e, t, s. Keep examples focused on code obscurity rather than generic advice.

Include practical exercises that require the learner to:

1. Identify six encodings from blobs.
2. Crack three XOR blobs.
3. Decode two RC4 layers with harvested keys.
4. Chain a three-layer decode.
5. Verify plaintext at each layer.
6. Add regression tests for one codec.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from parsers, ASTs, encodings, control flow, and dynamic analysis where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize ECMAScript spec, parser and compiler literature, sandbox tooling docs, and malware-analysis methodology. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **alpha-id checklist**, a **xor-cracked checklist**, a **rc4-decoded checklist**, a **chain-verified checklist**, a **tests-added checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
