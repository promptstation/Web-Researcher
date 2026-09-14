# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 08 Proxy Management & Network Routing → Section: Auth, Rotation and Secret Handling

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Auth, Rotation and Secret Handling”** as part of an advanced course in proxy management, egress routing, and compliant traffic operations. How to authenticate proxies with allowlists and rotated credentials, how to store and inject secrets safely, and how to rotate without downtime or leaks.

The material should teach how to handle proxy authentication and secrets securely. Go beyond surface-level tips and examine egress operations as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong egress health balances **success rate, cost, compliance, latency, and resilience**. Show how these principles apply differently to single proxies, multi-pool fleets, and global egress programs. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to prefer IP allowlists where possible and scope them tightly

Teach how to vault proxy credentials with least-privilege access

Teach how to rotate credentials with dual-validity windows and zero downtime

Teach how to inject secrets at runtime without touching disk, logs, or images

Teach how to audit secret handling with scans and rotation drills

Include practical methods for real projects. Cover:

* Auth selection
* Allowlist scoping
* Vault design
* Dual-validity rotation
* Runtime injection
* Leak scanning
* Rotation drills
* Access reviews

Explain how practitioners can avoid auth failures after rotation (stale worker or missed scope).
Explain how practitioners can avoid allowlist too broad (ranges instead of hosts).
Explain how practitioners can avoid secrets in artifacts (debug logs or traces capture).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover g, e, o, -, l, o, c, k, e, d,  , c, a, t, a, l, o, g, s, ,,  , r, e, g, i, o, n, a, l,  , s, e, a, r, c, h, ,,  , l, o, c, a, l, i, z, e, d,  , p, r, i, c, i, n, g, ,,  , m, u, l, t, i, -, a, c, c, o, u, n, t,  , p, o, r, t, a, l, s, ,,  , a, n, d,  , c, o, m, p, l, i, a, n, c, e, -, s, c, o, p, e, d,  , c, o, l, l, e, c, t, i, o, n, s. Keep examples focused on egress health rather than generic advice.

Include practical exercises that require the learner to:

1. Scope one allowlist tightly.
2. Vault one credential set.
3. Rotate with zero downtime.
4. Inject at runtime cleanly.
5. Scan one repo for leaks.
6. Drill one emergency rotation.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from pools, rotation, affinity, health scoring, and routing policy where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize proxy provider docs, routing and network references, and compliance frameworks. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **allowed-tight checklist**, a **vaulted-all checklist**, a **rotated-clean checklist**, a **injected-runtime checklist**, a **scanned-zero checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
