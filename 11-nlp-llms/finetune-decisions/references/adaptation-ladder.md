# Adaptation Ladder

Ladder: prompt engineering (days, $) for instruction-following gaps; RAG (weeks, $$) for knowledge gaps; PEFT/LoRA (weeks, $$$) for style/format/domain priors; full fine-tune (months, $$$$) rarely; distillation for cost after teacher proven. Climb only on pilot wins.

Pilots: 500+ curated pairs, 1-3 epochs PEFT, eval vs prompt-baseline AND RAG on same suite; gates: +5 judged points minimum to climb; ablate (size halves, quality tiers) to prove data value. Stop rules written before tuning.

Curation: rubric (correctness, style, diversity, difficulty); dedupe near-identical; balance classes/intents; PII-scrubbed; licensed/owned; 10 percent held for eval. Quality beats quantity 10:1 — prove with ablations.

Decisions: memo with lift, cost (train + serve), risk (regression, forgetting, safety re-eval), and recommendation; safety suite re-run post-tune; version data+config+eval together; ship or explicitly stop.
