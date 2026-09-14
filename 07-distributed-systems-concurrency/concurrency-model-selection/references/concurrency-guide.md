# Concurrency Guide

Rules of thumb: IO-bound fetching -> asyncio (hundreds of connections) or threads (dozens, simpler); CPU-bound parsing -> multiprocessing; mixed -> async IO feeding process pools via queues. Browser fleets -> processes (one browser each), never threads sharing a browser.

GIL reality: threads help IO waits, not CPU; measure with CPU-heavy microbench before and after threading; if flat or worse, go processes. Re-measure yearly as libraries change.

Sizing: connections from target politeness first, memory second; process workers from cores minus one; queue depth bounded (100-10k) with backpressure. Shutdown: SIGTERM drains, SIGKILL caps; test both.

Hybrids: single async loop per process; executors for blocking calls; queues (not shared dicts) between processes; immutable messages; idempotent handlers so redelivery is safe.
