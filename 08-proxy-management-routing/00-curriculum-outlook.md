# Course 08 — Proxy Management & Network Routing
## Curriculum Content Outlook (Researching-Outline workflow, compressed to ≤15 sections)

Source course list: `Web researcher and scrapper.txt` — Course 8: Proxy Management & Network Routing
Method: Researching-Outline.md workflow (Steps 1–8) + beginner→expert progression research + compression into groups.
Sections: 10 (within the ≤15 limit). Each section = Summary (what it teaches) + Absorbed Skill (capability gained).

---

**Proxy Types and Selection**

**Summary:** How datacenter, residential, ISP, and mobile proxies differ in trust, cost, and stability, how protocols and auth modes constrain design, and how to select providers with trials and scorecards.

**Absorbed Skill:** Select proxy types and providers with trials, scorecards, and honest tradeoff math.

---

**Pool Operations and Rotation**

**Summary:** How to operate proxy pools with rotation policies, session control, concurrency per egress, quarantine, and warm spares so throughput stays high and bans stay low.

**Absorbed Skill:** Operate proxy pools with sound rotation, session control, and quarantine.

---

**Sticky Sessions and Identity Pinning**

**Summary:** How session affinity, account-to-egress pinning, cookie persistence, and checkout-safe flows keep multi-step and authenticated journeys coherent across requests.

**Absorbed Skill:** Keep multi-step journeys coherent with affinity, pinning, and checkout-safe flows.

---

**Geo-Targeting and Exit Verification**

**Summary:** How to target countries, regions, and cities honestly for legitimate localization testing, how to verify exit geo, ASN, and rDNS, and how to detect drift and mismatches.

**Absorbed Skill:** Target and verify egress geography with measured proof for legitimate localization.

---

**Health Scoring and Quarantine**

**Summary:** How to score egress health from success, latency, bans, and drift, how to set trip thresholds, and how to run quarantine lifecycles with canary recovery.

**Absorbed Skill:** Score egress health continuously and run quarantine lifecycles with canary recovery.

---

**Cost Control and Budgets**

**Summary:** How to attribute proxy spend by pool, target, and team, how to set unit-cost budgets and alerts, and how to cut cost with type right-sizing, caching, and retry discipline.

**Absorbed Skill:** Control egress spend with attribution, unit budgets, and disciplined savings.

---

**Auth, Rotation and Secret Handling**

**Summary:** How to authenticate proxies with allowlists and rotated credentials, how to store and inject secrets safely, and how to rotate without downtime or leaks.

**Absorbed Skill:** Authenticate egress securely with vaulted secrets and zero-downtime rotation.

---

**Routing Policies and Failover**

**Summary:** How to route requests across pools by target class, geography, cost, and health, how to fail over automatically, and how to keep routing decisions observable and auditable.

**Absorbed Skill:** Route egress by policy with automatic failover and full observability.

---

**Compliance and Acceptable Use**

**Summary:** How provider terms, target terms, data laws, and export controls constrain egress operations, how to document lawful basis per flow, and how to audit and enforce acceptable use.

**Absorbed Skill:** Operate egress within provider terms, target terms, and data law with auditable proof.

---

**Incident Response for Egress**

**Summary:** How to detect, triage, contain, and recover from egress incidents — ban waves, provider outages, credential leaks, and compliance breaches — with runbooks, comms, and postmortems.

**Absorbed Skill:** Respond to egress incidents with fast containment, clean recovery, and learning.
