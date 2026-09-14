#!/usr/bin/env python3
"""Mine Next.js payloads + data-route templates (stdlib only)."""
import argparse, json, re, sys, urllib.request

def fetch(url, timeout):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 next-miner"})
    r = urllib.request.urlopen(req, timeout=timeout)
    return r.geturl(), r.read().decode("utf-8", "replace")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", required=True)
    ap.add_argument("--timeout", type=int, default=20)
    args = ap.parse_args()
    try:
        final, html = fetch(args.url, args.timeout)
    except Exception as e:
        print("fetch failed: %s" % e, file=sys.stderr)
        sys.exit(2)
    print("final: %s" % final)
    m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html, re.S)
    if not m:
        print("no __NEXT_DATA__ found")
        sys.exit(0)
    try:
        data = json.loads(m.group(1))
    except Exception as e:
        print("payload parse failed: %s" % e, file=sys.stderr)
        sys.exit(2)
    print("buildId: %s" % data.get("buildId"))
    print("page: %s" % data.get("page"))
    print("locale: %s" % (data.get("locale") or "none"))
    props = (data.get("props") or {}).get("pageProps") or {}
    print("pageProps_keys: %s" % sorted(props.keys())[:40])
    print("isFallback: %s gsp: %s" % (data.get("isFallback"), bool(data.get("gsp"))))
    route = data.get("page", "/")
    print("dataroute_template: /_next/data/%s%s.json" % (data.get("buildId"), route.rstrip("/") or "/index"))

if __name__ == "__main__":
    main()
