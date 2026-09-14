#!/usr/bin/env python3
"""Enumerate SPA routes: sitemap + bundle paths (stdlib only)."""
import argparse, re, sys, urllib.request

def fetch(url, timeout, cap=500000):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 route-miner"})
    return urllib.request.urlopen(req, timeout=timeout).read(cap).decode("utf-8", "replace")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", required=True, help="origin like https://example.com")
    ap.add_argument("--timeout", type=int, default=20)
    args = ap.parse_args()
    routes = set()
    try:
        sm = fetch(args.site.rstrip("/") + "/sitemap.xml", args.timeout)
        for u in re.findall(r"<loc>([^<]+)</loc>", sm)[:500]:
            routes.add(u)
        print("sitemap_urls: %d" % len(routes))
    except Exception as e:
        print("sitemap: %s" % e)
    try:
        html = fetch(args.site, args.timeout)
    except Exception as e:
        print("fetch failed: %s" % e, file=sys.stderr)
        sys.exit(2)
    for p in re.findall(r'path\s*:\s*["\'](/[A-Za-z0-9/_:.-]*)["\']', html):
        routes.add(args.site.rstrip("/") + p)
    for s in re.findall(r'<script[^>]+src="([^"]+\.js[^"]*)"', html)[:4]:
        try:
            js = fetch(urllib.request.urljoin(args.site, s), args.timeout, 300000)
        except Exception:
            continue
        for p in re.findall(r'["\'](/[a-z][A-Za-z0-9/_-]{1,60})["\']', js):
            if "." not in p.split("/")[-1]:
                routes.add(args.site.rstrip("/") + p)
    print("routes_total: %d" % len(routes))
    for r in sorted(routes)[:100]:
        print("  %s" % r)

if __name__ == "__main__":
    main()
