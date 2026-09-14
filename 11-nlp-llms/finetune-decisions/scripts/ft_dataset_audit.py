#!/usr/bin/env python3
"""Audit instruction-tuning JSONL: format, lengths, dupes (stdlib only)."""
import argparse, hashlib, json
from collections import Counter

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True)
    args = ap.parse_args()
    n, bad, lens, seen, dupes = 0, 0, [], set(), 0
    roles = Counter()
    for line in open(args.inp, encoding="utf-8"):
        try:
            r = json.loads(line)
        except Exception:
            bad += 1
            continue
        n += 1
        msgs = r.get("messages", [])
        if not msgs:
            bad += 1
            continue
        roles.update(m.get("role", "?") for m in msgs)
        text = " ".join(m.get("content", "") for m in msgs)
        lens.append(len(text.split()))
        h = hashlib.sha256(text.encode()).hexdigest()[:16]
        if h in seen:
            dupes += 1
        seen.add(h)
    lens.sort()
    print("n=%d bad=%d dupes=%d roles=%s" % (n, bad, dupes, dict(roles)))
    if lens:
        print("words p50=%d p95=%d max=%d" % (lens[len(lens)//2], lens[int(len(lens)*0.95)], lens[-1]))
    print("gate: bad=0, dupes~0, rubric-grade 200+ before tuning.")

if __name__ == "__main__":
    main()
