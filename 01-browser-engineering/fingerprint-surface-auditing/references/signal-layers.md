# Signal Layers

Layer 1 JS identity: userAgent, platform, hardwareConcurrency, deviceMemory, languages, timezone, screen and viewport, touch points, plugins and mimeTypes, permissions states, storage estimates. Layer 2 rendering: canvas 2D pixel hash, WebGL vendor/renderer plus parameter set, font enumeration via measurement, CSS media and color-gamut. Layer 3 audio: oscillator plus analyser hash chains. Layer 4 network: TLS version, cipher, ALPN, JA3-style handshake shape, HTTP/2 fingerprint, IP and ASN. Layer 5 behavior: mouse entropy, typing cadence, scroll patterns, timing jitter.

Entropy notes: no single common signal identifies; combinations do. Rare values dominate: odd viewports, large font sets, unusual timezones, exotic GPUs. Consistency beats rarity-hiding: mismatched tuples are themselves strong signals.

Measurement protocol: same profile, same network, two pages, three runs, record medians. Store hashes for images, full values for strings. Date every verdict; datasets drift.

Defense posture: standard configurations, few extensions, coherent locale stack, updated browsers, tracking protection on. State residual exposure plainly.
