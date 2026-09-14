# Rename Rules

Scoping: rename within the narrowest declaring scope; qualify with function names when flattened; never merge names across scopes. Role naming: counters get i/j/k, strings get sN, decoders get decodeN, stores get storeN, flags get flagN, unknowns keep indexed temporaries.

Determinism: sort identifiers before numbering; seed from file hash plus rule version; identical inputs must byte-ident outputs. Prove by double-run diffing.

Inlining: only single-use, side-effect-free aliases; count uses textually then confirm semantically; keep the original assignment in a comment for one review cycle. Folding: literals and provable expressions only; never fold Date, random, or environment reads.

Stability: freeze rule versions; record tool plus version with outputs; diffs across builds use identical rules or say so loudly.
