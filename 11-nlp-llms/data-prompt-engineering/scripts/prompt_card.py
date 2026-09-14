#!/usr/bin/env python3
"""Scaffold versioned prompt cards (stdlib only)."""
import argparse
from datetime import date

TPL = """# Prompt: {task} v1 ({today})
model: FILL (pinned)
temperature: 0
## Instructions
FILL: role, task, constraints, format, edge cases.
## Few-shots (4-12, one per class + edges)
1. FILL input -> FILL output (why: FILL)
## Output contract
FILL: exact labels / enum / JSON schema.
## Eval
suite=FILL thresholds=FILL
## Changelog
v1: initial.
"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--task", required=True)
    ap.add_argument("--out", default="")
    args = ap.parse_args()
    text = TPL.format(task=args.task, today=date.today())
    if args.out:
        open(args.out, "w").write(text)
        print("wrote %s" % args.out)
    else:
        print(text)

if __name__ == "__main__":
    main()
