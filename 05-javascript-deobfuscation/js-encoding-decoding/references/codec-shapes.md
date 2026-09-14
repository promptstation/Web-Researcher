# Codec Shapes

Shape guide: base64 shows A-Za-z0-9+/ with = padding and length mod 4; hex shows 0-9a-f pairs; XOR blobs show high entropy with single-byte structure; RC4 outputs look random until keyed; custom alphabets reveal via char-set histograms.

XOR: score candidates by English letter frequency plus space rate; single-byte first, then repeating-key lengths 2-32 with Hamming distance ranking. RC4: standard KSA+PRGA, plus skip-256/512/1024 variants and key-xor tweaks; try key encodings utf8, hex, base64.

Key harvesting: literals adjacent to decoder calls, array entries referenced once, URL params, cookie values. Verify by decoding to known markers (http, function, var).

Chaining: outermost first, verify readability each layer, stop at parseable JS or plain config. Treat recovered secrets as sensitive evidence with handling notes.
