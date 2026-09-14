#!/usr/bin/env python3
"""Scaffold jurisdiction maps (stdlib only)."""
import argparse, json

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--assets", default="assets.json", help="JSON list {name,countries[]}")
    ap.add_argument("--out", default="")
    args = ap.parse_args()
    try:
        assets = json.load(open(args.assets, encoding="utf-8"))
    except Exception:
        assets = [{"name": "example-db", "countries": ["US", "DE"]}]
    rows = ["| Asset | Countries | Counsel | Notes |", "|---|---|---|---|"]
    for a in assets:
        rows.append("| %s | %s | FILL | FILL |" % (a.get("name"), ",".join(a.get("countries", []))))
    text = "# Jurisdiction Map\n\n" + "\n".join(rows) + "\n"
    if args.out:
        open(args.out, "w").write(text)
        print("wrote %s" % args.out)
    else:
        print(text)

if __name__ == "__main__":
    main()
