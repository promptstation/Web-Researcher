# Headless Modes

Mode map: old headless is a separate minimal implementation with the most deltas; new headless (--headless=new) runs the full browser UI-less with near-headed fidelity; xvfb-headed runs headed under a virtual display for GPU-dependent work on servers; headed is ground truth.

Typical delta sources: GPU compositing and WebGL paths, fontconfig versus OS font stacks, media codec availability, permission defaults, extension loading, print and PDF paths, and download handling. Timing also differs because automation outpaces humans.

Flag discipline: default plus explicit needs only. Verify --no-sandbox never ships without a risk note; confirm --disable-gpu actually changes the composite path on your build; test --use-gl and --use-angle values per platform instead of copying.

Parity protocol: identical URL, viewport, device scale, locale, timezone, user agent, waits, and network shaping. Diff screenshot, serialized DOM, console messages, and request lists. Attribute all deltas before changing flags.
