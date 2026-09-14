#!/usr/bin/env python3
"""Seen-key idempotency gate over sqlite3 (stdlib only)."""
import argparse, hashlib, sqlite3, time

def db(path):
    c = sqlite3.connect(path)
    c.execute("CREATE TABLE IF NOT EXISTS seen(k TEXT PRIMARY KEY, ts REAL)")
    c.commit()
    return c

def key(s):
    return hashlib.sha256(s.encode("utf-8", "replace")).hexdigest()[:32]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default="ledger.db")
    ap.add_argument("cmd", choices=["check", "mark", "stats", "purge"])
    ap.add_argument("--key", default="")
    ap.add_argument("--ttl-days", type=float, default=90)
    args = ap.parse_args()
    c = db(args.db)
    if args.cmd == "check":
        row = c.execute("SELECT ts FROM seen WHERE k=?", (key(args.key),)).fetchone()
        print("seen" if row else "new")
    elif args.cmd == "mark":
        c.execute("INSERT OR IGNORE INTO seen VALUES(?,?)", (key(args.key), time.time()))
        c.commit()
        print("marked")
    elif args.cmd == "stats":
        print("keys: %d" % c.execute("SELECT COUNT(*) FROM seen").fetchone()[0])
    else:
        cut = time.time() - args.ttl_days * 86400
        c.execute("DELETE FROM seen WHERE ts<?", (cut,))
        c.commit()
        print("purged")

if __name__ == "__main__":
    main()
