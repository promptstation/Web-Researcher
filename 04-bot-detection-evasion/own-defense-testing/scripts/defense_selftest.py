#!/usr/bin/env python3
"""Gentle limit/challenge probe for OWNED staging (stdlib only)."""
import argparse, sys, time, urllib.request

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", required=True)
    ap.add_argument("--rate", type=float, default=2.0, help="req/sec, keep tiny")
    ap.add_argument("--count", type=int, default=20)
    ap.add_argument("--timeout", type=int, default=15)
    args = ap.parse_args()
    if args.rate > 5:
        print("refusing: keep self-test rate <= 5 rps", file=sys.stderr)
        sys.exit(2)
    print("scope-confirm: you own %s or hold written authorization. Ctrl-C otherwise." % args.target)
    time.sleep(2)
    codes = {}
    for i in range(args.count):
        req = urllib.request.Request(args.target, headers={"User-Agent": "SelfTest/1.0 (authorized)"})
        try:
            r = urllib.request.urlopen(req, timeout=args.timeout)
            code = r.status
            body = r.read(2000).decode("utf-8", "replace").lower()
            mark = "challenge?" if ("captcha" in body or "verify you are human" in body) else "ok"
        except Exception as e:
            code, mark = "ERR", str(e)[:60]
        codes[code] = codes.get(code, 0) + 1
        print("%d %s %s" % (i, code, mark))
        time.sleep(1.0 / args.rate)
    print("summary: %s" % codes)

if __name__ == "__main__":
    main()
