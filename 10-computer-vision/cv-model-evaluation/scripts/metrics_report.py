#!/usr/bin/env python3
"""Classification report from preds CSV: acc, per-class P/R/F1 (stdlib only)."""
import argparse, csv
from collections import Counter, defaultdict

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--preds", required=True, help="CSV with true,pred columns")
    args = ap.parse_args()
    rows = list(csv.DictReader(open(args.preds, encoding="utf-8")))
    n = len(rows)
    acc = sum(1 for r in rows if r["true"] == r["pred"]) / max(1, n)
    tp, fp, fn = Counter(), Counter(), Counter()
    for r in rows:
        t, p = r["true"], r["pred"]
        if t == p:
            tp[t] += 1
        else:
            fp[p] += 1
            fn[t] += 1
    print("n=%d accuracy=%.3f" % (n, acc))
    f1s = []
    for c in sorted(set(list(tp) + list(fp) + list(fn))):
        pr = tp[c] / max(1, tp[c] + fp[c])
        rc = tp[c] / max(1, tp[c] + fn[c])
        f1 = 2 * pr * rc / max(1e-9, pr + rc)
        f1s.append(f1)
        print("  %-18s P=%.3f R=%.3f F1=%.3f n=%d" % (c, pr, rc, f1, tp[c] + fn[c]))
    print("macro-F1=%.3f worst-F1=%.3f" % (sum(f1s) / max(1, len(f1s)), min(f1s or [0])))
    print("slice further by size/source/lighting; gate on worst, not mean.")

if __name__ == "__main__":
    main()
