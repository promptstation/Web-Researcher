#!/usr/bin/env python3
"""Dry-run retention sweeps by mtime (stdlib only)."""
import argparse, os, time

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--older-than", type=int, default=365, help="days")
    ap.add_argument("--dry-run", action="store_true", default=True)
    args = ap.parse_args()
    cut = time.time() - args.older_than * 86400
    cand, bytes_ = 0, 0
    for root, _, files in os.walk(args.root):
        for f in files:
            p = os.path.join(root, f)
            try:
                st = os.stat(p)
            except OSError:
                continue
            if st.st_mtime < cut:
                cand += 1
                bytes_ += st.st_size
    print("candidates older than %dd: files=%d bytes=%.1fMB (DRY RUN - nothing deleted)" % (
        args.older_than, cand, bytes_ / 1e6))
    print("next: verify against retention table, archive first, then delete with manifest proof.")

if __name__ == "__main__":
    main()
