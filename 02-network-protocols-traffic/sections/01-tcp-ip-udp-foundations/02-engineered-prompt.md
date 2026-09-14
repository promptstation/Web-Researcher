# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 02 Network Protocols & Traffic Analysis → Section: TCP/IP and UDP Foundations for Scrapers

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“TCP/IP and UDP Foundations for Scrapers”** as part of an advanced course in network protocols, packet analysis, and scraping traffic operations. How IP routing, TCP handshakes, retransmission, windowing, and UDP datagrams shape scraping reliability, how to read connection setup cost in timings, and how to choose timeouts, retries, and parallelism that respect transport behavior.

The material should teach how to diagnose transport behavior from timing evidence and configure timeouts that match path reality. Go beyond surface-level tips and examine protocol-level traffic analysis as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong network behavior balances **visibility, accuracy, performance, cost, and legal restraint**. Show how these principles apply differently to single-flow debugging, proxy-fleet monitoring, and continuous collection oversight. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to trace TCP setup and teardown and attribute each phase's cost in connect timings

Teach how to read retransmission, window exhaustion, and RTT inflation from latency distributions

Teach how to choose TCP versus UDP transports based on reliability needs, using DNS and QUIC as worked contrasts

Teach how to set connect, read, and total timeouts from measured percentiles instead of defaults

Teach how to separate transport faults from TLS, HTTP, and application faults with a layered elimination order

Include practical methods for real projects. Cover:

* Connect-timing splits per host
* DNS versus TCP versus TLS attribution
* RTT percentile baselines
* Timeout derivation from p95 plus margin
* Retransmission symptom reading
* Keep-alive and reuse tuning
* Parallelism caps per path
* Fault-layer elimination order

Explain how practitioners can avoid connect hangs then succeeds in bursts (dns stalls or syn throttling on the path).
Explain how practitioners can avoid high latency only through proxy (egress congestion or distant exit nodes).
Explain how practitioners can avoid timeouts cluster at one hour (target deploy windows or rate shaping by time).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover R, E, S, T,  , a, n, d,  , G, r, a, p, h, Q, L,  , A, P, I, s, ,,  , p, a, g, i, n, a, t, e, d,  , l, i, s, t, i, n, g, s, ,,  , a, u, t, h, e, n, t, i, c, a, t, e, d,  , f, e, e, d, s, ,,  , s, t, r, e, a, m, i, n, g,  , e, n, d, p, o, i, n, t, s, ,,  , a, n, d,  , g, e, o, -, d, i, s, t, r, i, b, u, t, e, d,  , t, a, r, g, e, t, s. Keep examples focused on network behavior rather than generic advice.

Include practical exercises that require the learner to:

1. Split fetch latency into DNS, connect, TLS, and wait for five hosts.
2. Derive timeouts from 100 samples and justify each value.
3. Distinguish a retransmitting path from a slow server with evidence.
4. Tune keep-alive and show connection-reuse delta.
5. Write a transport-fault elimination checklist and test it on one failure.
6. Document a per-host timeout table for a scraping fleet.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from TCP/IP, UDP, TLS, HTTP versions, DNS, proxies, and traffic analysis where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize IETF RFCs, Wireshark and tshark documentation, vendor protocol guides, measurement research, and mitmproxy and proxy-server official docs. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **timing-splits checklist**, a **timeout-table checklist**, a **fault-layering checklist**, a **reuse-tuning checklist**, a **baseline-record checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
