# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 02 Network Protocols & Traffic Analysis → Section: WebSocket and Streaming Protocols

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“WebSocket and Streaming Protocols”** as part of an advanced course in network protocols, packet analysis, and scraping traffic operations. How HTTP upgrades to WebSocket, how frames, masking, pings, and backpressure work, how Server-Sent Events and chunked streams differ, and how to debug drops, stalls, and reconnect storms in scraping and monitoring clients.

The material should teach how to debug streaming transports from frame evidence and engineer calm reconnects. Go beyond surface-level tips and examine protocol-level traffic analysis as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong network behavior balances **visibility, accuracy, performance, cost, and legal restraint**. Show how these principles apply differently to single-flow debugging, proxy-fleet monitoring, and continuous collection oversight. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to trace the upgrade handshake and name each header's role in the switch

Teach how to parse frames by opcode, length encoding, and masking, including fragmented messages

Teach how to choose between WebSocket, SSE, chunked responses, and polling based on direction and scale

Teach how to diagnose drops and stalls from ping gaps, close codes, and consumer lag

Teach how to build reconnects with backoff, jitter, resume tokens, and server-friendly limits

Include practical methods for real projects. Cover:

* Handshake verification
* Frame parsing drills
* Close-code reading
* Ping-gap monitoring
* Consumer-lag measurement
* Transport comparison tables
* Reconnect policy design
* Storm drills

Explain how practitioners can avoid handshake 400s on one path (missing headers, bad key, or proxy stripping upgrade).
Explain how practitioners can avoid messages delayed in bursts (nagle, buffering proxies, or slow consumer).
Explain how practitioners can avoid resume duplicates data (no idempotency on replayed messages).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover R, E, S, T,  , a, n, d,  , G, r, a, p, h, Q, L,  , A, P, I, s, ,,  , p, a, g, i, n, a, t, e, d,  , l, i, s, t, i, n, g, s, ,,  , a, u, t, h, e, n, t, i, c, a, t, e, d,  , f, e, e, d, s, ,,  , s, t, r, e, a, m, i, n, g,  , e, n, d, p, o, i, n, t, s, ,,  , a, n, d,  , g, e, o, -, d, i, s, t, r, i, b, u, t, e, d,  , t, a, r, g, e, t, s. Keep examples focused on network behavior rather than generic advice.

Include practical exercises that require the learner to:

1. Verify one upgrade handshake header by header.
2. Decode a fragmented masked message by hand.
3. Compare three transports for one feed and pick with reasons.
4. Diagnose one stall from ping gaps.
5. Write a reconnect policy and storm-test it.
6. Monitor one stream for a week with close-code stats.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from TCP/IP, UDP, TLS, HTTP versions, DNS, proxies, and traffic analysis where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize IETF RFCs, Wireshark and tshark documentation, vendor protocol guides, measurement research, and mitmproxy and proxy-server official docs. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **handshake-verify checklist**, a **frame-drill checklist**, a **transport-pick checklist**, a **reconnect-policy checklist**, a **stream-watch checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
