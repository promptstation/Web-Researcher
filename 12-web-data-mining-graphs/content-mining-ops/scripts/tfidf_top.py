#!/usr/bin/env python3
"""TF-IDF top terms per doc + corpus (stdlib only)."""
import argparse, json, math, re
from collections import Counter, defaultdict

STOP = set("the a an and or of to in on for with is are was were be been this that it its as at by from".split())

def toks(s):
    return [w for w in re.findall(r"[a-z]{3,}", s.lower()) if w not in STOP]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True, help="JSONL with id,text")
    ap.add_argument("--top", type=int, default=8)
    args = ap.parse_args()
    docs = []
    for line in open(args.inp, encoding="utf-8"):
        try:
            r = json.loads(line)
        except Exception:
            continue
        docs.append((str(r.get("id")), toks(str(r.get("text", "")))))
    df = Counter()
    for _, t in docs:
        df.update(set(t))
    N = len(docs)
    for i, t in docs[:5]:
        tf = Counter(t)
        scored = sorted(((1 + math.log(c)) * math.log(N / max(1, df[w])), w) for w, c in tf.items())
        print("%s: %s" % (i[:40], [w for _, w in scored[-args.top:]][::-1]))
    print("docs=%d vocab=%d" % (N, len(df)))

if __name__ == "__main__":
    main()
