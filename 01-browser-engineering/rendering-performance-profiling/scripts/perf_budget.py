#!/usr/bin/env python3
"""Transfer-weight budget check using only the standard library."""
import argparse, re, sys, urllib.request

RES_RE = re.compile(r"(?:src|href)\s*=\s*[\"']([^\"']+)\"", re.I)

def size_of(url, timeout):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 perf-budget"}, method="HEAD")
    try:
        r = urllib.request.urlopen(req, timeout=timeout)
        n = r.headers.get("Content-Length")
        return int(n) if n else -1
    except Exception:
        return -1

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", required=True)
    ap.add_argument("--timeout", type=int, default=20)
    ap.add_argument("--budget-js-kb", type=int, default=300)
    ap.add_argument("--budget-img-kb", type=int, default=800)
    ap.add_argument("--max-assets", type=int, default=40)
    args = ap.parse_args()
    html = urllib.request.urlopen(urllib.request.Request(
        args.url, headers={"User-Agent": "Mozilla/5.0 perf-budget"}),
        timeout=args.timeout).read().decode("utf-8", "replace")
    print("html_bytes: %d" % len(html))
    urls = []
    for m in RES_RE.findall(html):
        if m.startswith(("data:", "#", "javascript:")):
            continue
        urls.append(urllib.request.urljoin(args.url, m))
    seen, js_b, img_b, unknown = set(), 0, 0, 0
    for u in urls:
        if u in seen:
            continue
        seen.add(u)
        if len(seen) > args.max_assets:
            break
        s = size_of(u, args.timeout)
        low = u.lower()
        if s < 0:
            unknown += 1
            continue
        if low.endswith(".js"):
            js_b += s
        elif low.endswith((".png", ".jpg", ".jpeg", ".webp", ".avif", ".gif", ".svg")):
            img_b += s
    print("assets_seen: %d unknown_size: %d" % (len(seen), unknown))
    print("js_kb~%d budget=%d %s" % (js_b // 1024, args.budget_js_kb,
          "PASS" if js_b // 1024 <= args.budget_js_kb else "FAIL"))
    print("img_kb~%d budget=%d %s" % (img_b // 1024, args.budget_img_kb,
          "PASS" if img_b // 1024 <= args.budget_img_kb else "FAIL"))

if __name__ == "__main__":
    main()
