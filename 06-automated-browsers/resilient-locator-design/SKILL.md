---
name: resilient-locator-design
description: Design refactor-proof locators and audit selector health measurably. Use when the user asks to fix brittle selectors; audit test-id coverage; replace XPath with roles; handle dynamic lists in Playwright; write selector standards.
compatibility: Any automation stack; saved HTML for audits; no browser needed for static audits.
metadata:
  author: Promptstation
  version: 1.0.0
  category: browser-automation
---

# Resilient Locator Design

End selector whack-a-mole. You rank locator types honestly, audit coverage with counts, rewrite brittle paths to user semantics, and lock standards into review so redesigns stop breaking suites.

Optimize simultaneously for:

- ranked strategies
- counted coverage
- rewritten selectors
- handled dynamics
- living standards

User-facing semantics first; positional and structural selectors only with written justification.

## Use Cases

### Brittle suite

Trigger: user says 'selectors break weekly' or 'XPath everywhere'

Steps:

1. Audit health
2. Rewrite worst offenders
3. Add test-ids with devs
4. Verify stability over sprints

Result: Stable selectors, fewer fixes.

### New coverage

Trigger: user says 'automate this page' or 'locator review'

Steps:

1. Map user flows
2. Choose ladder-top locators
3. Verify uniqueness
4. Document choices

Result: Durable new automation.

### Redesign survival

Trigger: user says 'redesign coming' or 'rebrand next quarter'

Steps:

1. Pre-audit risk areas
2. Add semantic hooks early
3. Run dual-locator transition
4. Retire old post-launch

Result: Green through redesign.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Health audit with counts
- Rewrite list with reasons
- Uniqueness proofs
- Standard document
- Review checklist
- Dev collaboration notes
- Stability metrics
- Redesign plan

Never commit nth-child or absolute XPath without justification, and never skip uniqueness checks.

## Phase 1 — Audit Health

Run `scripts/locator_audit.py --file page.html` for coverage counts.

Score id, test-id, role, and text availability.

Rank pages by brittleness risk.

## Phase 2 — Rewrite Brittle

Climb the ladder per selector with reasons.

Verify strict uniqueness each time.

Pair with devs on missing hooks.

## Phase 3 — Handle Dynamics

Scope lists to containers with filters.

Normalize dynamic text before matching.

Avoid positional indexing; filter by content.

## Phase 4 — Standardize

Publish the ladder plus examples.

Add checks to review.

Track stability per sprint.

## Examples

### Example 1: XPath cleanup

User says: "200 XPaths, constant breakage."

Actions:

1. Audited: 70 percent replaceable
2. Rewrote in 3 sprints with devs
3. Breakage fell 80 percent
4. Standard adopted

Result: Maintainable suite.

### Example 2: List handling

User says: "Product grid flakes."

Actions:

1. Scoped to grid, filtered by name
2. Removed nth indexing
3. Stable across sorts
4. Pattern libraried

Result: Robust list automation.

## Troubleshooting

### Strict-mode violations

Cause: Duplicate matches across portals or lists

Fix:

1. Scope to containers
2. Add name filters
3. Check hidden duplicates
4. Re-verify unique

### Text match flakes

Cause: Whitespace, case, or locale variance

Fix:

1. Normalize before matching
2. Use regex thoughtfully
3. Pin locale in tests
4. Prefer roles over raw text

### No good hooks

Cause: Component library without semantics

Fix:

1. Request test-ids with examples
2. Use interim scoped CSS
3. Track tech-debt removal
4. Never accept XPath forever

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Audit.
- Rewrite.
- Standard.

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

Avoid absolute XPath; nth-child indexing; text-only fragile matches; unscoped list access; hook-free components accepted; standards unenforced.

## Bundled References

Read `references/locator-ladder.md` when choosing or reviewing selectors.
Run `scripts/locator_audit.py` to score static locator health of saved HTML.
Copy `assets/checklists.md` into every delivery.
