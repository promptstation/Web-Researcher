#!/usr/bin/env python3
"""Transfer register: add/list/review (stdlib sqlite)."""
import argparse, sqlite3, time

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default="transfers.db")
    ap.add_argument("cmd", choices=["add", "list", "review-due"])
    ap.add_argument("--route", default="")
    ap.add_argument("--mechanism", default="")
    ap.add_argument("--review-days", type=int, default=365)
    args = ap.parse_args()
    c = sqlite3.connect(args.db)
    c.execute("CREATE TABLE IF NOT EXISTS t(route TEXT PRIMARY KEY, mech TEXT, ts REAL, review REAL)")
    if args.cmd == "add":
        now = time.time()
        c.execute("INSERT OR REPLACE INTO t VALUES(?,?,?,?)", (args.route, args.mechanism, now, now + args.review_days * 86400))
        c.commit()
        print("registered")
    elif args.cmd == "list":
        for r in c.execute("SELECT route,mech FROM t"):
            print("%-50s %s" % (r[0][:50], r[1]))
    else:
        for r in c.execute("SELECT route FROM t WHERE review<?", (time.time(),)):
            print("REVIEW-DUE " + r[0])

if __name__ == "__main__":
    main()
