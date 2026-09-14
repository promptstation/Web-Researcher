#!/usr/bin/env python3
"""Fetch robots.txt + ai.txt signals (stdlib only)."""
import argparse, urllib.request

def get(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "ai-signals-check/1.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            return r.read().decode("utf-8", "replace")
    except Exception as e:
        return "FETCH-FAIL %s" % e

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", required=True, help="https://example.com")
    args = ap.parse_args()
    base = args.site.rstrip("/")
    robots = get(base + "/robots.txt")
    print("== robots.txt ==")
    for line in robots.splitlines():
        if any(k in line.lower() for k in ("ai", "bot", "crawl", "disallow", "user-agent")):
            print("  " + line[:120])
    ai = get(base + "/ai.txt")
    print("== ai.txt: %s ==" % ("present" if not ai.startswith("FETCH-FAIL") else "absent"))
    if not ai.startswith("FETCH-FAIL"):
        print(ai[:1500])
    print("honor all; check registries; log signal state per source.")

if __name__ == "__main__":
    main()
