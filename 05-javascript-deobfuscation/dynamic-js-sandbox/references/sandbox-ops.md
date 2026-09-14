# Sandbox Ops

Isolation bar: disposable VM or container, no host mounts, no bridged malware-net, snapshots before runs, destroy or revert after. Node vm contexts are observation conveniences, not security boundaries; assume escape and isolate at VM level.

Stubbing: implement document, window, navigator, localStorage, fetch/XHR with logging sinks; answer enough for progress, never with real data; iterate from ReferenceErrors. Log every stub hit with arguments and stack depth.

Budgets: wall timeout 5-30s, stub-call caps, loop-iteration guards via instrumented Date, memory watch. Exceeding budget is itself a finding (delay tactic).

Evidence: sample sha256, tool versions, stub set, environment matrix, full transcripts, IOCs with payload shapes. Reports distinguish observed versus inferred; keying and variance get explicit sections.
