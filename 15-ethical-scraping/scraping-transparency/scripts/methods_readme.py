#!/usr/bin/env python3
"""Draft methods README (stdlib only)."""
import argparse
from datetime import date

TPL = """# Methods: {name} ({today})
## Sources
FILL: sites/feeds + why + terms basis.
## Collection
FILL: tools/versions, rates, windows, robots handling.
## Processing
FILL: cleaning, dedupe, filters, versions.
## QA
FILL: evals, audits, error rates.
## Limits
FILL: coverage, bias, freshness, exclusions.
## Contact + corrections
FILL
"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", required=True)
    ap.add_argument("--out", default="")
    args = ap.parse_args()
    text = TPL.format(name=args.project, today=date.today())
    if args.out:
        open(args.out, "w").write(text)
        print("wrote %s" % args.out)
    else:
        print(text)

if __name__ == "__main__":
    main()
