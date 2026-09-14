# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 02 Network Protocols & Traffic Analysis → Section: Latency, Bandwidth and Congestion Diagnostics

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Latency, Bandwidth and Congestion Diagnostics”** as part of an advanced course in network protocols, packet analysis, and scraping traffic operations. How to measure path latency, usable bandwidth, loss, and jitter, how congestion control shapes scraping throughput, and how to set parallelism and pacing that respect shared paths and target capacity.

The material should teach how to diagnose path performance and pace collection within measured budgets. Go beyond surface-level tips and examine protocol-level traffic analysis as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong network behavior balances **visibility, accuracy, performance, cost, and legal restraint**. Show how these principles apply differently to single-flow debugging, proxy-fleet monitoring, and continuous collection oversight. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to measure RTT, loss, and jitter per path with repeated probes and percentile summaries

Teach how to estimate usable bandwidth without abusive floods, using paced transfers and timing math

Teach how congestion control and buffering shape scraping throughput on long or lossy paths

Teach how to set per-host pacing from the tighter of path budget and target politeness budget

Teach how to detect shaping and deprioritization from time-of-day and size-dependent patterns

Include practical methods for real projects. Cover:

* Probe design per path
* Percentile reporting
* Bandwidth estimation protocol
* Loss isolation steps
* Bufferbloat checks
* Pacing derivation
* Shaping detection
* Budget publishing

Explain how practitioners can avoid jitter spikes randomly (bufferbloat or competing bulk flows).
Explain how practitioners can avoid bandwidth varies wildly (shared egress contention or server-side pacing).
Explain how practitioners can avoid loss only on large transfers (mtu or middlebox size sensitivity).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover R, E, S, T,  , a, n, d,  , G, r, a, p, h, Q, L,  , A, P, I, s, ,,  , p, a, g, i, n, a, t, e, d,  , l, i, s, t, i, n, g, s, ,,  , a, u, t, h, e, n, t, i, c, a, t, e, d,  , f, e, e, d, s, ,,  , s, t, r, e, a, m, i, n, g,  , e, n, d, p, o, i, n, t, s, ,,  , a, n, d,  , g, e, o, -, d, i, s, t, r, i, b, u, t, e, d,  , t, a, r, g, e, t, s. Keep examples focused on network behavior rather than generic advice.

Include practical exercises that require the learner to:

1. Baseline three paths with RTT, loss, and jitter stats.
2. Estimate bandwidth for one path without flooding.
3. Prove a throughput ceiling is congestion, not server.
4. Derive pacing for one host class from budgets.
5. Detect one shaping pattern with time-of-day proof.
6. Publish path budgets for a fleet.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from TCP/IP, UDP, TLS, HTTP versions, DNS, proxies, and traffic analysis where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize IETF RFCs, Wireshark and tshark documentation, vendor protocol guides, measurement research, and mitmproxy and proxy-server official docs. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **path-baseline checklist**, a **bandwidth-estimate checklist**, a **ceiling-proof checklist**, a **pacing-table checklist**, a **shaping-watch checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
