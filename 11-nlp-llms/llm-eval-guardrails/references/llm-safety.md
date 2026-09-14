# LLM Safety

Threats: prompt injection (direct/indirect via retrieved content), jailbreaks, PII regurgitation, tool abuse, data exfiltration via outputs. Model per feature; tier by data sensitivity and tool power; suite 100+ adversarial minimum for connected features.

PII: patterns per locale (email, phone, card, ID, address); scrub inputs (retrieval + user) and outputs; plant-PII tests verify; counts logged; quarantine on scrub failure for sensitive flows. PII never in prompts to third parties without basis.

Injection defense: system/user/content boundaries; retrieved content marked untrusted; tools allowlisted with least privilege and confirmation for side effects; output validators (schema, policy, citation); indirect-injection tests from poisoned docs.

Launch: all criticals fixed, highs triaged; human review band for high-stakes; monitoring (attack patterns, scrub counts, policy hits); incident runbook + yearly drill; re-test every model/prompt/tool change.
