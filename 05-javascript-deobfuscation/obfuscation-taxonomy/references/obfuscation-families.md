# Obfuscation Families

Class guide: minified keeps semantics readable after formatting (webpack/terser boilerplate, meaningful strings); packed shows eval-wrapped payloads with small decoders (packer signatures, base62 alphabets); string-array obfuscation shows giant _0x arrays with rotation IIFEs and hex identifiers; control-flow flattening shows dispatcher loops with switch cases; exotic encodings show only few distinct characters (jsfuck-style) or pure unicode escapes.

Signal scoring: entropy over 5.5 bits/char suggests packing or encryption; identifier randomness over 70 percent hex-like suggests mangling; string-array over 100 entries with rotation loop is near-diagnostic; debugger and date-trap density flags anti-analysis.

Routing: minified -> beautify; packed -> unpack then re-triage; string-array -> decode arrays first; flattened -> simplify dispatchers; exotic -> normalize encoding first. Dynamic sandbox only after static understanding and always isolated.

Safety: hash (sha256) and archive originals; work on copies; never open in browsers with network; detonate suspicious samples in VMs without host shares.
