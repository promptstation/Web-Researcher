#!/usr/bin/env python3
"""Extract title, links, text blocks from HTML (stdlib only)."""
import argparse, json
from html.parser import HTMLParser

class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title, self._in = "", None
        self.links, self.blocks, self._buf = [], [], ""

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self._in = "title"
        if tag == "a" and a.get("href"):
            self.links.append(a["href"][:200])
        if tag in ("p", "h1", "h2", "h3", "li", "td"):
            self._flush()

    def handle_endtag(self, tag):
        if tag == "title":
            self._in = None
        if tag in ("p", "h1", "h2", "h3", "li", "td"):
            self._flush()

    def handle_data(self, d):
        d = d.strip()
        if not d:
            return
        if self._in == "title":
            self.title += d + " "
        else:
            self._buf += d + " "

    def _flush(self):
        t = " ".join(self._buf.split())
        if len(t) > 40:
            self.blocks.append(t[:2000])
        self._buf = ""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    args = ap.parse_args()
    p = P()
    p.feed(open(args.file, encoding="utf-8", errors="replace").read())
    p._flush()
    print(json.dumps({"title": p.title.strip()[:200], "links": len(p.links),
                      "blocks": len(p.blocks)}, indent=1))
    for b in p.blocks[:5]:
        print("  - %.150s" % b)

if __name__ == "__main__":
    main()
