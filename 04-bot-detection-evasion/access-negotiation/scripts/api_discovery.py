#!/usr/bin/env python3
"""Discover official APIs, feeds, docs (stdlib only)."""
import argparse, sys, urllib.request

PATHS = ["/developers", "/api", "/api/docs", "/openapi.json", "/swagger.json",
         "/robots.txt", "/sitemap.xml", "/feed", "/rss.xml", "/atom.xml",
         "/data", "/datasets", "/bulk", "/downloads"]

def hit(origin, path, timeout):
    url = origin.rstrip("/") + path
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 channel-discovery"}, method="HEAD")
    try:
        r = urllib.request.urlopen(req, timeout=timeout)
        return r.status
    except Exception as e:
        return "ERR %s" % str(e)[:40]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", required=True)
    ap.add_argument("--timeout", type=int, default=12)
    args = ap.parse_args()
    for p in PATHS:
        print("%-16s %s" % (p, hit(args.site, p, args.timeout)))
    print("follow up 200s by hand; prefer docs + bulk over page scraping.")

if __name__ == "__main__":
    main()
