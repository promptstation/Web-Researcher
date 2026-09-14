# Engine Tiers and Scheduling

V8 pipeline: parse to AST, Ignition baseline bytecode, Sparkplug quick compile, TurboFan optimized compile for hot functions, deopt back to baseline when assumptions break. Hidden classes reward stable object shapes; mixed types and delete punish hot paths. JavaScriptCore and SpiderMonkey share the tiered idea with different tier names.

Event loop order per turn: run one macrotask, drain the microtask queue fully, render if needed, then next macrotask. Promises and queueMicrotask are microtasks; setTimeout, message events, and I/O callbacks are macrotasks. Async functions resume as microtasks. Long tasks are macrotasks over 50ms and drive interaction delays.

Memory truths: detached DOM persists while JS retains any node; listeners on removed subtrees retain whole trees; consoles and closures hold surprising roots. Compare snapshots by retained size, follow the shortest retaining path, and confirm with a flat re-run.

Offload rules: workers cannot touch DOM; transfer ArrayBuffers instead of copying; sequence numbered messages preserve order; scheduler.yield or setTimeout(0) breaks microtask starvation; requestIdleCallback suits deferrable hydration with deadlines.
