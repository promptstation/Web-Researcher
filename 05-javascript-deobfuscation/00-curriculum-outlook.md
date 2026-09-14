# Course 05 — JavaScript Deobfuscation
## Curriculum Content Outlook (Researching-Outline workflow, compressed to ≤15 sections)

Source course list: `Web researcher and scrapper.txt` — Course 5: JavaScript Deobfuscation
Method: Researching-Outline.md workflow (Steps 1–8) + beginner→expert progression research + compression into groups.
Sections: 10 (within the ≤15 limit). Each section = Summary (what it teaches) + Absorbed Skill (capability gained).

---

**Obfuscation Landscape and Triage**

**Summary:** How minification, packing, string-array obfuscation, control-flow flattening, and exotic encodings differ in fingerprints, how to classify samples fast, and how to route each class to the right technique.

**Absorbed Skill:** Classify obfuscation types from fingerprints and route samples to correct deobfuscation techniques.

---

**Beautification and Normalization**

**Summary:** How to format minified code readably, normalize quotes and unicode escapes, unwrap trivial packers, and produce stable baselines that later decoding and AST passes can build on.

**Absorbed Skill:** Normalize minified and packed code into readable, stable baselines for deeper analysis.

---

**String Arrays and Rotation**

**Summary:** How obfuscators hide strings in rotated arrays with decoder functions, how to extract arrays, emulate rotation, resolve decoders, and restore readable literals safely.

**Absorbed Skill:** Extract string arrays, emulate rotation, resolve decoder calls, and restore literals without executing payloads.

---

**Control-Flow Simplification**

**Summary:** How flattened dispatchers, opaque predicates, and dead branches obscure logic, how to sketch control flow, prune the provably dead, and recover the real execution order for review.

**Absorbed Skill:** Sketch flattened control flow, prune dead branches, and recover readable execution order.

---

**Renaming and AST-Level Cleanup**

**Summary:** How to rename mangled identifiers deterministically, inline trivial aliases, fold constants, and clean AST-shaped patterns so analysis and diffs stay stable across builds.

**Absorbed Skill:** Rename mangled identifiers deterministically and clean trivial aliasing for stable analysis.

---

**Sandboxed Dynamic Analysis**

**Summary:** How to observe obfuscated code safely in isolated sandboxes with stubbed globals, logged calls, timeouts, and network denial, turning runtime behavior into documented evidence.

**Absorbed Skill:** Run suspicious JavaScript in isolated sandboxes with stubs and logs to capture behavior safely.

---

**Anti-Debug and Anti-Tamper Traps**

**Summary:** How debugger statements, DevTools detection, timing checks, domain locks, and self-defending code slow analysis, how to catalog traps, and how to neutralize them for lawful analysis without harming production integrity.

**Absorbed Skill:** Catalog anti-analysis traps and neutralize them in lab copies for lawful analysis.

---

**Encoding and Crypto Layers**

**Summary:** How base64, hex, XOR, RC4, and custom ciphers hide payloads in JS, how to identify schemes from shapes, and how to decode layers into readable evidence with key recovery where feasible.

**Absorbed Skill:** Identify encoding and cipher layers and decode them into readable evidence with documented keys.

---

**Malicious JavaScript Triage**

**Summary:** How to risk-score suspicious scripts from static signals, decide detonate versus static-only analysis, extract IOCs safely, and disclose through proper channels with evidence packs.

**Absorbed Skill:** Risk-score suspicious JavaScript, extract IOCs safely, and disclose with evidence packs.

---

**Interop Reversing and Endpoint Recovery**

**Summary:** How to reverse engineer frontend code for lawful interoperability: recovering undocumented endpoints, data shapes, and protocols to build compatible integrations, with clean-room notes and permission trails.

**Absorbed Skill:** Recover endpoints and protocols from frontend code for lawful interop with documented clean-room practice.
