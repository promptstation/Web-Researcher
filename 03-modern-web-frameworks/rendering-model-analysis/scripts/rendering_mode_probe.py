#!/usr/bin/env python3
"""Classify rendering model from fetched HTML (stdlib only)."""
import argparse, re, sys, urllib.request

MARKERS = {"__NEXT_DATA__": "Next.js", "__NUXT__": "Nuxt", "__NUXT_DATA__": "Nuxt",
           "ng-version": "Angular", "sveltekit:data": "SvelteKit",
           "data-reactroot": "React", "__APOLLO_STATE__": "Apollo"}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", required=True)
    ap.add_argument("--timeout", type=int, default=20)
    args = ap.parse_args()
    req = urllib.request.Request(args.url, headers={"User-Agent": "Mozilla/5.0 model-probe"})
    try:
        r = urllib.request.urlopen(req, timeout=args.timeout)
        html = r.read().decode("utf-8", "replace")
    except Exception as e:
        print("fetch failed: %s" % e, file=sys.stderr)
        sys.exit(2)
    print("bytes: %d final: %s" % (len(html), r.geturl()))
    found = [v for k, v in MARKERS.items() if k in html]
    print("framework_markers: %s" % (found or ["none"]))
    text = re.sub(r"<script.*?</script>", " ", html, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    print("text_chars: %d links: %d" % (len(text), html.lower().count("<a ")))
    root_empty = bool(re.search(r'<div id="(root|app)"[^>]*>\s*</div>', html))
    print("root_empty: %s" % root_empty)
    payloads = re.findall(r'<script[^>]*id="([^"]*(?:NEXT|NUXT|STATE)[^"]*)"', html)
    print("payload_scripts: %s" % (payloads or ["none"]))
    if len(text) > 2000:
        print("verdict: SSR-or-SSG fetch-first")
    elif payloads or found:
        print("verdict: payload-backed, parse payload or map API")
    else:
        print("verdict: likely-CSR, map API before reaching for browsers")

if __name__ == "__main__":
    main()
