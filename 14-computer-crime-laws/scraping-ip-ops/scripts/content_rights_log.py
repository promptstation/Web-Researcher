#!/usr/bin/env python3
"""Content rights log: add/list/takedown (stdlib sqlite)."""
import argparse, sqlite3, time

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default="rights.db")
    ap.add_argument("cmd", choices=["add", "list", "takedown"])
    ap.add_argument("--source", default="")
    ap.add_argument("--basis", default="")
    ap.add_argument("--item", default="")
    args = ap.parse_args()
    c = sqlite3.connect(args.db)
    c.execute("CREATE TABLE IF NOT EXISTS r(source TEXT PRIMARY KEY, basis TEXT, ts REAL)")
    c.execute("CREATE TABLE IF NOT EXISTS t(item TEXT PRIMARY KEY, ts REAL, state TEXT)")
    if args.cmd == "add":
        c.execute("INSERT OR REPLACE INTO r VALUES(?,?,?)", (args.source, args.basis, time.time()))
        c.commit()
        print("logged")
    elif args.cmd == "list":
        for r in c.execute("SELECT source,basis FROM r"):
            print("%-50s %s" % (r[0][:50], r[1]))
    else:
        c.execute("INSERT OR REPLACE INTO t VALUES(?,?,?)", (args.item, time.time(), "removed-pending-verify"))
        c.commit()
        print("takedown logged - remove content, verify, notify, file")

if __name__ == "__main__":
    main()
