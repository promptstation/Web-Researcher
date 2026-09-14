# Normalization Rules

Formatting: indent by brace depth ignoring braces inside strings, templates, comments, and regex literals; split on semicolons and braces outside those contexts; preserve ASI hazards by never joining lines that change meaning. Verify by string-hash comparison pre/post.

Escapes: decode \uXXXX and \xXX to literal characters for review copies only; keep originals byte-identical; unify quotes only where semantics cannot change. Log counts per class.

Unwrapping: eval-packed layers decode by running the packer's own decoder logic reimplemented statically, never by eval. Validate output starts with plausible JS and re-triage; layered packs peel one at a time with baselines between.

Baselines: sha256 every input and output; store with tool name plus version; later passes diff against baselines, never against shifting formatted copies.
