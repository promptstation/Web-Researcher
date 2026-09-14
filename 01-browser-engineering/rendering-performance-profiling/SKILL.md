---
name: rendering-performance-profiling
description: Budget, measure, and fix rendering performance with critical-chain evidence and release guards. Use when the user asks to fix Core Web Vitals failures; map a critical request chain; cut image and font cost; contain slow third parties; set performance budgets for releases.
compatibility: Any modern browser with DevTools and Lighthouse; Python 3.10+ for budget audits; field data source optional but recommended.
metadata:
  author: Promptstation
  version: 1.0.0
  category: browser-engineering
---

# Rendering Performance Profiling

Make speed a budgeted feature, not a wish. You triage vitals honestly, map critical chains to owners, fix hero resources first, contain third parties, and lock wins behind build-time budgets.

Optimize simultaneously for:

- honest vitals triage
- owned critical chains
- faster hero paths
- contained third parties
- surviving budgets

Do not claim performance wins without field-or-lab deltas from identical runs, and do not add third parties without budget sign-off.

## Use Cases

### Failing vitals

Trigger: user says 'LCP red' or 'CLS failing in Search Console'

Steps:

1. Triage lab vs field and device splits
2. Map the critical chain for the failing metric
3. Fix the top owner first
4. Verify in lab, then watch field

Result: Metric fixed at its true owner.

### Template budgets

Trigger: user says 'stop perf regressions' or 'define budgets'

Steps:

1. Measure current transfers per template
2. Set count, byte, and timing budgets
3. Wire build guards with clear failures
4. Drill the regression response

Result: Regressions caught before deploy.

### Third-party bloat

Trigger: user says 'tags slowed us down' or 'audit third parties'

Steps:

1. Rank third parties by blocking cost
2. Facade or delay non-critical tags
3. Negotiate or replace the worst
4. Lock the survivors into budget

Result: Contained tags with preserved function.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Vitals table: lab and field per template
- Chain map: hops with owners and costs
- Hero plan: image, font, API priorities
- Third-party rank with containment per tag
- Budget sheet: bytes, counts, timings
- Build guard: failing output example
- Before/after deltas from identical runs
- Regression drill record

Never report lab-only wins as user impact, and never approve third parties outside budget.

## Phase 1 — Triage Vitals

Collect lab runs plus any field data; split by device and connection.

Decide which failures are field-real and which are lab artifacts.

Rank pages by traffic times severity.

## Phase 2 — Map the Chain

Run `scripts/perf_budget.py --url <page> --budget-js-kb 300 --budget-img-kb 500` for a transfer baseline.

Draw the critical chain from navigation to LCP with per-hop cost and owner.

Name the single top owner before proposing fixes.

## Phase 3 — Fix Hero First

Prioritize the LCP image with fetchpriority and correct sizing; preload only the true hero.

Subset fonts, use display swap, and cut font weights.

Facade or idle-load below-fold third parties; delay hydration that shifts layout.

## Phase 4 — Lock Budgets

Write budgets per template: JS, CSS, image bytes, request counts, LCP and CLS caps.

Add a build check that fails loudly with the offending asset named.

Run a planted-regression drill and record detection time.

## Examples

### Example 1: LCP rescue

User says: "Product pages LCP over 4s on mobile."

Actions:

1. Chain showed late-discovered hero plus render-blocking tag
2. Preloaded hero with sizing, facaded tag
3. Lab LCP 4.2s to 2.1s, field followed in 2 weeks
4. Budget locked for hero bytes

Result: Sustained LCP win.

### Example 2: Tag containment

User says: "Marketing tags keep regressing us."

Actions:

1. Ranked 9 tags by blocking cost
2. Facaded 4, delayed 3, kept 2 in budget
3. Build guard rejects new blocking tags
4. Quarter without regressions

Result: Marketing velocity with guardrails.

## Troubleshooting

### Lab green but field red

Cause: Device, network, or cache-state gaps between lab and users

Fix:

1. Match lab throttling to field p75
2. Test logged-in and returning-user states
3. Check slow-device splits
4. Trust field for priority, lab for iteration

### LCP element shifts between runs

Cause: Racing hero candidates or A/B variants

Fix:

1. Pin the variant for measurement
2. Stabilize hero selection
3. Report per-variant LCP
4. Fix the common path first

### Budget failures ignored

Cause: Noisy guard or no owner for failures

Fix:

1. Name the asset and owner in output
2. Make failures blocking on release branches
3. Review budget fit quarterly
4. Celebrate prevented regressions

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Triage.
- Fix.
- Guard.

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

Avoid lab-only impact claims; preload spraying; hero images without sizing; third parties without owners; budgets without build guards; field data ignored for quarters.

## Bundled References

Read `references/vitals-and-budgets.md` when triaging metrics or writing budgets.
Run `scripts/perf_budget.py` to baseline transfer weight against budgets.
Copy `assets/checklists.md` into every delivery.
