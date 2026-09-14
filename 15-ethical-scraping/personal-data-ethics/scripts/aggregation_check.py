#!/usr/bin/env python3
"""Tier re-identification risk from field lists (stdlib only)."""
import argparse, json

W = {"name": 3, "email": 3, "phone": 3, "face": 3, "address": 3, "dob": 2, "employer": 1,
     "city": 1, "photo": 2, "username": 2, "posts": 1, "location_history": 3}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fields", required=True, help="comma field names")
    args = ap.parse_args()
    fs = [f.strip().lower() for f in args.fields.split(",")]
    score = sum(W.get(f, 0) for f in fs)
    print("fields=%d risk_score=%d" % (len(fs), score))
    print("verdict=%s" % ("REFUSE-or-aggregate-only" if score >= 6 else ("defuse+gate" if score >= 3 else "low-tread-careful")))
    print("then mosaic-test with outsiders; scores guide, tests decide.")

if __name__ == "__main__":
    main()
