#!/usr/bin/env python3
"""Vendor/DPA register with renewal alerts (stdlib sqlite)."""
import argparse, sqlite3, time

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default="vendors.db")
    ap.add_argument("cmd", choices=["add", "list", "due"])
    ap.add_argument("--vendor", default="")
    ap.add_argument("--tier", default="medium")
    ap.add_argument("--dpa", default="no")
    ap.add_argument("--renew-days", type=int, default=365)
    args = ap.parse_args()
    c = sqlite3.connect(args.db)
    c.execute("CREATE TABLE IF NOT EXISTS v(name TEXT PRIMARY KEY, tier TEXT, dpa TEXT, renew REAL)")
    if args.cmd == "add":
        c.execute("INSERT OR REPLACE INTO v VALUES(?,?,?,?)",
                  (args.vendor, args.tier, args.dpa, time.time() + args.renew_days * 86400))
        c.commit()
        print("registered (no data flows until dpa=yes)")
    elif args.cmd == "list":
        for r in c.execute("SELECT name,tier,dpa FROM v"):
            print("%-30s %-8s dpa=%s" % (r[0][:30], r[1], r[2]))
    else:
        for r in c.execute("SELECT name FROM v WHERE renew<?", (time.time() + 60 * 86400,)):
            print("RENEW-SOON " + r[0])

if __name__ == "__main__":
    main()
