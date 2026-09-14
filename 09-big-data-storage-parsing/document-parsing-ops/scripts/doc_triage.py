#!/usr/bin/env python3
"""Triage document folders by type/size/text signals (stdlib only)."""
import argparse, os, zipfile

def pdf_text_len(path):
    try:
        data = open(path, "rb").read()
    except OSError:
        return -1
    texts = 0
    for i in range(len(data)):
        if data[i:i + 2] == b"Tj" or data[i:i + 3] == b"TJ]":
            texts += 1
    return texts

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    args = ap.parse_args()
    rows = []
    for root, _, files in os.walk(args.dir):
        for f in files:
            p = os.path.join(root, f)
            try:
                sz = os.path.getsize(p)
            except OSError:
                continue
            ext = os.path.splitext(f)[1].lower()
            sig = ""
            if ext == ".pdf":
                n = pdf_text_len(p)
                sig = "native" if n > 20 else ("scanned?" if n >= 0 else "unreadable")
            elif ext in (".docx", ".xlsx", ".pptx"):
                try:
                    z = zipfile.ZipFile(p)
                    sig = "office-ok(%d)" % len(z.namelist())
                except Exception:
                    sig = "corrupt?"
            rows.append((ext, sz, sig, p))
    for ext, sz, sig, p in sorted(rows)[:100]:
        print("%-6s %8dKB %-14s %s" % (ext, sz // 1024, sig, p[-90:]))
    print("total=%d — bucket native/scanned/corrupt, rank by value." % len(rows))

if __name__ == "__main__":
    main()
