# ClientHello Fields

Fingerprint inputs in order: TLS versions offered, cipher suite list and order, extensions list and order, elliptic curves, point formats, ALPN protocols, signature schemes, key shares, session ticket and PSK modes, compression and padding. JA3-style hashes join versions, ciphers, extensions, curves, and formats with delimiters; GREASE values are ignored by convention.

Stability facts: library upgrades reorder suites; OS changes alter curves; proxies may terminate and re-originate with their own profile; middleboxes can strip extensions. Re-baseline after every image, library, or egress change.

Server-side reads: alerts name the complaint class; negotiated downgrades reveal policy floors; cipher picks reveal preference order; SNI errors reveal routing or cert mapping faults. Interpret with transcripts, not guesses.

Coherence rule: client profile must match its stated platform stack. Mixed signals (new ciphers with ancient versions, desktop ALPN with mobile curves) read as anomalous. Align at the source; never patch single fields to imitate another client against guarded systems.
