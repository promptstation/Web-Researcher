#!/usr/bin/env python3
"""Draft a vision model card (stdlib only)."""
import argparse
from datetime import date

TPL = """# Model Card: {name} ({today})
## Purpose
FILL: task, intended users, out-of-scope uses.
## Data
FILL: sources, licenses, sizes, splits, seed.
## Eval
headline=FILL sliced=FILL ece=FILL robustness=FILL fairness=FILL
## Limits
FILL: known failures, OOD behavior, sensitive slices.
## Serving
latency_p95=FILL version=FILL rollback=FILL
## Owner
FILL | review_date=FILL
"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--out", default="")
    args = ap.parse_args()
    text = TPL.format(name=args.model, today=date.today())
    if args.out:
        open(args.out, "w").write(text)
        print("wrote %s — fill FILLs, review, then serve." % args.out)
    else:
        print(text)

if __name__ == "__main__":
    main()
