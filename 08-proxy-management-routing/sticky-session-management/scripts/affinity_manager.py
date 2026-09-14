#!/usr/bin/env python3
"""Generate + audit account-to-egress affinity maps (stdlib only)."""
import argparse, json, sys

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--accounts", default="a1,a2,a3")
    ap.add_argument("--egress", default="e1,e2,e3,e4")
    ap.add_argument("--audit", default="")
    args = ap.parse_args()
    if args.audit:
        m = json.load(open(args.audit, encoding="utf-8"))
        seen, dup = set(), []
        for acc, egr in m.items():
            if egr in seen:
                dup.append((acc, egr))
            seen.add(egr)
        print("pins=%d shared_egress=%s" % (len(m), dup or "none - OK"))
        sys.exit(1 if dup else 0)
    accs = args.accounts.split(",")
    egrs = args.egress.split(",")
    if len(egrs) < len(accs):
        print("need >= 1 egress per account", file=sys.stderr)
        sys.exit(2)
    m = {a: egrs[i % len(egrs)] for i, a in enumerate(accs)}
    print(json.dumps(m, indent=1))
    print("save as affinity.json; audit in CI for 1:1 discipline.")

if __name__ == "__main__":
    main()
