#!/usr/bin/env python3
"""Scaffold stakeholder/harm analyses (stdlib only)."""
import argparse

TPL = """# Ethics Review: {name}
## Stakeholders (powerless first)
- subjects: FILL | sites: FILL | users: FILL | public: FILL
## Harms (likelihood x severity)
- privacy: FILL | economic: FILL | autonomy: FILL | dignitary: FILL
## Benefits (evidenced)
- FILL
## Least-harm alternatives tried
- FILL
## Consent rung + why
- FILL
## Decision + dissent + review date
- FILL
"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", required=True)
    ap.add_argument("--out", default="")
    args = ap.parse_args()
    text = TPL.format(name=args.project)
    if args.out:
        open(args.out, "w").write(text)
        print("wrote %s" % args.out)
    else:
        print(text)

if __name__ == "__main__":
    main()
