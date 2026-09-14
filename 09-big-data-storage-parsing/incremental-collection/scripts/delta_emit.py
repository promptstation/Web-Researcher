#!/usr/bin/env python3
"""Emit insert/update deltas vs sqlite hash state (stdlib only)."""
import argparse, hashlib, json, sqlite3

def h(rec):
    core = {k: v for k, v in rec.items() if k not in ("fetched_at", "_raw")}
    return hashlib.sha256(json.dumps(core, sort_keys=True).encode()).hexdigest()[:16]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True)
    ap.add_argument("--state", default="hashes.db")
    ap.add_argument("--key", default="record_id")
    ap.add_argument("--out", default="delta.jsonl")
    args = ap.parse_args()
    c = sqlite3.connect(args.state)
    c.execute("CREATE TABLE IF NOT EXISTS h(k TEXT PRIMARY KEY, hv TEXT)")
    ins = upd = same = 0
    out = open(args.out, "w", encoding="utf-8")
    for line in open(args.inp, encoding="utf-8"):
        try:
            r = json.loads(line)
        except Exception:
            continue
        k = str(r.get(args.key, ""))
        hv = h(r)
        row = c.execute("SELECT hv FROM h WHERE k=?", (k,)).fetchone()
        if not row:
            ins += 1
            out.write(json.dumps({"op": "insert", "id": k, "rec": r}) + "\n")
        elif row[0] != hv:
            upd += 1
            out.write(json.dumps({"op": "update", "id": k, "rec": r}) + "\n")
        else:
            same += 1
        c.execute("INSERT OR REPLACE INTO h VALUES(?,?)", (k, hv))
    c.commit()
    print("insert=%d update=%d unchanged=%d delta=%s" % (ins, upd, same, args.out))

if __name__ == "__main__":
    main()
