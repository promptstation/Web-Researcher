---
name: access-negotiation
description: Find official data channels and win access with professional requests and renewals. Use when the user asks to find official APIs for a site; write a data access request; negotiate API rate limits; track API approvals; report scraping compliance.
compatibility: Any OS with Python 3.10+ and HTTPS; professional email; no scraping needed to start.
metadata:
  author: Promptstation
  version: 1.0.0
  category: bot-management
---

# Access Negotiation

Get to yes through professionalism. You discover official channels first, write requests operators approve, steward quotas carefully, and report compliance so renewals are routine.

Optimize simultaneously for:

- mapped channels
- approved requests
- stewarded quotas
- tracked renewals
- renewed access

Official channels first always; never scrape around a denied request, and never share granted keys.

## Use Cases

### New source

Trigger: user says 'need data from X' or 'do they have an API'

Steps:

1. Discover channels
2. Draft scoped request
3. Negotiate terms
4. Onboard cleanly

Result: Sanctioned access.

### Rate growth

Trigger: user says 'need higher limits' or 'quota too small'

Steps:

1. Show clean history
2. Justify growth with cause
3. Accept staged increases
4. Report usage

Result: Earned headroom.

### Renewal season

Trigger: user says 'keys expiring' or 'annual review'

Steps:

1. Compile compliance report
2. Request renewal early
3. Update scope as needed
4. Rotate keys cleanly

Result: Uninterrupted access.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Channel inventory
- Request drafts
- Terms records
- Key vault entries
- Quota dashboards
- Renewal calendar
- Compliance reports
- Rejection learnings

Never route around denials, and never let keys lapse into emergency scraping.

## Phase 1 — Discover Channels

Run `scripts/api_discovery.py --site <origin>` for docs, feeds, and dumps.

Check developer portals and data programs.

Rank channels by fit and cost.

## Phase 2 — Draft Requests

Write purpose, scope, rate, retention, security, and contact.

Propose review checkpoints.

Send professionally and track.

## Phase 3 — Steward Access

Stay inside granted quotas with headroom.

Vault keys; rotate on schedule.

Log usage per grant.

## Phase 4 — Renew and Report

Report compliance before renewal.

Request changes with justification.

Update terms records same day.

## Examples

### Example 1: Feed unlocked

User says: "Scraping blocked, need the data."

Actions:

1. Found bulk feed program
2. Applied with tight scope
3. Approved in 5 days
4. Scrapers retired

Result: Better data, blessed channel.

### Example 2: Quota doubled

User says: "Hitting API ceiling monthly."

Actions:

1. Showed 6 months clean usage
2. Justified growth
3. Staged increase granted
4. Kept reporting

Result: Earned capacity.

## Troubleshooting

### No reply to request

Cause: Wrong channel or vague ask

Fix:

1. Find the data-program owner
2. Sharpen scope and rate
3. Follow up once politely
4. Proceed only on public scope meanwhile

### Request denied

Cause: Risk, cost, or policy

Fix:

1. Ask what would change the answer
2. Offer narrower scope
3. Accept no gracefully
4. Never route around

### Keys leaked

Cause: Checked into code or logs

Fix:

1. Rotate immediately
2. Purge from history and logs
3. Notify grantor honestly
4. Vault properly

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Discover.
- Request.
- Steward.

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

Avoid scraping before channel search; vague access asks; quota-maximal first requests; keys in code; lapsed renewals; denials routed around.

## Bundled References

Read `references/access-requests.md` when drafting requests or stewarding grants.
Run `scripts/api_discovery.py` to discover official data channels.
Copy `assets/checklists.md` into every delivery.
