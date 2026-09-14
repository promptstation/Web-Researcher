#!/usr/bin/env python3
"""Parse sitemap XML (index or urlset) from file (stdlib only)."""
import argparse, gzip, xml.etree.ElementTree as ET

def load(path):
    if path.endswith(".gz"):
        return gzip.open(path, "rb").read()
    return open(path, "rb").read()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    args = ap.parse_args()
    root = ET.fromstring(load(args.file))
    ns = {"s": root.tag.split("}")[0].strip("{")} if "}" in root.tag else {"s": ""}
    urls, maps = [], []
    for u in root.findall("s:url/s:loc", ns) or root.findall("url/loc"):
        urls.append(u.text)
    for u in root.findall("s:sitemap/s:loc", ns) or root.findall("sitemap/loc"):
        maps.append(u.text)
    lms = len(root.findall("s:url/s:lastmod", ns) or root.findall("url/lastmod"))
    print("type=%s urls=%d submaps=%d lastmod=%d" % (
        "index" if maps else "urlset", len(urls), len(maps), lms))
    for u in urls[:5]:
        print("  %.120s" % u)
    for u in maps[:5]:
        print("  map: %.120s" % u)

if __name__ == "__main__":
    main()
