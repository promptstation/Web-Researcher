#!/usr/bin/env python3
"""Capture redirect chains + gate headers politely (stdlib only)."""
import argparse, sys, urllib.request

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

EDGE = ["x-middleware-rewrite", "x-middleware-next", "x-vercel-cache", "cf-mitigated",
        "x-robots-tag", "retry-after", "location", "set-cookie", "server"]

def once(url, timeout):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 gate-probe"})
    opener = urllib.request.build_opener(NoRedirect)
    try:
        r = opener.open(req, timeout=timeout)
        return r.status, dict(r.headers.items()), r.geturl()
    except urllib.request.HTTPError as e:
        return e.code, dict(e.headers.items()), url
    except Exception as e:
        return 0, {"error": str(e)}, url

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", required=True)
    ap.add_argument("--hops", type=int, default=5)
    ap.add_argument("--timeout", type=int, default=15)
    args = ap.parse_args()
    cur = args.url
    for i in range(args.hops):
        st, h, final = once(cur, args.timeout)
        print("hop %d: %s %s" % (i, st, cur[:120]))
        for k in EDGE:
            for hk, hv in h.items():
                if hk.lower() == k:
                    print("    %s: %.160s" % (hk, hv))
        loc = h.get("Location") or h.get("location")
        if st in (301, 302, 303, 307, 308) and loc:
            cur = urllib.request.urljoin(cur, loc)
            continue
        print("terminal: %s at %s" % (st, final[:120]))
        break

if __name__ == "__main__":
    main()
