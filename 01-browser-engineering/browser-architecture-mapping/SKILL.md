---
name: browser-architecture-mapping
description: Map browser processes, rendering stages, and automation hooks to diagnose failures at the right layer. Use when the user asks to explain why a page hangs or renders blank; map Chromium or Firefox process models; choose between CDP, WebDriver, and BiDi; diagnose renderer crashes and GPU faults; size browser fleets by process memory.
compatibility: Any OS with Chrome or Firefox installed; Python 3.10+ for audit scripts; no browser automation required.
metadata:
  author: Promptstation
  version: 1.0.0
  category: browser-engineering
---

# Browser Architecture Mapping

Give every browser symptom a structural home. You map processes, pipeline stages, isolation boundaries, and protocol hooks so diagnosis starts at evidence instead of folklore, and automation attaches at the layer that actually controls the behavior.

Optimize simultaneously for:

- layer-accurate diagnosis
- correct protocol choice
- crash containment understanding
- memory-aware fleet sizing
- auditable architecture maps

Do not recommend flags, switches, or protocol calls without naming the process or stage they affect and the evidence that implicates it.

## Use Cases

### Blank-page triage

Trigger: user says 'page loads blank in headless but works headed' or 'white screen after deploy'

Steps:

1. Inventory processes and confirm renderer liveness
2. Trace navigation to commit and first paint markers
3. Check GPU process status and swiftshader fallback
4. Pin the failing stage and prescribe the minimal fix

Result: Stage-level diagnosis with evidence instead of flag soup.

### Protocol selection

Trigger: user says 'should I use CDP or WebDriver' or 'need network interception plus BiDi'

Steps:

1. List required observations and interventions
2. Map each to CDP domains, WebDriver endpoints, or BiDi modules
3. Score coverage, stability, and browser support
4. Recommend one primary plus fallback

Result: Defensible protocol choice with a coverage matrix.

### Fleet sizing

Trigger: user says 'workers OOM at scale' or 'how many contexts per box'

Steps:

1. Measure per-renderer and per-GPU memory on target pages
2. Derive contexts per browser and browsers per host
3. Set recycle thresholds and memory guards
4. Document the sizing model

Result: Capacity plan grounded in measured process footprints.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Process map: type, role, IPC peers, and failure blast radius
- Pipeline trace: navigation, commit, parse, style, layout, paint, composite
- Isolation notes: site isolation verdict and sandbox constraints
- Protocol matrix: required capability mapped to CDP, WebDriver, or BiDi
- Symptom table: symptom to stage to first evidence command
- Memory budget: per-process numbers with measurement method
- Crash procedure: exit codes, dump location, recovery behavior
- Deliverable: one-page architecture map plus runbook section

Never emit diagnosis-by-guessing, flag lists without stage rationale, or protocol advice without a capability matrix.

## Phase 1 — Inventory Processes

List every live process for the browser under test with its type flag and memory.

Run `scripts/chrome_process_audit.py --browser chrome` to capture the inventory as JSON.

Label browser, renderer(s) per site, GPU, network service, and utility processes; note the browser version and channel.

If no browser is installed, document the expected topology from the reference and mark numbers as unmeasured.

## Phase 2 — Trace Navigation to Pixels

Open DevTools Performance or use CDP Page lifecycle events and record commit, DOMContentLoaded, first paint, and load.

Attribute each gap to a stage: DNS/TLS/connect, content download, parse, script, style/layout, paint/composite.

Produce a stage table with timestamps and the dominant cost per stage.

## Phase 3 — Verify Isolation and Sandbox

Confirm renderers are per-site where expected and cross-site frames are isolated.

Record sandbox status for renderers and GPU; note any --no-sandbox usage as a blocking risk with justification required.

State what automation can and cannot touch from its privilege level (profile files, devices, OS).

## Phase 4 — Choose Hooks and Size Capacity

Build the capability matrix: each needed observation or intervention mapped to CDP domain, WebDriver endpoint, or BiDi module.

Recommend the primary protocol and one fallback, with browser-support caveats.

Convert per-renderer memory into contexts-per-browser and browsers-per-host with recycle thresholds.

## Examples

### Example 1: Headless blank page

User says: "Headless shows blank, headed is fine."

Actions:

1. Ran process audit: renderer alive, GPU process in swiftshader fallback
2. Traced navigation: commit ok, first paint never fires
3. Pinned WebGL init failure under software GL as the blocker
4. Prescribed headed/xvfb or WebGL-disabled path with evidence

Result: Fix targeted at the GPU stage instead of random flags.

### Example 2: Interception protocol pick

User says: "Need request interception in Firefox and Chrome."

Actions:

1. Mapped interception to CDP Fetch, WebDriver classic limits, BiDi network module
2. Scored BiDi coverage vs maturity per browser
3. Recommended BiDi-first with CDP fallback on Chromium

Result: One matrix, one recommendation, explicit fallback.

## Troubleshooting

### Renderer uses gigabytes on one page

Cause: Leaking DOM/JS heap or unbounded canvas buffers in that site's renderer

Fix:

1. Confirm growth is one renderer via repeated audits
2. Capture heap snapshot and DOM node counts
3. Recycle context and retest to separate leak from bloat
4. Cap contexts and set per-renderer memory guard

### Aw Snap / renderer kill under load

Cause: OOM, stack exhaustion, or sandbox-triggered termination

Fix:

1. Read exit code and crash key from logs
2. Correlate with memory timeline and concurrent contexts
3. Reduce concurrency and enable per-job browser recycle
4. File layout or input minimization if reproducible

### Automation sees different behavior than headed user

Cause: Different GPU path, user agent, viewport, or missing human-behavior pacing

Fix:

1. Diff process flags and feature states between modes
2. Align GPU path first before touching fingerprints
3. Add paced waits and retry-assertions
4. Re-measure instead of stacking stealth flags

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Architecture map.
- Trace and isolation.
- Hooks and capacity.

## Decision Heuristic

Before adding complexity, ask:

1. What outcome requires this step?
2. What evidence justifies it?
3. What happens when it fails?
4. What is the cheaper alternative?
5. What proves quality did not regress?
6. What must be logged for audit?
7. What is the rollback plan?

If the main justification is "more", prove the outcome needs it first.

## Anti-Patterns

Avoid flag soup without stage evidence; one shared renderer assumed for all sites; protocol picks without capability matrices; headed/headless diffs blamed on detection first; memory sizing from blog numbers instead of measurements; sandbox disabled without a written risk note.

## Bundled References

Read `references/architecture-layers.md` when mapping symptoms to stages or picking protocols.
Run `scripts/chrome_process_audit.py` to capture a process inventory as evidence.
Copy `assets/checklists.md` into every delivery.
