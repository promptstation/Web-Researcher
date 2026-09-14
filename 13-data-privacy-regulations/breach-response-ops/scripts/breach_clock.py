#!/usr/bin/env python3
"""Breach clock + checklist tracker (stdlib sqlite)."""
import argparse, sqlite3, time
from datetime import datetime

ITEMS = ["contained", "evidence-held", "dpo-looped", "counsel-looped", "scope-memo",
         "authority-assessed", "authority-notified", "subjects-assessed", "subjects-notified", "postmortem"]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default="breach.db")
    ap.add_argument("cmd", choices=["start", "check", "status"])
    ap.add_argument("--case", default="")
    ap.add_argument("--item", default="")
    args = ap.parse_args()
    c = sqlite3.connect(args.db)
    c.execute("CREATE TABLE IF NOT EXISTS b(caseid TEXT, item TEXT, ts REAL)")
    c.execute("CREATE TABLE IF NOT EXISTS o(caseid TEXT PRIMARY KEY, opened REAL)")
    if args.cmd == "start":
        c.execute("INSERT OR REPLACE INTO o VALUES(?,?)", (args.case, time.time()))
        c.commit()
        print("clock started %s - 72h authority line: notify or reason why not" % args.case)
    elif args.cmd == "check":
        c.execute("INSERT INTO b VALUES(?,?,?)", (args.case, args.item, time.time()))
        c.commit()
        print("checked " + args.item)
    else:
        o = c.execute("SELECT opened FROM o WHERE caseid=?", (args.case,)).fetchone()
        el = (time.time() - o[0]) / 3600 if o else 0
        done = {r[0] for r in c.execute("SELECT item FROM b WHERE caseid=?", (args.case,))}
        print("case=%s elapsed=%.1fh/72h" % (args.case, el))
        for it in ITEMS:
            print("  [%s] %s" % ("x" if it in done else " ", it))

if __name__ == "__main__":
    main()
