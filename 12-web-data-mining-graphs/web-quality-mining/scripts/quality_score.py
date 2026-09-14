#!/usr/bin/env python3
"""Sketch content quality signals from HTML (stdlib only)."""
import argparse, re
from html.parser import HTMLParser

class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text, self.links, self.words = 0, 0, []
        self._in_a = False
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self._in_a = True
            self.links += 1
    def handle_endtag(self, tag):
        if tag == "a":
            self._in_a = False
    def handle_data(self, d):
        ws = re.findall(r"[A-Za-z]+", d)
        self.text += len(ws)
        if not self._in_a:
            self.words += ws

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    args = ap.parse_args()
    p = P()
    p.feed(open(args.file, encoding="utf-8", errors="replace").read())
    uniq = len(set(w.lower() for w in p.words))
    print("words=%d content_words=%d links=%d uniq_ratio=%.2f" % (
        p.text, len(p.words), p.links, uniq / max(1, len(p.words))))
    score = 0
    score += 2 if len(p.words) > 300 else (1 if len(p.words) > 100 else 0)
    score += 1 if p.links < 100 else 0
    score += 1 if uniq / max(1, len(p.words)) > 0.4 else 0
    print("sketch_score=%d/4 (thin<300w, link-heavy, repetitive = junk smells)" % score)

if __name__ == "__main__":
    main()
