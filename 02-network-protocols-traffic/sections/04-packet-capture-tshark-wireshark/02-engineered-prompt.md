# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 02 Network Protocols & Traffic Analysis → Section: Packet Capture with tcpdump, tshark and Wireshark

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Packet Capture with tcpdump, tshark and Wireshark”** as part of an advanced course in network protocols, packet analysis, and scraping traffic operations. How to plan captures with precise BPF filters, record with tcpdump or dumpcap, analyze with tshark and Wireshark display filters, follow streams, and extract evidence without drowning in packets or mishandling sensitive payloads.

The material should teach how to capture network evidence precisely and analyze streams to verdicts. Go beyond surface-level tips and examine protocol-level traffic analysis as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong network behavior balances **visibility, accuracy, performance, cost, and legal restraint**. Show how these principles apply differently to single-flow debugging, proxy-fleet monitoring, and continuous collection oversight. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to write BPF capture filters that collect the flow of interest and nothing else

Teach how to record with snaplen, ring buffers, and rotation so captures stay small and complete

Teach how to analyze with display filters, IO graphs, and conversation statistics instead of scrolling packets

Teach how to follow streams across TCP, TLS, HTTP/2, WebSocket, and QUIC dissectors

Teach how to extract files, keys logs, and transcripts with redaction and retention discipline

Include practical methods for real projects. Cover:

* Capture planning worksheets
* BPF filter patterns per task
* Rotation and ring-buffer setups
* Display-filter recipes
* Stream-following protocol
* Decryption with key logs (owned traffic only)
* Evidence extraction checklists
* Payload redaction rules

Explain how practitioners can avoid capture misses packets (snaplen trimming, buffer drops, or wi-fi monitor gaps).
Explain how practitioners can avoid tls indecipherable (no key log or forward-secret session without keys).
Explain how practitioners can avoid filter catches nothing (wrong interface, vlan tags, or tunnel encapsulation).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover R, E, S, T,  , a, n, d,  , G, r, a, p, h, Q, L,  , A, P, I, s, ,,  , p, a, g, i, n, a, t, e, d,  , l, i, s, t, i, n, g, s, ,,  , a, u, t, h, e, n, t, i, c, a, t, e, d,  , f, e, e, d, s, ,,  , s, t, r, e, a, m, i, n, g,  , e, n, d, p, o, i, n, t, s, ,,  , a, n, d,  , g, e, o, -, d, i, s, t, r, i, b, u, t, e, d,  , t, a, r, g, e, t, s. Keep examples focused on network behavior rather than generic advice.

Include practical exercises that require the learner to:

1. Write BPF filters for five scraping-debug scenarios.
2. Capture one login flow under 5MB with full evidence.
3. Follow a TLS stream and map its HTTP/2 frames.
4. Build an IO graph that proves a retransmission fault.
5. Extract one file from a capture with hashes.
6. Redact a capture for sharing without losing the finding.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from TCP/IP, UDP, TLS, HTTP versions, DNS, proxies, and traffic analysis where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize IETF RFCs, Wireshark and tshark documentation, vendor protocol guides, measurement research, and mitmproxy and proxy-server official docs. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **capture-plan checklist**, a **filter-precision checklist**, a **stream-proof checklist**, a **evidence-extract checklist**, a **redaction-pass checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
