# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 02 Network Protocols & Traffic Analysis → Section: HTTP Versions: 1.1, 2 and 3 in Practice

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“HTTP Versions: 1.1, 2 and 3 in Practice”** as part of an advanced course in network protocols, packet analysis, and scraping traffic operations. How HTTP/1.1 keep-alive and pipelining limits, HTTP/2 multiplexing and prioritization, and HTTP/3 QUIC streams behave on real targets, how to confirm negotiated versions, and how to shape client behavior per version for speed and politeness.

The material should teach how to verify HTTP version behavior per origin and tune clients to each version's mechanics. Go beyond surface-level tips and examine protocol-level traffic analysis as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong network behavior balances **visibility, accuracy, performance, cost, and legal restraint**. Show how these principles apply differently to single-flow debugging, proxy-fleet monitoring, and continuous collection oversight. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how connection use differs across versions, from one-request-at-a-time through multiplexed streams to QUIC datagrams

Teach how to confirm the negotiated version per origin with ALPN output and header evidence

Teach how multiplexing, flow control, and prioritization interact, and where head-of-line blocking survives

Teach how to tune per-host concurrency and stream priority so clients are fast without being abusive

Teach how to diagnose fallback faults where middleboxes or servers silently downgrade versions

Include practical methods for real projects. Cover:

* ALPN capture per origin
* Version census across target lists
* Waterfall multiplexing reads
* Concurrency ladders per version
* Priority assignment for heroes
* Fallback detection drills
* Middlebox interference checks
* Politeness caps per version

Explain how practitioners can avoid h2 waterfall looks serial (server ignores priorities or client opens many connections).
Explain how practitioners can avoid h3 works direct, fails via proxy (proxy lacks udp/quic support or strips alt-svc).
Explain how practitioners can avoid higher concurrency slows everything (past the knee into loss or server queueing).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover R, E, S, T,  , a, n, d,  , G, r, a, p, h, Q, L,  , A, P, I, s, ,,  , p, a, g, i, n, a, t, e, d,  , l, i, s, t, i, n, g, s, ,,  , a, u, t, h, e, n, t, i, c, a, t, e, d,  , f, e, e, d, s, ,,  , s, t, r, e, a, m, i, n, g,  , e, n, d, p, o, i, n, t, s, ,,  , a, n, d,  , g, e, o, -, d, i, s, t, r, i, b, u, t, e, d,  , t, a, r, g, e, t, s. Keep examples focused on network behavior rather than generic advice.

Include practical exercises that require the learner to:

1. Census versions across 20 targets and chart the mix.
2. Prove multiplexing on one HTTP/2 origin with a waterfall.
3. Ladder concurrency 1 to 16 and find the knee per version.
4. Detect a silent downgrade and name the interfering layer.
5. Prioritize hero requests and measure the paint delta.
6. Write per-version concurrency policy for one fleet.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from TCP/IP, UDP, TLS, HTTP versions, DNS, proxies, and traffic analysis where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize IETF RFCs, Wireshark and tshark documentation, vendor protocol guides, measurement research, and mitmproxy and proxy-server official docs. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **version-census checklist**, a **multiplex-proof checklist**, a **concurrency-ladder checklist**, a **fallback-drill checklist**, a **policy-table checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
