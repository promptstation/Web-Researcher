#!/usr/bin/env python3
"""Draft team ethics charters (stdlib only)."""
import argparse
from datetime import date

TPL = """# Ethics Charter: {team} ({today})
## We do
- FILL: polite, lawful, consented, transparent collection.
## We refuse
- FILL: stalking, sabotage, deception, persecution tooling.
## How we decide
- stakeholder+harm memos, dissent protected, board binding.
## Escalation
- FILL: leads, board, whistle path (independent).
## Review
- yearly + on incident. Signed: FILL
"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--team", required=True)
    ap.add_argument("--out", default="")
    args = ap.parse_args()
    text = TPL.format(team=args.team, today=date.today())
    if args.out:
        open(args.out, "w").write(text)
        print("wrote %s — draft WITH the team, then sign." % args.out)
    else:
        print(text)

if __name__ == "__main__":
    main()
