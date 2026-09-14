#!/usr/bin/env python3
"""Tiny durable leased queue over sqlite3: enqueue/dequeue/ack/dlq (stdlib only)."""
import argparse, json, sqlite3, time

DDL = """CREATE TABLE IF NOT EXISTS jobs(
 id INTEGER PRIMARY KEY, body TEXT, prio INTEGER DEFAULT 5,
 state TEXT DEFAULT 'ready', lease_until REAL DEFAULT 0,
 attempts INTEGER DEFAULT 0, error TEXT, ts REAL)"""

def db(path):
    c = sqlite3.connect(path)
    c.execute(DDL)
    c.commit()
    return c

def enqueue(c, body, prio):
    c.execute("INSERT INTO jobs(body,prio,ts) VALUES(?,?,?)", (body, prio, time.time()))
    c.commit()
    print("enqueued")

def dequeue(c, lease_s):
    now = time.time()
    c.execute("UPDATE jobs SET state='ready' WHERE state='leased' AND lease_until<?", (now,))
    row = c.execute("""SELECT id,body,attempts FROM jobs WHERE state='ready'
                       ORDER BY prio,ts LIMIT 1""").fetchone()
    if not row:
        print("empty")
        return
    jid, body, att = row
    c.execute("UPDATE jobs SET state='leased',lease_until=?,attempts=attempts+1 WHERE id=?",
              (now + lease_s, jid))
    c.commit()
    print(json.dumps({"id": jid, "attempts": att + 1, "body": body}))

def ack(c, jid, error):
    if error:
        c.execute("UPDATE jobs SET state='dlq',error=? WHERE id=?", (error, jid))
    else:
        c.execute("DELETE FROM jobs WHERE id=?", (jid,))
    c.commit()
    print("done")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default="queue.db")
    ap.add_argument("cmd", choices=["enqueue", "dequeue", "ack", "dlq", "stats"])
    ap.add_argument("--body", default="{}")
    ap.add_argument("--prio", type=int, default=5)
    ap.add_argument("--lease", type=float, default=300)
    ap.add_argument("--id", type=int, default=0)
    ap.add_argument("--error", default="")
    args = ap.parse_args()
    c = db(args.db)
    if args.cmd == "enqueue":
        enqueue(c, args.body, args.prio)
    elif args.cmd == "dequeue":
        dequeue(c, args.lease)
    elif args.cmd == "ack":
        ack(c, args.id, args.error)
    elif args.cmd == "dlq":
        for r in c.execute("SELECT id,attempts,error,substr(body,1,80) FROM jobs WHERE state='dlq'"):
            print(r)
    else:
        for r in c.execute("SELECT state,COUNT(*) FROM jobs GROUP BY state"):
            print(r)

if __name__ == "__main__":
    main()
