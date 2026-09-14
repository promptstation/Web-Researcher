#!/usr/bin/env python3
"""Mine JSON API endpoints from HAR files (stdlib only)."""
import argparse, json, urllib.parse
from collections import Counter

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--har", required=True)
    ap.add_argument("--limit", type=int, default=30)
    args = ap.parse_args()
    har = json.load(open(args.har, encoding="utf-8"))
    entries = har.get("log", {}).get("entries", [])
    hits = Counter()
    samples = {}
    for e in entries:
        req = e.get("request", {})
        resp = e.get("response", {})
        url = req.get("url", "")
        ctype = ""
        for h in resp.get("headers", []):
            if h.get("name", "").lower() == "content-type":
                ctype = h.get("value", "")
        if "json" not in ctype:
            continue
        u = urllib.parse.urlparse(url)
        key = "%s %s://%s%s" % (req.get("method", "?"), u.scheme, u.netloc, u.path)
        hits[key] += 1
        samples.setdefault(key, (u.query[:120], (resp.get("content", {}).get("text") or "")[:200]))
    print("json_endpoints: %d" % len(hits))
    for k, n in hits.most_common(args.limit):
        print("%dx %s" % (n, k))
        print("    query=%.100s" % samples[k][0])
    print("verify live, then document auth + paging + schema.")

if __name__ == "__main__":
    main()
