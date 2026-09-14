---
name: bot-management-literacy
description: Classify bot-management outcomes from evidence and route each to lawful responses. Use when the user asks to identify a challenge page vendor; classify blocks versus rate limits; explain how bot detection works; read a bot-management response; decide what to do after a block.
compatibility: Any OS with Python 3.10+; response samples you received lawfully; no probing tools needed.
metadata:
  author: Promptstation
  version: 1.0.0
  category: bot-management
---

# Bot Management Literacy

Replace block-page panic with classified understanding. You map detection pipelines, recognize outcomes from evidence, separate lookalikes, and route every class to backoff, permission, API, or stop.

Optimize simultaneously for:

- mapped pipelines
- classified outcomes
- separated lookalikes
- routed responses
- logged decisions

Classify from evidence you already hold; do not probe defenses to complete the taxonomy, and never treat blocks as puzzles to defeat.

## Use Cases

### Page triage

Trigger: user says 'what blocked us' or 'which vendor is this'

Steps:

1. Capture page plus headers
2. Classify with marker quotes
3. Separate rate vs bot vs auth
4. Route to response

Result: Named outcome, correct next step.

### Fleet pattern

Trigger: user says 'blocks rising everywhere' or 'new vendor live'

Steps:

1. Classify samples per domain
2. Chart class mix over time
3. Name the shift
4. Adjust access strategy

Result: Strategy matched to reality.

### Response routing

Trigger: user says 'playbook for blocks' or 'when to stop'

Steps:

1. Build outcome-to-action table
2. Wire detection to router
3. Log decisions
4. Review weekly

Result: Consistent lawful handling.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Pipeline map per vendor studied
- Marker catalog with quotes
- Classification per sample
- Lookalike separation notes
- Response routing table
- Decision log
- Review cadence
- Stop criteria

Never probe defenses for taxonomy sport, and never route blocks toward circumvention.

## Phase 1 — Map Pipelines

Study public docs for signals, scores, and actions per vendor.

Draw the allow-challenge-limit-block ladder.

Note what each action looks like to a client.

## Phase 2 — Classify Samples

Run `scripts/challenge_classifier.py --file sample.html --url <u>` per sample.

Quote the markers behind each verdict.

Separate rate, bot, auth, geo, and capacity explicitly.

## Phase 3 — Build the Router

Map each class to backoff, permission, API, or stop.

Define stop criteria with teeth.

Wire classifiers to the router.

## Phase 4 — Log and Review

Log every routing decision with evidence.

Review weekly for drift.

Update the catalog on changes.

## Examples

### Example 1: Mystery wall

User says: "New verify page, unknown vendor."

Actions:

1. Markers matched managed-challenge class
2. Routed to backoff plus API request
3. Access granted via API
4. Catalog updated

Result: Lawful resolution, catalog richer.

### Example 2: Rate vs bot

User says: "403s everywhere after scale-up."

Actions:

1. Headers showed rate shaping, not bot verdict
2. Cut concurrency, honored Retry-After
3. Errors cleared
4. Router learned the split

Result: Shaping fix, not an arms race.

## Troubleshooting

### Classifier unsure

Cause: Generic page or new marker set

Fix:

1. Save full sample with headers
2. Check vendor changelogs
3. Default to backoff plus review
4. Update catalog after verdict

### Mixed classes per domain

Cause: Layered defenses or A/B policies

Fix:

1. Classify per URL pattern
2. Route per class
3. Track mix over time
4. Negotiate access for the set

### Blocks after permission

Cause: Mis-scoped allowlist or changed egress

Fix:

1. Confirm allowlisted identities
2. Check egress drift
3. Re-verify with owner
4. Never self-exempt

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Map.
- Classify.
- Route.

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

Avoid status-only verdicts; probe-to-complete taxonomies; blocks treated as puzzles; rate and bot conflation; routers without stop criteria; unlogged exceptions.

## Bundled References

Read `references/outcome-classes.md` when classifying responses or routing actions.
Run `scripts/challenge_classifier.py` to classify saved response samples.
Copy `assets/checklists.md` into every delivery.
