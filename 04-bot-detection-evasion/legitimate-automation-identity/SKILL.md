---
name: legitimate-automation-identity
description: Identify crawlers honestly with compliant agents, robots adherence, and purpose docs. Use when the user asks to write a proper crawler user agent; check robots.txt for my bot; honor crawl-delay correctly; publish a crawler purpose page; review terms before scraping.
compatibility: Any OS with Python 3.10+ and HTTPS; no crawling needed to audit compliance.
metadata:
  author: Promptstation
  version: 1.0.0
  category: bot-management
---

# Legitimate Automation Identity

Be the crawler operators welcome. You identify honestly, obey robots precisely, plan from sitemaps, publish purpose, and review terms before collecting anything.

Optimize simultaneously for:

- honest agents
- obeyed robots
- sitemap-first plans
- published purpose
- reviewed terms

Obey robots.txt and terms strictly; treat ambiguity as disallow until clarified with the operator.

## Use Cases

### New crawler launch

Trigger: user says 'launching a crawler' or 'compliance checklist'

Steps:

1. Draft UA and purpose page
2. Audit robots across targets
3. Plan sitemap-first
4. Review terms and log

Result: Compliant launch pack.

### Disallow dispute

Trigger: user says 'robots blocks us' or 'is this path allowed'

Steps:

1. Parse the exact group and rule
2. Quote the matching line
3. Exclude or ask operator
4. Log the verdict

Result: Correct compliance call.

### Operator outreach

Trigger: user says 'ask for access' or 'exception request'

Steps:

1. Package identity plus purpose
2. Propose rate and scope
3. Send professionally
4. Track response

Result: Documented access dialogue.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- UA strings with contact
- Robots verdicts per target
- Sitemap plans
- Purpose pages live
- Terms notes per target
- Compliance logs
- Outreach records
- Review dates

Never ignore robots or terms, and never treat silence as permission.

## Phase 1 — Draft Identity

Write UA as Name/Version (+purpose-URL; contact-email).

Publish the purpose page before first crawl.

Use the same identity fleet-wide.

## Phase 2 — Audit Robots

Run `scripts/robots_tos_check.py --site <origin> --ua <agent>` per target.

Record allow, disallow, delay, and sitemap per group.

Treat ambiguity as disallow; ask operators.

## Phase 3 — Plan Compliant

Build URL lists from sitemaps first.

Apply crawl-delay globally per host.

Exclude disallowed paths entirely.

## Phase 4 — Review and Log

Read terms for automation clauses.

Log verdicts and outreach.

Re-audit quarterly.

## Examples

### Example 1: Research launch

User says: "Crawl 50 university sites."

Actions:

1. Identity plus purpose published
2. Robots audited: 44 open, 6 partial
3. Scoped to allowed
4. Zero complaints

Result: Clean compliant crawl.

### Example 2: Partial disallow

User says: "Half the paths disallowed."

Actions:

1. Parsed exact groups
2. Scoped to allowed plus sitemaps
3. Asked about two key paths
4. One granted, one refused, both logged

Result: Respectful partial coverage.

## Troubleshooting

### Conflicting group matches

Cause: Overlapping UA groups with different rules

Fix:

1. Apply most-specific group
2. Quote matched lines
3. Choose stricter on ties
4. Ask operator to clarify

### No robots file

Cause: Missing file is not a free pass

Fix:

1. Proceed minimally and politely
2. Still review terms
3. Publish purpose
4. Offer opt-out

### Terms forbid scraping

Cause: Explicit automation ban

Fix:

1. Stop that scope immediately
2. Seek API or permission
3. Document the decision
4. Never reframe as allowed

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Identity.
- Robots.
- Terms.

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

Avoid generic or fake user agents; robots ignored or cached forever; crawl-delay skipped; disallowed probing; terms unread; silence read as permission.

## Bundled References

Read `references/robots-rules.md` when parsing robots or planning crawls.
Run `scripts/robots_tos_check.py` to audit robots compliance per target.
Copy `assets/checklists.md` into every delivery.
