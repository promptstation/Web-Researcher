#!/usr/bin/env python3
"""DSAR case tracker: open/step/close/due (stdlib sqlite)."""
import argparse, sqlite3, time
from datetime import datetime, timedelta

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default="dsar.db")
    ap.add_argument("cmd", choices=["open", "step", "close", "due"])
    ap.add_argument("--case", default="")
    ap.add_argument("--type", default="access")
    ap.add_argument("--sla-days", type=int, default=30)
    ap.add_argument("--note", default="")
    args = ap.parse_args()
    c = sqlite3.connect(args.db)
    c.execute("CREATE TABLE IF NOT EXISTS d(caseid TEXT PRIMARY KEY, typ TEXT, opened REAL, due REAL, state TEXT, log TEXT)")
    if args.cmd == "open":
        now = time.time()
        due = now + args.sla_days * 86400
        c.execute("INSERT INTO d VALUES(?,?,?,?,?,?)", (args.case, args.type, now, due, "open", "opened"))
        c.commit()
        print("opened %s due %s" % (args.case, datetime.fromtimestamp(due).date()))
    elif args.cmd == "step":
        c.execute("UPDATE d SET log=log||? WHERE caseid=?", (" | " + args.note, args.case))
        c.commit()
        print("logged")
    elif args.cmd == "close":
        c.execute("UPDATE d SET state='closed' WHERE caseid=?", (args.case,))
        c.commit()
        print("closed - file evidence pack")
    else:
        for r in c.execute("SELECT caseid,typ,due,state FROM d WHERE state='open' ORDER BY due"):
            left = (r[2] - time.time()) / 86400
            print("%s %s due_in=%.1fd %s" % (r[0], r[1], left, "OVERDUE" if left < 0 else "ok"))

if __name__ == "__main__":
    main()
