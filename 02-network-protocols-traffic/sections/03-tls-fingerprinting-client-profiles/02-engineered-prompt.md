# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 02 Network Protocols & Traffic Analysis → Section: TLS Fingerprinting and Client Profiles

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“TLS Fingerprinting and Client Profiles”** as part of an advanced course in network protocols, packet analysis, and scraping traffic operations. How ClientHello fields (versions, ciphers, extensions, curves, ALPN) fingerprint TLS clients, how JA3-style hashes summarize handshakes, how to audit your own client profile, and how to interpret server-side TLS decisions for research and defense.

The material should teach how to audit TLS client behavior and interpret handshake outcomes for legitimate research and defense. Go beyond surface-level tips and examine protocol-level traffic analysis as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong network behavior balances **visibility, accuracy, performance, cost, and legal restraint**. Show how these principles apply differently to single-flow debugging, proxy-fleet monitoring, and continuous collection oversight. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to list every ClientHello input that feeds fingerprints, from versions and ciphers to extensions, curves, and ALPN order

Teach how JA3-style hashes summarize those inputs, and what changes or preserves a hash

Teach how to audit local client profiles with handshake output and library introspection

Teach how to interpret server downgrades, alerts, and cipher rejections as fingerprint or policy decisions

Teach how to recommend coherent research profiles that match their stated platform instead of mixing signals

Include practical methods for real projects. Cover:

* ClientHello field inventory
* Local cipher and curve listing
* Handshake capture review
* Hash-stability experiments
* Server-alert interpretation
* Profile coherence checks
* Library-version tracking
* Research scope documentation

Explain how practitioners can avoid profile changes after upgrade (library defaults moved ciphers or extensions).
Explain how practitioners can avoid server picks weak cipher (client offers weak first or server honors client order).
Explain how practitioners can avoid sni-related failures (missing or mismatched server name indication).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover R, E, S, T,  , a, n, d,  , G, r, a, p, h, Q, L,  , A, P, I, s, ,,  , p, a, g, i, n, a, t, e, d,  , l, i, s, t, i, n, g, s, ,,  , a, u, t, h, e, n, t, i, c, a, t, e, d,  , f, e, e, d, s, ,,  , s, t, r, e, a, m, i, n, g,  , e, n, d, p, o, i, n, t, s, ,,  , a, n, d,  , g, e, o, -, d, i, s, t, r, i, b, u, t, e, d,  , t, a, r, g, e, t, s. Keep examples focused on network behavior rather than generic advice.

Include practical exercises that require the learner to:

1. Inventory ClientHello fields for one client with evidence.
2. List local ciphers and curves and compare to a browser profile.
3. Change one library version and record the handshake delta.
4. Interpret three server alerts and name each cause.
5. Write a coherence checklist for research profiles.
6. Document scope limits for fingerprint work.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from TCP/IP, UDP, TLS, HTTP versions, DNS, proxies, and traffic analysis where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize IETF RFCs, Wireshark and tshark documentation, vendor protocol guides, measurement research, and mitmproxy and proxy-server official docs. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **field-inventory checklist**, a **profile-audit checklist**, a **stability-test checklist**, a **coherence-check checklist**, a **scope-note checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
