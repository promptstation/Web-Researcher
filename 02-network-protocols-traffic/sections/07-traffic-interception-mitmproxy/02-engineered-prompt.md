# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 02 Network Protocols & Traffic Analysis → Section: Traffic Interception with mitmproxy

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Traffic Interception with mitmproxy”** as part of an advanced course in network protocols, packet analysis, and scraping traffic operations. How to run mitmproxy for owned test traffic: CA install, upstream modes, addon scripting for logging and modification, and evidence handling, with strict scope so interception never touches traffic you are not authorized to inspect.

The material should teach how to operate traffic interception on authorized test flows with scripted, reviewable addons. Go beyond surface-level tips and examine protocol-level traffic analysis as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong network behavior balances **visibility, accuracy, performance, cost, and legal restraint**. Show how these principles apply differently to single-flow debugging, proxy-fleet monitoring, and continuous collection oversight. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to install the mitmproxy CA on test devices and route only in-scope traffic through the proxy

Teach how to choose regular, reverse, transparent, and upstream modes based on what must be observed

Teach how to write addons that log flows to JSONL, modify requests safely, and block out-of-scope hosts

Teach how to replay flows and script deterministic sequences for regression tests

Teach how to handle intercepted evidence with redaction, retention, and scope documentation

Include practical methods for real projects. Cover:

* Scope definition worksheets
* CA install verification
* Mode selection matrix
* Addon scaffolding
* Flow logging schemas
* Modification guardrails
* Replay scripting
* Evidence hygiene

Explain how practitioners can avoid app pins certs and refuses proxy (certificate pinning on test builds).
Explain how practitioners can avoid flows missing for one host (out-of-scope block or direct connection).
Explain how practitioners can avoid replay nondeterministic (timestamps, nonces, or ordering variance).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover R, E, S, T,  , a, n, d,  , G, r, a, p, h, Q, L,  , A, P, I, s, ,,  , p, a, g, i, n, a, t, e, d,  , l, i, s, t, i, n, g, s, ,,  , a, u, t, h, e, n, t, i, c, a, t, e, d,  , f, e, e, d, s, ,,  , s, t, r, e, a, m, i, n, g,  , e, n, d, p, o, i, n, t, s, ,,  , a, n, d,  , g, e, o, -, d, i, s, t, r, i, b, u, t, e, d,  , t, a, r, g, e, t, s. Keep examples focused on network behavior rather than generic advice.

Include practical exercises that require the learner to:

1. Define scope for one test app in writing.
2. Install CA and verify interception on test traffic only.
3. Log 50 flows to JSONL with redaction.
4. Modify one API response and document behavior.
5. Replay a login flow deterministically.
6. Produce a redacted evidence pack.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from TCP/IP, UDP, TLS, HTTP versions, DNS, proxies, and traffic analysis where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize IETF RFCs, Wireshark and tshark documentation, vendor protocol guides, measurement research, and mitmproxy and proxy-server official docs. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **scope-sheet checklist**, a **ca-verify checklist**, a **mode-pick checklist**, a **addon-review checklist**, a **evidence-pack checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
