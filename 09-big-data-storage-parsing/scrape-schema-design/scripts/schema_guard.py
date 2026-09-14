#!/usr/bin/env python3
"""Validate JSONL against a simple schema spec (stdlib only)."""
import argparse, json

def check(rec, spec):
    errs = []
    for f in spec.get("required", []):
        if f not in rec or rec[f] in (None, ""):
            errs.append("MISSING:" + f)
    for f, t in spec.get("types", {}).items():
        if f in rec and rec[f] is not None:
            want = {"int": int, "float": (int, float), "str": str, "bool": bool}.get(t)
            if want and not isinstance(rec[f], want):
                errs.append("TYPE:" + f)
    for f, vals in spec.get("enums", {}).items():
        if f in rec and rec[f] not in vals:
            errs.append("ENUM:" + f)
    for f, (lo, hi) in spec.get("ranges", {}).items():
        if f in rec and isinstance(rec[f], (int, float)) and not (lo <= rec[f] <= hi):
            errs.append("RANGE:" + f)
    return errs

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schema", required=True)
    ap.add_argument("--in", dest="inp", required=True)
    ap.add_argument("--quarantine", default="rejects.jsonl")
    args = ap.parse_args()
    spec = json.load(open(args.schema, encoding="utf-8"))
    ok = bad = 0
    q = open(args.quarantine, "w", encoding="utf-8")
    for line in open(args.inp, encoding="utf-8"):
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except Exception:
            bad += 1
            q.write(json.dumps({"_error": "BADJSON", "_raw": line[:200]}) + "\n")
            continue
        errs = check(rec, spec)
        if errs:
            bad += 1
            q.write(json.dumps({"_errors": errs, "_rec": rec}) + "\n")
        else:
            ok += 1
    print("ok=%d bad=%d rate=%.2f%% quarantined=%s" % (ok, bad, 100 * ok / max(1, ok + bad), args.quarantine))

if __name__ == "__main__":
    main()
