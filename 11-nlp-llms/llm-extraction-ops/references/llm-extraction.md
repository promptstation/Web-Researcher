# LLM Extraction

Schema-first: JSON schema with types, enums, required, and descriptions per field; prompt instructs exact schema, no extra keys, quotes for values; use structured-output modes where available. Version prompt+schema together.

Validation: JSON parse -> schema check -> business rules (ranges, enums, cross-field, source-grounding for risky fields); repair retry once with error feedback; escalate model once; then quarantine coded. Track valid-first-try rate.

Eval: 100+ gold records; per-field precision/recall/F1; exact-match for IDs/dates/money, normalized-match for names; adversarial golds (negations, missing info, distractors); fix worst field first. Report macro and worst.

Cost: route easy (short, clean) to small models, hard to large; cache by content hash; batch; cap context (relevant excerpts, not whole docs); cost per 1k records tracked; human review band (low-confidence + critical fields) with SLA.
