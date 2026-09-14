# Step 2 — Engineered Prompt (Prompt Engineering.md workflow)
## Course 01 Browser Engineering → Section: Network Stack: DNS, TLS, HTTP/2/3 and Caching

The RESULT below is the engineered prompt. In Step 4 this RESULT becomes the task for building the SKILL.md.

---

RESULT:

Develop a comprehensive, professional-level learning module on **“Network Stack: DNS, TLS, HTTP/2/3 and Caching”** as part of an advanced course in browser engineering, rendering internals, and web runtime behavior. How browsers resolve, connect, secure, and multiplex fetches across HTTP/1.1, HTTP/2, and HTTP/3, how TLS handshakes, certificates, and ALPN negotiate security, and how memory, disk, and service-worker caches decide freshness without refetching.

The material should teach how to audit browser network behavior from handshake to cache hit and fix protocol and header faults. Go beyond surface-level tips and examine browser internals analysis as a disciplined practice in which every choice is observable, repeatable, and justified against evidence.

Explain how strong browser behavior balances **correctness, performance, compatibility, observability, and security**. Show how these principles apply differently to single-page debugging, fleet-wide scraping, and long-lived monitoring. Discuss how the techniques in this module compose into one coherent workflow rather than disconnected tricks.

Teach how to trace connection setup from DNS through TCP or QUIC, TLS handshake, and ALPN negotiation for one origin

Teach how multiplexing, prioritization, and head-of-line blocking differ across HTTP versions in waterfall evidence

Teach how to audit certificate chains, expiry, cipher suites, and minimum TLS versions with handshake output

Teach how to read Cache-Control, ETag, Last-Modified, and Vary so freshness and revalidation behave as intended

Teach how to fix redirect chains, missing HSTS, and cache-busting mistakes that multiply connection work

Include practical methods for real projects. Cover:

* Handshake capture: protocol, cipher, ALPN, cert chain
* Redirect chain mapping with timing per hop
* Waterfall multiplexing analysis per origin
* Cache header audit across asset classes
* HSTS and upgrade-insecure-requests review
* Preconnect and origin-consolidation planning
* Service-worker cache strategy selection
* Revalidation storm diagnosis

Explain how practitioners can avoid h2 shows no multiplexing win (origin sharding, uncoalesced connections, or server without priorities).
Explain how practitioners can avoid 304 storm on every navigation (validators forced on non-cacheable or private responses).
Explain how practitioners can avoid tls failure only through proxy (sni alteration, cert replacement, or alpn stripping by egress).

Use numerous realistic examples throughout the module. For each important principle, show weak, improved, and professional-level examples where useful. Examples should cover e, -, c, o, m, m, e, r, c, e,  , p, r, o, d, u, c, t,  , p, a, g, e, s, ,,  , n, e, w, s,  , a, r, t, i, c, l, e,  , t, e, m, p, l, a, t, e, s, ,,  , a, u, t, h, e, n, t, i, c, a, t, e, d,  , d, a, s, h, b, o, a, r, d, s, ,,  , s, i, n, g, l, e, -, p, a, g, e,  , a, p, p, l, i, c, a, t, i, o, n, s, ,,  , a, n, d,  , m, e, d, i, a, -, h, e, a, v, y,  , l, a, n, d, i, n, g,  , p, a, g, e, s. Keep examples focused on browser behavior rather than generic advice.

Include practical exercises that require the learner to:

1. Capture a full handshake for one HTTPS origin and label every phase cost.
2. Map a redirect chain and remove at least one hop with proof.
3. Prove whether an origin multiplexes correctly under HTTP/2 or falls back.
4. Audit cache headers for HTML, JS, CSS, images, and APIs; fix one class.
5. Diagnose a 304 storm and correct the validator configuration.
6. Write a cache strategy table a team can enforce in review.

For each exercise, provide the scenario, objective, constraints, expected deliverable, evaluation criteria, and an expert-quality example solution where appropriate.

Structure the material progressively, beginning with fundamentals and moving toward advanced professional practice. Establish clear conceptual distinctions before showing how concepts interact.

Use professional terminology from browser architecture, rendering pipelines, JavaScript runtimes, networking, and web security where relevant, but explain specialized terminology in clear language. Do not make the material sound like generic AI-generated advice.

Research the subject using high-quality professional and academic sources where external research materially strengthens the material. Prioritize Chromium design documentation, WHATWG and W3C specifications, V8 and WebKit engineering blogs, MDN Web Docs, and peer-reviewed web performance literature. Avoid relying primarily on low-quality SEO articles, content farms, or unsupported “best practice” claims.

Create a professional framework that a practitioner could actually use in a real project. The final material should therefore function simultaneously as a learning resource, practical reference, and working methodology.

Where a recommendation depends on context, explicitly explain the trade-off rather than presenting it as an absolute rule.

End the module with a **handshake-audit checklist**, a **redirect-map checklist**, a **multiplex-proof checklist**, a **cache-table checklist**, a **hsts-review checklist** that can be used by a professional team before work is approved for production.

The final result should be comprehensive enough to serve as an advanced professional training module, but organized clearly enough that a learner can study it progressively and apply each concept in practical work.
