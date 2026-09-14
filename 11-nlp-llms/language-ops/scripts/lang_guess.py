#!/usr/bin/env python3
"""Script-ratio + stopword language sketch (stdlib only)."""
import argparse, re
from collections import Counter

STOPS = {"en": "the and of to in", "fr": "le la les des une", "de": "der die und den",
         "es": "el la los las una"}

def scripts(text):
    c = Counter()
    for ch in text:
        o = ord(ch)
        if o < 128:
            c["latin"] += 1
        elif 0x4E00 <= o <= 0x9FFF or 0x3040 <= o <= 0x30FF:
            c["cjk"] += 1
        elif 0x0600 <= o <= 0x06FF:
            c["arabic"] += 1
        elif 0x0400 <= o <= 0x04FF:
            c["cyrillic"] += 1
        else:
            c["other"] += 1
    return c

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True)
    args = ap.parse_args()
    for i, line in enumerate(open(args.inp, encoding="utf-8")):
        line = line.strip()
        if not line:
            continue
        sc = scripts(line)
        dom = sc.most_common(1)[0][0]
        guess = dom
        if dom == "latin":
            words = set(re.findall(r"[a-z]+", line.lower()))
            best = max(STOPS, key=lambda L: len(words & set(STOPS[L].split())))
            guess = "latin:%s?" % best
        print("line%d: %s %s" % (i + 1, guess, dict(sc)))
    print("sketch only — production uses fasttext-class models + thresholds.")

if __name__ == "__main__":
    main()
