# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 02 Network Protocols & Traffic Analysis → Section: Proxy Protocols: HTTP, SOCKS and Tunnels

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Proxy Protocols: HTTP, SOCKS and Tunnels”** as part of an advanced course in network protocols, packet analysis, and scraping traffic operations. How HTTP forward proxies, CONNECT tunneling, SOCKS4/5 handshakes, and modern tunnels compare, how to verify chains hop by hop, and how to choose and test egress for scraping fleets without leaking DNS or credentials.

The material should teach how to operate proxy protocols with verified chains and leak-free egress selection. Go beyond surface-level tips and examine protocol-level traffic analysis as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong network behavior balances **visibility, accuracy, performance, cost, and legal restraint**. Show how these principles apply differently to single-flow debugging, proxy-fleet monitoring, and continuous collection oversight. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to contrast forward proxying, CONNECT tunneling, and SOCKS handshakes with byte-level honesty

Teach how to trace where DNS resolves and credentials travel on each hop of a chain

Teach how to verify chains hop by hop with echo endpoints and header inspection

Teach how to detect DNS, SNI, header, and WebRTC leaks that defeat proxying

Teach how to select egress pools by target sensitivity, geography needs, and cost per gigabyte

Include practical methods for real projects. Cover:

* Protocol contrast drills
* Chain mapping per route
* Hop-by-hop echo tests
* DNS resolution-path checks
* Header and SNI leak tests
* Credential-handling review
* Pool selection matrices
* Egress health scoring

Explain how practitioners can avoid 407 despite correct password (auth scheme mismatch or credential encoding).
Explain how practitioners can avoid socks handshake hangs (version or auth-method mismatch).
Explain how practitioners can avoid geo wrong at exit (stale geoip or anycast exit).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover R, E, S, T,  , a, n, d,  , G, r, a, p, h, Q, L,  , A, P, I, s, ,,  , p, a, g, i, n, a, t, e, d,  , l, i, s, t, i, n, g, s, ,,  , a, u, t, h, e, n, t, i, c, a, t, e, d,  , f, e, e, d, s, ,,  , s, t, r, e, a, m, i, n, g,  , e, n, d, p, o, i, n, t, s, ,,  , a, n, d,  , g, e, o, -, d, i, s, t, r, i, b, u, t, e, d,  , t, a, r, g, e, t, s. Keep examples focused on network behavior rather than generic advice.

Include practical exercises that require the learner to:

1. Draw byte flows for CONNECT versus SOCKS5 for one HTTPS fetch.
2. Verify a two-hop chain hop by hop with echo endpoints.
3. Prove where DNS resolves for three proxy configs.
4. Find one header leak and close it.
5. Build a pool-selection matrix for tolerant, sensitive, and authed traffic.
6. Score three egresses and quarantine the worst with cause.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from TCP/IP, UDP, TLS, HTTP versions, DNS, proxies, and traffic analysis where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize IETF RFCs, Wireshark and tshark documentation, vendor protocol guides, measurement research, and mitmproxy and proxy-server official docs. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **protocol-map checklist**, a **chain-verify checklist**, a **leak-sweep checklist**, a **pool-matrix checklist**, a **health-score checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
