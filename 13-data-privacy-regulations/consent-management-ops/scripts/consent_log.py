#!/usr/bin/env python3
"""Consent ledger: grant/withdraw/status (stdlib sqlite)."""
import argparse, sqlite3, time

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default="consent.db")
    ap.add_argument("cmd", choices=["grant", "withdraw", "status", "export"])
    ap.add_argument("--subject", default="")
    ap.add_argument("--purpose", default="")
    ap.add_argument("--notice", default="v1")
    args = ap.parse_args()
    c = sqlite3.connect(args.db)
    c.execute("CREATE TABLE IF NOT EXISTS c(subject TEXT, purpose TEXT, state TEXT, ts REAL, notice TEXT)")
    now = time.time()
    if args.cmd == "grant":
        c.execute("INSERT INTO c VALUES(?,?,'granted',?,?)", (args.subject, args.purpose, now, args.notice))
        c.commit()
        print("granted")
    elif args.cmd == "withdraw":
        c.execute("INSERT INTO c VALUES(?,?, 'withdrawn',?,?)", (args.subject, args.purpose, now, args.notice))
        c.commit()
        print("withdrawn - propagate <24h")
    elif args.cmd == "status":
        r = c.execute("SELECT state,ts,notice FROM c WHERE subject=? AND purpose=? ORDER BY ts DESC LIMIT 1",
                      (args.subject, args.purpose)).fetchone()
        print(r or "no-record")
    else:
        for r in c.execute("SELECT * FROM c ORDER BY ts"):
            print(r)

if __name__ == "__main__":
    main()
