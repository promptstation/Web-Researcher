#!/usr/bin/env python3
"""Scaffold research ethics review packs (stdlib only)."""
import argparse

TPL = """# Ethics Review: {name}
## Questions + pre-registration link
FILL
## Methods (subjects? deception? data?)
FILL
## Risks + mitigations
FILL
## Vulnerable populations screen
FILL
## Consent + debrief plan
FILL
## Repro plan + limits
FILL
## Board decision + date
FILL
"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--study", required=True)
    ap.add_argument("--out", default="")
    args = ap.parse_args()
    text = TPL.format(name=args.study)
    if args.out:
        open(args.out, "w").write(text)
        print("wrote %s" % args.out)
    else:
        print(text)

if __name__ == "__main__":
    main()
