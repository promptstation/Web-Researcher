#!/usr/bin/env python3
"""Inventory embedded JSON state islands (stdlib only)."""
import argparse, json, re, sys, urllib.request

PAT = re.compile(r'<script([^>]*)>(.*?)</script>', re.S | re.I)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", required=True)
    ap.add_argument("--timeout", type=int, default=20)
    ap.add_argument("--max-show", type=int, default=8)
    args = ap.parse_args()
    req = urllib.request.Request(args.url, headers={"User-Agent": "Mozilla/5.0 state-miner"})
    try:
        html = urllib.request.urlopen(req, timeout=args.timeout).read().decode("utf-8", "replace")
    except Exception as e:
        print("fetch failed: %s" % e, file=sys.stderr)
        sys.exit(2)
    n = 0
    for attrs, body in PAT.findall(html):
        low = attrs.lower()
        if "application/json" not in low and "nuxt" not in low and "__" not in attrs:
            continue
        n += 1
        mid = re.search(r'id="([^"]+)"', attrs)
        print("--- island %d id=%s bytes=%d" % (n, mid.group(1) if mid else "?", len(body)))
        try:
            data = json.loads(body.strip())
            keys = list(data.keys()) if isinstance(data, dict) else ["list[%d]" % len(data)]
            print("keys: %s" % keys[:args.max_show])
        except Exception:
            print("keys: UNPARSEABLE-AS-JSON (reviver format?)")
    print("islands: %d" % n)

if __name__ == "__main__":
    main()
