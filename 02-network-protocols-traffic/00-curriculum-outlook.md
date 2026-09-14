# Course 02 — Network Protocols & Traffic Analysis
## Curriculum Content Outlook (Researching-Outline workflow, compressed to ≤15 sections)

Source course list: `Web researcher and scrapper.txt` — Course 2: Network Protocols & Traffic Analysis
Method: Researching-Outline.md workflow (Steps 1–8) + beginner→expert progression research + compression into groups.
Sections: 10 (within the ≤15 limit). Each section = Summary (what it teaches) + Absorbed Skill (capability gained).

---

**TCP/IP and UDP Foundations for Scrapers**

**Summary:** How IP routing, TCP handshakes, retransmission, windowing, and UDP datagrams shape scraping reliability, how to read connection setup cost in timings, and how to choose timeouts, retries, and parallelism that respect transport behavior.

**Absorbed Skill:** Explain transport-layer behavior from timing evidence, set timeouts and retries that match path reality, and separate network faults from application faults.

---

**HTTP Versions: 1.1, 2 and 3 in Practice**

**Summary:** How HTTP/1.1 keep-alive and pipelining limits, HTTP/2 multiplexing and prioritization, and HTTP/3 QUIC streams behave on real targets, how to confirm negotiated versions, and how to shape client behavior per version for speed and politeness.

**Absorbed Skill:** Confirm negotiated HTTP versions, explain multiplexing and prioritization effects, and tune client concurrency and prioritization per version.

---

**TLS Fingerprinting and Client Profiles**

**Summary:** How ClientHello fields (versions, ciphers, extensions, curves, ALPN) fingerprint TLS clients, how JA3-style hashes summarize handshakes, how to audit your own client profile, and how to interpret server-side TLS decisions for research and defense.

**Absorbed Skill:** Explain TLS fingerprint inputs, audit local client profiles, and interpret handshake outcomes for research consistency and defense.

---

**Packet Capture with tcpdump, tshark and Wireshark**

**Summary:** How to plan captures with precise BPF filters, record with tcpdump or dumpcap, analyze with tshark and Wireshark display filters, follow streams, and extract evidence without drowning in packets or mishandling sensitive payloads.

**Absorbed Skill:** Plan minimal captures, record cleanly, analyze with display filters and stream following, and extract evidence with payload hygiene.

---

**Proxy Protocols: HTTP, SOCKS and Tunnels**

**Summary:** How HTTP forward proxies, CONNECT tunneling, SOCKS4/5 handshakes, and modern tunnels compare, how to verify chains hop by hop, and how to choose and test egress for scraping fleets without leaking DNS or credentials.

**Absorbed Skill:** Explain proxy protocol mechanics, verify chains hop by hop, and select egress that preserves DNS privacy and credential safety.

---

**DNS Analysis: Resolution, DoH and DoT**

**Summary:** How recursive and authoritative resolution works, how to trace delegations and record sets, how DNS-over-HTTPS and DNS-over-TLS change privacy and debugging, and how to diagnose resolution faults that stall scraping fleets.

**Absorbed Skill:** Trace DNS resolution end to end, audit record sets and TTLs, and diagnose resolver, delegation, and encryption faults.

---

**Traffic Interception with mitmproxy**

**Summary:** How to run mitmproxy for owned test traffic: CA install, upstream modes, addon scripting for logging and modification, and evidence handling, with strict scope so interception never touches traffic you are not authorized to inspect.

**Absorbed Skill:** Operate mitmproxy on authorized test traffic to log, modify, and replay flows with scripted addons and clean evidence.

---

**WebSocket and Streaming Protocols**

**Summary:** How HTTP upgrades to WebSocket, how frames, masking, pings, and backpressure work, how Server-Sent Events and chunked streams differ, and how to debug drops, stalls, and reconnect storms in scraping and monitoring clients.

**Absorbed Skill:** Explain upgrade and framing, debug drops and stalls from frame evidence, and build reconnect logic without storms.

---

**Latency, Bandwidth and Congestion Diagnostics**

**Summary:** How to measure path latency, usable bandwidth, loss, and jitter, how congestion control shapes scraping throughput, and how to set parallelism and pacing that respect shared paths and target capacity.

**Absorbed Skill:** Measure path quality with percentiles, explain throughput ceilings, and pace scraping fleets within path and target budgets.

---

**Anomaly Detection in Scraping Traffic**

**Summary:** How to baseline scraping traffic by rate, status mix, latency, and challenge signals, how to detect ban waves, layout drift, proxy decay, and cost spikes early, and how to respond with playbooks instead of panic.

**Absorbed Skill:** Baseline collection traffic, detect multi-signal anomalies early, and execute response playbooks with measured recovery.
