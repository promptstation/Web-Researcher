#!/usr/bin/env python3
"""Sentence-aware chunking with overlap + token estimate (stdlib only)."""
import argparse, json, re

def sents(text):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True)
    ap.add_argument("--max-tokens", type=int, default=400)
    ap.add_argument("--overlap", type=int, default=1)
    args = ap.parse_args()
    text = open(args.inp, encoding="utf-8").read()
    ss = sents(text)
    chunks, cur, cur_tok = [], [], 0
    for s in ss:
        t = max(1, len(s.split()) * 4 // 3)
        if cur_tok + t > args.max_tokens and cur:
            chunks.append(cur)
            cur, cur_tok = cur[-args.overlap:], sum(max(1, len(x.split()) * 4 // 3) for x in cur[-args.overlap:])
        cur.append(s)
        cur_tok += t
    if cur:
        chunks.append(cur)
    print("sentences=%d chunks=%d" % (len(ss), len(chunks)))
    for i, c in enumerate(chunks[:5]):
        print("--- chunk %d (~%d tok)" % (i, sum(len(x.split()) for x in c) * 4 // 3))
        print((" ".join(c))[:400])

if __name__ == "__main__":
    main()
