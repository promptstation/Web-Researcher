---
name: scraping-transparency
description: Publish methods and limits; correct openly; report regularly. Use when the user asks to publish scraping methodology; write data limitations; correction policy; transparency reports; invite external audit.
compatibility: Publishing channel; correction workflow; audit relationships.
metadata:
  author: Promptstation
  version: 1.0.0
  category: ethics
---

# Scraping Transparency

Work in daylight. You publish methods readably, state limits prominently, open feedback channels genuinely, correct errors visibly with versions, and report quarterly — inviting audits that make you better.

Optimize simultaneously for:

- open methods
- honest limits
- live channels
- visible corrections
- regular reports

No stealth methods for public-impact data; corrections never silent.

## Use Cases

### Methods live

Trigger: user says 'document collection' or 'how did you get this'

Steps:

1. Write methods
2. State limits
3. Publish + invite
4. Maintain

Result: Credible data.

### Error found

Trigger: user says 'numbers wrong' or 'bug in data'

Steps:

1. Scope fast
2. Correct visibly
3. Notify users
4. Prevent repeat

Result: Trust kept.

### Audit invite

Trigger: user says 'verify us' or 'external review'

Steps:

1. Scope audit
2. Open books
3. Remediate
4. Publish summary

Result: Verified ops.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Methods docs
- Limit statements
- Repro assets
- Feedback log
- Correction log
- Report archive
- Audit reports
- Owner roster

Never hide methods that shape public understanding or bury corrections.

## Phase 1 — Document Methods

Sources, tools, rates, dates, versions.

Draft with `scripts/methods_readme.py --project NAME`.

Readable by outsiders.

## Phase 2 — State Limits

Coverage, bias, freshness, error rates.

Prominent, not footnoted.

Updated per release.

## Phase 3 — Invite Scrutiny

Contact + repro + data samples.

Respond to queries dated.

External audit yearly-ish.

## Phase 4 — Correct and Report

Visible corrections + versions.

Quarterly transparency reports.

Log everything.

## Examples

### Example 1: Believed data

User says: "Press questions our numbers."

Actions:

1. Methods + limits shown
2. Repro shared
3. Story corrected fairly
4. Cited since

Result: Earned credibility.

### Example 2: Clean correction

User says: "Error in v3 dataset."

Actions:

1. v3.1 in 48h
2. Notice + diff
3. Users notified
4. Checks added

Result: Handled right.

## Troubleshooting

### Methods rot

Cause: Docs trail code

Fix:

1. Generate from pipeline
2. Review per release
3. Owner assigned
4. Audit quarterly

### Limit minimization

Cause: Marketing pressure

Fix:

1. Limits prominent
2. Sign-off required
3. Push back
4. Protect authors

### Feedback void

Cause: Channel unmonitored

Fix:

1. SLA + owner
2. Respond all
3. Log + act
4. Report volumes

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Show.
- Hear.
- Own.

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

Avoid stealth methods; footnoted limits; void feedback; silent corrections; report-free years; audit-allergic ops.

## Bundled References

Read `references/open-methods.md` when publishing or correcting.
Run `scripts/methods_readme.py` to draft methods docs.
Copy `assets/checklists.md` into every delivery.
