#!/usr/bin/env python3
"""Score egress incident severity from signals (stdlib only)."""
import argparse, json

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--signals", required=True, help="JSON: succ_drop_pct, ban_rate, scope, compliance")
    args = ap.parse_args()
    s = json.loads(open(args.signals, encoding="utf-8").read())
    score = 0
    score += 3 if s.get("succ_drop_pct", 0) > 50 else (2 if s.get("succ_drop_pct", 0) > 20 else 0)
    score += 2 if s.get("ban_rate", 0) > 0.2 else (1 if s.get("ban_rate", 0) > 0.05 else 0)
    score += 2 if s.get("scope") == "all" else (1 if s.get("scope") == "pool" else 0)
    score += 3 if s.get("compliance") else 0
    sev = "SEV-1" if score >= 6 else ("SEV-2" if score >= 3 else "SEV-3")
    print("score=%d -> %s" % (score, sev))
    print({"SEV-1": "page all, IC now, 15-min cadence",
           "SEV-2": "page on-call, 30-min cadence",
           "SEV-3": "ticket, daily updates"}[sev])

if __name__ == "__main__":
    main()
