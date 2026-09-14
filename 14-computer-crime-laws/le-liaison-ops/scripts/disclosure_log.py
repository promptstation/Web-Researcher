#!/usr/bin/env python3
"""Log disclosures + data requests (stdlib sqlite)."""
import argparse, sqlite3, time

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default="requests.db")
    ap.add_argument("cmd", choices=["add", "list"])
    ap.add_argument("--kind", default="request")
    ap.add_argument("--ref", default="")
    ap.add_argument("--state", default="triaging")
    args = ap.parse_args()
    c = sqlite3.connect(args.db)
    c.execute("CREATE TABLE IF NOT EXISTS r(ts REAL, kind TEXT, ref TEXT, state TEXT)")
    if args.cmd == "add":
        c.execute("INSERT INTO r VALUES(?,?,?,?)", (time.time(), args.kind, args.ref, args.state))
        c.commit()
        print("logged - counsel owns next step")
    else:
        for r in c.execute("SELECT * FROM r ORDER BY ts"):
            print(r)

if __name__ == "__main__":
    main()
