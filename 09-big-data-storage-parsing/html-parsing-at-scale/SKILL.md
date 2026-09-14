---
name: html-parsing-at-scale
description: Parse millions of pages fast, correctly, and boilerplate-free. Use when the user asks to parse HTML faster; lxml or BeautifulSoup for scale; remove boilerplate from articles; handle encoding errors; stream large HTML files.
compatibility: Python 3.10+; lxml for speed, bs4 for tolerance; stdlib fallback included.
metadata:
  author: Promptstation
  version: 1.0.0
  category: data-engineering
---

# HTML Parsing at Scale

Turn markup into data at speed. You pick parsers by evidence, stream the big ones, normalize encodings, strip boilerplate measurably, and parallelize with golden fixtures guarding correctness.

Optimize simultaneously for:

- right parsers
- streamed larges
- clean text
- no boilerplate
- guarded speed

Correctness first: golden fixtures must pass before any speed work ships.

## Use Cases

### Slow parse

Trigger: user says 'parsing takes hours' or 'bs4 too slow'

Steps:

1. Benchmark parsers
2. Switch hot path
3. Parallelize
4. Verify fixtures

Result: 10x parse speed.

### Dirty text

Trigger: user says 'nav in content' or 'ads extracted'

Steps:

1. Score content blocks
2. Strip boilerplate
3. Verify samples
4. Lock fixtures

Result: Clean content.

### Encoding pain

Trigger: user says 'mojibake' or 'decode errors'

Steps:

1. Detect properly
2. Normalize UTF-8
3. Fix pipeline
4. Validate corpus

Result: Clean corpus.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Parser decision
- Throughput bench
- Encoding policy
- Boilerplate method
- Golden fixtures
- Parallel design
- Memory profile
- Quality samples

Never regex-parse HTML structurally or ship speedups that fail fixtures.

## Phase 1 — Choose Parser

lxml for speed, bs4+lxml for tolerance, stdlib for zero-dep.

Benchmark on your corpus.

Lock golden fixtures first.

## Phase 2 — Extract Fields

Prototype with `scripts/html_field_extract.py --file page.html`.

Selectors per ladder; fallbacks ordered.

Normalize whitespace and entities.

## Phase 3 — Strip Boilerplate

Density and link-ratio scoring.

Verify on 100 samples.

Measure precision/recall roughly.

## Phase 4 — Scale

Stream big docs; chunk lists.

Parallelize by document.

Profile memory; cap workers.

## Examples

### Example 1: 20x parse

User says: "bs4 parses 2 pages/sec."

Actions:

1. lxml hot path 40/sec
2. Fixtures green
3. Parallel 8x more
4. Cost collapsed

Result: Fast correct parsing.

### Example 2: Clean articles

User says: "Menus pollute corpus."

Actions:

1. Block scoring added
2. Boilerplate under 2 percent
3. Samples verified
4. Locked in

Result: Clean text corpus.

## Troubleshooting

### Parser crashes on pages

Cause: Malformed markup or huge docs

Fix:

1. Tolerant parser fallback
2. Size caps plus streaming
3. Quarantine monsters
4. Log and continue

### Selectors rot

Cause: Template changes

Fix:

1. Ordered fallbacks
2. Monitor field rates
3. Alert on drops
4. Update ladder

### Memory grows

Cause: DOM retention or leaks

Fix:

1. Parse and release
2. Chunk inputs
3. Cap workers
4. Profile hot loop

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Choose.
- Extract.
- Scale.

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

Avoid regex-structure parsing; single-parser dogma; encoding assumptions; boilerplate blindness; fixture-free speedups; memory-blind parallelism.

## Bundled References

Read `references/html-parsing.md` when choosing parsers or stripping boilerplate.
Run `scripts/html_field_extract.py` to prototype field extraction (stdlib).
Copy `assets/checklists.md` into every delivery.
