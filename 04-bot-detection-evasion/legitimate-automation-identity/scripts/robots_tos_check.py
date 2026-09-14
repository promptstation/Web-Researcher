#!/usr/bin/env python3
"""Fetch robots.txt + summarize rules and ToS hints (stdlib only)."""
import argparse, sys, urllib.request, urllib.robotparser

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", required=True)
    ap.add_argument("--ua", required=True)
    ap.add_argument("--timeout", type=int, default=15)
    args = ap.parse_args()
    origin = args.site.rstrip("/")
    rp = urllib.robotparser.RobotFileParser()
    try:
        rp.set_url(origin + "/robots.txt")
        rp.read()
    except Exception as e:
        print("robots fetch failed: %s (treat as minimal-polite, still review ToS)" % e)
        return
    print("sitemaps: %s" % (rp.site_maps() or ["none listed"]))
    delay = rp.crawl_delay(args.ua)
    print("crawl_delay for %r: %s" % (args.ua, delay))
    for path in ["/", "/api/", "/search", "/login"]:
        print("can_fetch %-8s %s" % (path, rp.can_fetch(args.ua, origin + path)))
    print("note: also review Terms of Service automation clauses before collecting.")

if __name__ == "__main__":
    main()
