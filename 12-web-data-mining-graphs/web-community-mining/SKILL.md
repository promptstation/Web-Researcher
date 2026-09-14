---
name: web-community-mining
description: Find communities in web graphs for discovery and spam defense. Use when the user asks to find communities in graphs; cluster websites by topic; detect link farms; label propagation tutorial; partition a web graph.
compatibility: Python 3.10+; NetworkX/python-louvain optional; samples for naming.
metadata:
  author: Promptstation
  version: 1.0.0
  category: data-mining
---

# Web Community Mining

Reveal the graph's neighborhoods. You propagate labels fast, optimize modularity for stability, blend text with links, name communities from samples, and apply structure to discovery and spam defense.

Optimize simultaneously for:

- sketched labels
- stable partitions
- named hoods
- found rings
- applied structure

Communities validated by samples; spam accusations need evidence, not just density.

## Use Cases

### Discovery

Trigger: user says 'find related sites' or 'map the niche'

Steps:

1. Partition graph
2. Name hoods
3. Rank inside
4. Recommend

Result: Mapped niche.

### Farm hunt

Trigger: user says 'spam network?' or 'dense cluster'

Steps:

1. Isolate cluster
2. Gather evidence
3. Confirm or clear
4. Act + log

Result: Evidence-based call.

### Navigation

Trigger: user says 'browse by topic' or 'site directory'

Steps:

1. Cluster topical
2. Name + verify
3. Publish browse
4. Maintain

Result: Living directory.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Graph snapshot
- Method config
- Stability report
- Naming samples
- Validation log
- Spam evidence
- Application design
- Refresh plan

Never label communities unvalidated or accuse spam on density alone.

## Phase 1 — Sketch Fast

Run `scripts/label_prop.py --edges edges.txt` for first cut.

Inspect size distribution.

Flag giants and singletons.

## Phase 2 — Partition Stable

Modularity optimize; seed fixed.

Stability across runs.

Hierarchy for giants.

## Phase 3 — Name and Validate

Top pages + text per community.

Human names 20+.

Sample-verify each.

## Phase 4 — Apply

Discovery, spam, navigation.

Refresh scheduled.

Drift monitored.

## Examples

### Example 1: Niche mapped

User says: "Who links whom here?"

Actions:

1. 12 communities named
2. Authorities per hood
3. Report shipped
4. Refreshed quarterly

Result: Clear map.

### Example 2: Ring confirmed

User says: "Suspicious cluster found."

Actions:

1. Evidence: fresh, dense, template
2. Confirmed farm
3. Pruned from rank
4. Logged

Result: Clean graph.

## Troubleshooting

### Giant hairball

Cause: Nav links glue all

Fix:

1. Filter link types
2. Weight content links
3. Re-run
4. Hierarchy for rest

### Unstable partitions

Cause: Random order effects

Fix:

1. Fix seeds
2. Consensus runs
3. Stable core kept
4. Report variance

### Names wrong

Cause: Top-page bias

Fix:

1. Sample deeper
2. Text signals
3. Human review
4. Rename freely

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Cut.
- Name.
- Use.

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

Avoid nav-glued partitions; seed-free runs; sample-free names; density-only accusations; refresh-free maps; evidence-free prunes.

## Bundled References

Read `references/community-mining.md` when partitioning graphs.
Run `scripts/label_prop.py` to sketch communities fast.
Copy `assets/checklists.md` into every delivery.
