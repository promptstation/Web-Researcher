#!/usr/bin/env python3
"""Verify proxy exit IP via echo endpoints (stdlib only)."""
import argparse, json, urllib.request

ECHO = ["https://api.ipify.org?format=json", "https://ifconfig.me/ip"]

def via(proxy, url, timeout=15):
    req = urllib.request.Request(url, headers={"User-Agent": "exit-verify/1.0"})
    if proxy:
        req.set_proxy(proxy, "https" if url.startswith("https") else "http")
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace").strip()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--proxy", default="")
    args = ap.parse_args()
    for u in ECHO:
        try:
            out = via(args.proxy, u)
            try:
                out = json.loads(out).get("ip", out)
            except Exception:
                pass
            print("%s -> %s" % (u.split("/")[2], out[:60]))
        except Exception as e:
            print("%s -> ERROR %s" % (u.split("/")[2], e))
    print("cross-check IP in two geo DBs + ASN whois; log all five signals.")

if __name__ == "__main__":
    main()
