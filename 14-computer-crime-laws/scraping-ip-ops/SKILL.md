---
name: scraping-ip-ops
description: Collect and reuse web content inside copyright and database rights. Use when the user asks to copyright and web scraping; fair use for scraped data; database rights EU; handle DMCA takedowns; log content provenance.
compatibility: Counsel for fair-use calls; provenance store; takedown intake channel.
metadata:
  author: Promptstation
  version: 1.0.0
  category: cyber-law
---

# Scraping IP Ops

Respect creators while building datasets. You triage rights per source, assess fair use honestly, honor database rights, log provenance per item, and process takedowns fast — with counter-notice fairness.

Optimize simultaneously for:

- triaged sources
- honest assessments
- logged provenance
- fast takedowns
- scoped reuses

Fair-use calls need counsel on gray; takedowns honored first, disputed through process. Not legal advice.

## Use Cases

### Dataset build

Trigger: user says 'train on crawled text' or 'collect articles'

Steps:

1. Triage rights
2. Assess use
3. License or limit
4. Log all

Result: Rights-aware dataset.

### Takedown live

Trigger: user says 'DMCA notice' or 'remove my content'

Steps:

1. Validate notice
2. Remove fast
3. Notify + counter path
4. Log + learn

Result: Compliant response.

### Reuse review

Trigger: user says 'publish this data' or 'sell insights'

Steps:

1. Scope reuse
2. Re-assess rights
3. License gaps
4. Approve/file

Result: Cleared reuse.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Source rights table
- Fair-use memos
- License files
- Provenance log
- Takedown log
- Counter-notices
- Reuse approvals
- Counsel reviews

Never ignore takedowns or treat fair use as a blanket license.

## Phase 1 — Triage Sources

License/ToS/robots per source.

Risk-tier content types.

Log with `scripts/content_rights_log.py`.

## Phase 2 — Assess Use

Purpose, nature, amount, effect factors.

Transformative + minimal + non-substitute.

Counsel signs gray/commercial.

## Phase 3 — Log Provenance

Per item: source, date, rights basis.

Propagate to derivatives.

Auditable on demand.

## Phase 4 — Honor Takedowns

24-72h removal; notify; counter path.

Repeat-infringer policy.

Learn into sourcing.

## Examples

### Example 1: Licensed corpus

User says: "News training data?"

Actions:

1. Triaged: license 2, limit 1
2. Fair-use memo'd research
3. Provenance logged
4. Audited clean

Result: Defensible corpus.

### Example 2: Takedown smooth

User says: "Photographer complains."

Actions:

1. Removed in 12h
2. Sourced licensed alt
3. Counter path offered
4. Relationship kept

Result: Respectful ops.

## Troubleshooting

### Fair-use fog

Cause: Commercial + whole-work copying

Fix:

1. Narrow use
2. License
3. Counsel memo
4. Document

### Sui generis surprise

Cause: EU DB extraction

Fix:

1. Assess substantiality
2. License or limit
3. Counsel EU
4. Log call

### Notice floods

Cause: Aggressive sourcing

Fix:

1. Pause source
2. Fix pipeline
3. Bulk remediate
4. Re-source clean

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Take.
- Keep.
- Yield.

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

Avoid rights-blind scraping; blanket fair-use; provenance-free corpora; takedown-ignoring; reuse-scope creep; counsel-free gray.

## Bundled References

Read `references/content-rights.md` when collecting or reusing content.
Run `scripts/content_rights_log.py` as a content rights log.
Copy `assets/checklists.md` into every delivery.
