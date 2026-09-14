---
name: content-mining-ops
description: Mine crawled text for terms, topics, and trends — judged, not vibes. Use when the user asks to TF-IDF on crawled text; extract keyphrases; find topics in corpus; detect trending terms; evaluate text mining.
compatibility: Python 3.10+; scikit-learn optional; 100+ judged samples for eval.
metadata:
  author: Promptstation
  version: 1.0.0
  category: data-mining
---

# Content Mining Ops

Turn text piles into signals. You score TF-IDF sanely, rank keyphrases for judges, sketch topics with labels, detect bursts honestly, and evaluate everything on judged samples before dashboards.

Optimize simultaneously for:

- scored terms
- judged phrases
- labeled topics
- real trends
- eval'd mining

Mining output judged by humans before it drives decisions.

## Use Cases

### Corpus briefing

Trigger: user says 'what is this corpus about' or 'summarize topics'

Steps:

1. TF-IDF + topics
2. Judge labels
3. Brief with quotes
4. Ship dashboard

Result: True briefing.

### Trend watch

Trigger: user says 'what is rising' or 'track emergence'

Steps:

1. Baseline terms
2. Burst detect
3. Verify real
4. Alert + report

Result: Early signal.

### Keyphrase SEO

Trigger: user says 'top phrases' or 'content gaps'

Steps:

1. Rank phrases
2. Judge quality
3. Gap vs own
4. Recommend

Result: Content roadmap.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Tokenization spec
- DF table
- Phrase method
- Topic labels
- Trend baselines
- Judged samples
- Dashboard
- Refresh plan

Never present unjudged topics or burst noise as trends.

## Phase 1 — Score Terms

Tokenize per language; DF over corpus.

Run `scripts/tfidf_top.py --in docs.jsonl` for baselines.

Stopword-tune by eye.

## Phase 2 — Rank Phrases

Candidate n-grams + rank.

Judge 100 for precision.

Keep judged winners.

## Phase 3 — Sketch Topics

Cluster + label with terms.

Human-rename all.

Stability checked.

## Phase 4 — Watch Trends

Burst vs baseline; slope confirm.

Verify with reads.

Alert + weekly report.

## Examples

### Example 1: Briefing trusted

User says: "100k docs, what matters?"

Actions:

1. Topics judged
2. Brief with evidence
3. Execs act
4. Refreshed monthly

Result: Acted-on insight.

### Example 2: Trend real

User says: "Is X actually rising?"

Actions:

1. Burst + slope + reads
2. Confirmed real
3. Alerted early
4. Won the cycle

Result: True early signal.

## Troubleshooting

### Junk top terms

Cause: Template/stopword leakage

Fix:

1. Clean boilerplate
2. Tune stops
3. DF floors
4. Re-judge

### Topics mush

Cause: K wrong or mixed corpus

Fix:

1. Split corpus
2. Tune K
3. Hybrid link signals
4. Human labels

### False bursts

Cause: Volume shifts, not interest

Fix:

1. Normalize by volume
2. Require slope
3. Verify reads
4. Alert less

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Score.
- Judge.
- Watch.

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

Avoid boilerplate-fed mining; stopword-blind tops; judge-free topics; burst-noise alerts; volume-blind trends; evidence-free briefings.

## Bundled References

Read `references/text-mining.md` when mining terms, topics, trends.
Run `scripts/tfidf_top.py` to baseline TF-IDF terms.
Copy `assets/checklists.md` into every delivery.
