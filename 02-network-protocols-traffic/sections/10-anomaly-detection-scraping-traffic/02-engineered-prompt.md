# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 02 Network Protocols & Traffic Analysis → Section: Anomaly Detection in Scraping Traffic

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Anomaly Detection in Scraping Traffic”** as part of an advanced course in network protocols, packet analysis, and scraping traffic operations. How to baseline scraping traffic by rate, status mix, latency, and challenge signals, how to detect ban waves, layout drift, proxy decay, and cost spikes early, and how to respond with playbooks instead of panic.

The material should teach how to detect collection anomalies early and respond with verified playbooks. Go beyond surface-level tips and examine protocol-level traffic analysis as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong network behavior balances **visibility, accuracy, performance, cost, and legal restraint**. Show how these principles apply differently to single-flow debugging, proxy-fleet monitoring, and continuous collection oversight. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to baseline traffic across rate, status mix, latency percentiles, challenge rates, and cost per thousand pages

Teach how to set alert thresholds from measured distributions with hysteresis so pages stay meaningful

Teach how to correlate signals so single-metric noise does not page while multi-signal shifts do

Teach how to classify ban waves, layout drift, proxy decay, and cost spikes from signature tables

Teach how to execute response playbooks with explicit steps and verify recovery against baselines

Include practical methods for real projects. Cover:

* Metric inventory per domain
* Baseline windows and seasons
* Threshold derivation
* Hysteresis and cooldowns
* Signature tables per incident class
* Correlation rules
* Playbook library
* Recovery verification

Explain how practitioners can avoid alerts flap constantly (thresholds without hysteresis on noisy signals).
Explain how practitioners can avoid incident missed by alerts (unbaselined signal or holiday-season drift).
Explain how practitioners can avoid recovery claimed too early (single green sample after fix).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover R, E, S, T,  , a, n, d,  , G, r, a, p, h, Q, L,  , A, P, I, s, ,,  , p, a, g, i, n, a, t, e, d,  , l, i, s, t, i, n, g, s, ,,  , a, u, t, h, e, n, t, i, c, a, t, e, d,  , f, e, e, d, s, ,,  , s, t, r, e, a, m, i, n, g,  , e, n, d, p, o, i, n, t, s, ,,  , a, n, d,  , g, e, o, -, d, i, s, t, r, i, b, u, t, e, d,  , t, a, r, g, e, t, s. Keep examples focused on network behavior rather than generic advice.

Include practical exercises that require the learner to:

1. Baseline one domain across five signals for a week.
2. Derive thresholds with hysteresis for each signal.
3. Classify three past incidents from signatures.
4. Write a ban-wave playbook and drill it.
5. Correlate a proxy-decay event across signals.
6. Verify one recovery against baseline with charts.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from TCP/IP, UDP, TLS, HTTP versions, DNS, proxies, and traffic analysis where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize IETF RFCs, Wireshark and tshark documentation, vendor protocol guides, measurement research, and mitmproxy and proxy-server official docs. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **metric-inventory checklist**, a **baseline-week checklist**, a **threshold-table checklist**, a **playbook-drill checklist**, a **recovery-proof checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
