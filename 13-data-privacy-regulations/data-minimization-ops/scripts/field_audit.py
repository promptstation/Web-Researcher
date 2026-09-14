#!/usr/bin/env python3
"""Scaffold field necessity reviews from a schema JSON (stdlib only)."""
import argparse, json

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schema", required=True, help="JSON: {fields:[{name,type,pii}] }")
    ap.add_argument("--out", default="")
    args = ap.parse_args()
    spec = json.load(open(args.schema, encoding="utf-8"))
    rows = ["| Field | Type | PII? | Purpose link | Decision | Owner |",
            "|---|---|---|---|---|---|"]
    for f in spec.get("fields", []):
        rows.append("| %s | %s | %s | FILL | keep/drop/mask/aggregate | FILL |" % (
            f.get("name"), f.get("type", "?"), f.get("pii", "?")))
    text = "# Field Necessity Review\n\n" + "\n".join(rows) + "\n"
    if args.out:
        open(args.out, "w").write(text)
        print("wrote %s — decide every row, drop undecided." % args.out)
    else:
        print(text)

if __name__ == "__main__":
    main()
