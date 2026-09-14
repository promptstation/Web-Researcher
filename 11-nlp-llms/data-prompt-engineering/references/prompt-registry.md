# Prompt Registry

Card anatomy: task, version, model pin, instructions (role/task/constraints/format/edges), few-shots with rationale, output contract, eval suite link, thresholds, changelog. One file per prompt version; registry index; rollback = previous file.

Few-shots: one per class minimum plus 2-4 edge cases (negation, missing info, adversarial, long/short); diverse styles; order fixed (recency bias: hardest last); document why each earns its tokens. 4-12 shots typical.

Constraining: labels exact-match (normalize case/space, reject others); enums closed; JSON schema for structure; temperature 0 for data tasks; max-tokens capped; parse strictly with repair-once. Log raw outputs for audits.

Gates: eval suite 100+ with per-class floors; new version must beat current on suite (or tie cheaper); A/B on live sample for risky changes; changelog entry; rollback tested. Cost per 1k tracked per version.
