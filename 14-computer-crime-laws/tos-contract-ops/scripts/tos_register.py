#!/usr/bin/env python3
"""ToS register: add/list/review-due (stdlib sqlite)."""
import argparse, sqlite3, time

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default="tos.db")
    ap.add_argument("cmd", choices=["add", "list", "due"])
    ap.add_argument("--target", default="")
    ap.add_argument("--position", default="review")
    ap.add_argument("--review-days", type=int, default=90)
    args = ap.parse_args()
    c = sqlite3.connect(args.db)
    c.execute("CREATE TABLE IF NOT EXISTS t(target TEXT PRIMARY KEY, pos TEXT, ts REAL, review REAL)")
    if args.cmd == "add":
        now = time.time()
        c.execute("INSERT OR REPLACE INTO t VALUES(?,?,?,?)",
                  (args.target, args.position, now, now + args.review_days * 86400))
        c.commit()
        print("registered")
    elif args.cmd == "list":
        for r in c.execute("SELECT target,pos FROM t"):
            print("%-45s %s" % (r[0][:45], r[1]))
    else:
        for r in c.execute("SELECT target FROM t WHERE review<?", (time.time(),)):
            print("REVIEW-DUE " + r[0])

if __name__ == "__main__":
    main()
