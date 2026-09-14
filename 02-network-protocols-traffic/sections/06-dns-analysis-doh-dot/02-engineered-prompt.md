# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 02 Network Protocols & Traffic Analysis → Section: DNS Analysis: Resolution, DoH and DoT

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“DNS Analysis: Resolution, DoH and DoT”** as part of an advanced course in network protocols, packet analysis, and scraping traffic operations. How recursive and authoritative resolution works, how to trace delegations and record sets, how DNS-over-HTTPS and DNS-over-TLS change privacy and debugging, and how to diagnose resolution faults that stall scraping fleets.

The material should teach how to diagnose DNS behavior from query evidence and harden resolver choices. Go beyond surface-level tips and examine protocol-level traffic analysis as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong network behavior balances **visibility, accuracy, performance, cost, and legal restraint**. Show how these principles apply differently to single-flow debugging, proxy-fleet monitoring, and continuous collection oversight. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to trace a query from stub resolver through recursive to authoritative servers with each hop named

Teach how to read record sets and spot CNAME chains, stale glue, and missing IPv6 answers

Teach how to audit TTLs so caching helps freshness instead of serving stale targets

Teach how DoH and DoT change who sees queries and how debugging moves to new endpoints

Teach how to diagnose resolver outages, lame delegations, and DNSSEC failures with elimination steps

Include practical methods for real projects. Cover:

* Delegation tracing per domain
* Record-set inventories
* TTL and cache audits
* Resolver comparisons
* DoH endpoint checks
* Propagation verification
* Lame-delegation detection
* Fleet resolver policy

Explain how practitioners can avoid servfail on one resolver only (dnssec validation or lame delegation visible there).
Explain how practitioners can avoid stale answers after change (long ttls cached at recursive or app level).
Explain how practitioners can avoid doh works, classic fails (port 53 blocked or hijacked on path).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover R, E, S, T,  , a, n, d,  , G, r, a, p, h, Q, L,  , A, P, I, s, ,,  , p, a, g, i, n, a, t, e, d,  , l, i, s, t, i, n, g, s, ,,  , a, u, t, h, e, n, t, i, c, a, t, e, d,  , f, e, e, d, s, ,,  , s, t, r, e, a, m, i, n, g,  , e, n, d, p, o, i, n, t, s, ,,  , a, n, d,  , g, e, o, -, d, i, s, t, r, i, b, u, t, e, d,  , t, a, r, g, e, t, s. Keep examples focused on network behavior rather than generic advice.

Include practical exercises that require the learner to:

1. Trace delegation for three domains and diagram each chain.
2. Inventory records for one target and flag risks.
3. Compare three resolvers on latency and correctness.
4. Verify a DoH endpoint end to end.
5. Diagnose one lame delegation with proof.
6. Write resolver policy for a scraping fleet.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from TCP/IP, UDP, TLS, HTTP versions, DNS, proxies, and traffic analysis where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize IETF RFCs, Wireshark and tshark documentation, vendor protocol guides, measurement research, and mitmproxy and proxy-server official docs. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **delegation-trace checklist**, a **record-inventory checklist**, a **ttl-audit checklist**, a **resolver-compare checklist**, a **fleet-policy checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
