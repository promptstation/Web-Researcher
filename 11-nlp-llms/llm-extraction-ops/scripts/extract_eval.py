#!/usr/bin/env python3
"""Field-level P/R/F1 for extraction vs gold JSONL (stdlib only)."""
import argparse, json
from collections import Counter

def norm(v):
    return str(v).strip().lower()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gold", required=True)
    ap.add_argument("--pred", required=True)
    ap.add_argument("--key", default="id")
    args = ap.parse_args()
    gold = {}
    for line in open(args.gold, encoding="utf-8"):
        r = json.loads(line)
        gold[str(r.get(args.key))] = r
    tp, fp, fn = Counter(), Counter(), Counter()
    for line in open(args.pred, encoding="utf-8"):
        r = json.loads(line)
        g = gold.get(str(r.get(args.key)), {})
        fields = set(g) | set(r) - {args.key}
        for f in fields:
            gv, pv = g.get(f), r.get(f)
            if gv in (None, "") and pv in (None, ""):
                continue
            if gv not in (None, "") and pv not in (None, "") and norm(gv) == norm(pv):
                tp[f] += 1
            else:
                if pv not in (None, ""):
                    fp[f] += 1
                if gv not in (None, ""):
                    fn[f] += 1
    f1s = []
    for f in sorted(set(tp) | set(fp) | set(fn)):
        pr = tp[f] / max(1, tp[f] + fp[f])
        rc = tp[f] / max(1, tp[f] + fn[f])
        f1 = 2 * pr * rc / max(1e-9, pr + rc)
        f1s.append(f1)
        print("  %-20s P=%.3f R=%.3f F1=%.3f" % (f, pr, rc, f1))
    print("macro-F1=%.3f worst=%.3f — fix worst first." % (
        sum(f1s) / max(1, len(f1s)), min(f1s or [0])))

if __name__ == "__main__":
    main()
