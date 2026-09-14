# Grounded RAG

Pipeline: query rewrite (light) -> hybrid retrieve (dense + BM25, filters pre-applied) top-50 -> rerank to 5 -> generate with cite-every-claim instructions -> citation verify (resolve + support check) -> serve or abstain. Log each stage.

Citations: inline [n] per factual sentence bound to chunk ids; verifier checks chunk contains claim (entailment-ish or exact-span); unsupported claims trigger regen-once then abstain. Citation precision/recall reported.

Abstention: explicit 'not in sources' response when top contexts score below threshold or conflict unresolved; log and review weekly; tune threshold on judged edge cases. Never fill gaps from parametric memory silently.

Eval: 50+ judged QA (answerable, unanswerable, conflicting, stale, permissioned); metrics recall@5, citation precision/recall, faithfulness (supported claims / total), abstention correctness; fix top failure class monthly; freshness SLA on index.
