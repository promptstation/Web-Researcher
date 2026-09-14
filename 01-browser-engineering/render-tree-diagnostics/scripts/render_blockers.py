#!/usr/bin/env python3
"""Fetch-side render-blocker audit using only the standard library."""
import argparse, re, sys, urllib.request

HEAD_RE = re.compile(r"<head.*?>(.*?)</head>", re.S | re.I)
SCRIPT_RE = re.compile(r"<script\b([^>]*)>", re.I)
LINK_RE = re.compile(r"<link\b([^>]*)>", re.I)
TAG_RE = re.compile(r"<[a-zA-Z][^>]*>")

def attrs(tag):
    return dict(re.findall(r'(\w+)(?:\s*=\s*["\']([^"\']*)["\'])?', tag))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", required=True)
    ap.add_argument("--timeout", type=int, default=25)
    args = ap.parse_args()
    req = urllib.request.Request(args.url, headers={"User-Agent": "Mozilla/5.0 render-audit"})
    try:
        html = urllib.request.urlopen(req, timeout=args.timeout).read().decode("utf-8", "replace")
    except Exception as e:
        print("fetch failed: %s" % e, file=sys.stderr)
        sys.exit(2)
    head = HEAD_RE.search(html)
    head_html = head.group(1) if head else html[:20000]
    scripts = SCRIPT_RE.findall(head_html)
    links = LINK_RE.findall(head_html)
    blocking_js, deferred, asyncd = [], [], []
    for s in scripts:
        a = {k.lower(): (v or "") for k, v in attrs(s)}
        src = a.get("src", "")
        if "defer" in a:
            deferred.append(src or "inline")
        elif "async" in a:
            asyncd.append(src or "inline")
        else:
            blocking_js.append(src or "inline")
    blocking_css, gated_css, preloads = [], [], []
    for l in links:
        a = {k.lower(): (v or "") for k, v in attrs(l)}
        rel = a.get("rel", "")
        if rel == "stylesheet":
            (gated_css if a.get("media", "all") not in ("", "all") else blocking_css).append(a.get("href", ""))
        elif rel == "preload":
            preloads.append(a.get("href", ""))
    print("dom_tags_estimate: %d" % len(TAG_RE.findall(html)))
    print("html_bytes: %d" % len(html))
    print("blocking_scripts_in_head: %d" % len(blocking_js))
    for s in blocking_js[:20]:
        print("  BLOCK-JS %s" % s)
    print("deferred: %d async: %d" % (len(deferred), len(asyncd)))
    print("blocking_css: %d gated_css: %d preloads: %d" % (len(blocking_css), len(gated_css), len(preloads)))
    for s in blocking_css[:20]:
        print("  BLOCK-CSS %s" % s)

if __name__ == "__main__":
    main()
