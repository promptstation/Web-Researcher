#!/usr/bin/env python3
"""Scaffold lawful-basis records (stdlib only)."""
import argparse, json
from datetime import date

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--flow", required=True)
    ap.add_argument("--out", default="")
    args = ap.parse_args()
    pack = {
        "flow": args.flow, "date": str(date.today()),
        "purpose": "FILL narrow explicit purpose",
        "basis": "FILL consent|contract|legal|legitimate-interest (+regime)",
        "necessity": "FILL why less data cannot achieve purpose",
        "data": [], "retention_days": "FILL",
        "safeguards": ["minimization", "access-control", "retention"],
        "opt_out": "FILL mechanism + tested",
        "counsel_sign": "FILL name+date", "review_date": "FILL",
    }
    text = json.dumps(pack, indent=1)
    if args.out:
        open(args.out, "w").write(text)
        print("wrote %s — fill, sign, gate launch." % args.out)
    else:
        print(text)

if __name__ == "__main__":
    main()
