---
name: video-frame-ops
description: Sample video smartly, extract reproducibly, and track with ID discipline. Use when the user asks to extract frames from video; sample video for annotation; dedupe video frames; track objects in video; budget video storage.
compatibility: ffmpeg installed; Python 3.10+; tracking libs (ByteTrack/OC-SORT) per need.
metadata:
  author: Promptstation
  version: 1.0.0
  category: computer-vision
---

# Video Frame Ops

Turn hours of video into the right frames. You sample by task, extract reproducibly, dedupe ruthlessly, track with stable IDs, and budget storage honestly across tiers.

Optimize simultaneously for:

- task-matched samples
- reproducible extracts
- lean frame sets
- stable tracks
- honest budgets

Annotate deduped frames only; track IDs stable or explicitly handed off.

## Use Cases

### Annotation set

Trigger: user says 'label this video' or 'frames for training'

Steps:

1. Sample smart
2. Dedupe
3. Extract set
4. Annotate lean

Result: Cost-efficient labels.

### Tracking task

Trigger: user says 'count objects' or 'follow items'

Steps:

1. Detect per frame
2. Associate tracks
3. Eval ID switches
4. Ship counter

Result: Trusted tracks.

### Archive budget

Trigger: user says 'video storage exploding' or 'transcode policy'

Steps:

1. Tier by value
2. Transcode down
3. Purge per schedule
4. Track cost

Result: Affordable archive.

Ask yourself before starting:

- What is the smallest verifiable outcome the user needs?
- What evidence will prove the result is correct?
- Which failures are most likely, and how will each be detected?
- What scope, budget, or policy constraints apply?
- What artifact must remain for audit or reuse?

## Core Output Requirements

Every delivery with this skill must include:

- Sampling rationale
- ffmpeg commands
- Dedupe report
- Tracking eval
- ID policy
- Storage budget
- Transcode tiers
- Clip manifest

Never annotate raw 30fps streams or store everything at mezzanine quality.

## Phase 1 — Sample Smart

Uniform for coverage, keyframe/motion for events.

Plan with `scripts/frame_plan.py --minutes 60 --fps 1`.

Compare 3 strategies on pilot.

## Phase 2 — Extract Repro

ffmpeg commands versioned; seek exact.

Scale once; name deterministically.

Checksums per frame batch.

## Phase 3 — Dedupe

Hash consecutive; keep changes.

Annotate the lean set.

Report keep rate.

## Phase 4 — Track and Budget

Associate with ID discipline; eval switches.

Tier storage; purge scheduled.

Cost per hour tracked.

## Examples

### Example 1: Label savings

User says: "100 hours to label?"

Actions:

1. 1fps + motion filter
2. Deduped 90 percent
3. Annotated 4k frames
4. Model shipped

Result: Lean labels.

### Example 2: Counter live

User says: "Count items on belt."

Actions:

1. Tracked with ByteTrack
2. ID switches under 2 percent
3. Counter trusted
4. Audited weekly

Result: Working counter.

## Troubleshooting

### Seeks drift

Cause: Non-keyframe seeking

Fix:

1. Seek to keyframes
2. Map timestamps
3. Verify alignment
4. Lock commands

### Tracks swap IDs

Cause: Occlusion or similar look

Fix:

1. Tune association
2. Add re-ID
3. Eval switches
4. State limits

### Storage shock

Cause: Mezzanine everything

Fix:

1. Tier now
2. Transcode backlog
3. Purge scheduled
4. Budget alerts

## Checklists

Copy from `assets/checklists.md` into the delivery. Do not ship without all boxes checked or explicitly waived with a reason.

- Sample.
- Extract.
- Keep.

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

Avoid 30fps annotation; seek-drift extracts; dedupe-free sets; ID-chaos tracking; tier-free storage; command-free extraction.

## Bundled References

Read `references/video-frames.md` when sampling or extracting video.
Run `scripts/frame_plan.py` to plan frame sampling.
Copy `assets/checklists.md` into every delivery.
