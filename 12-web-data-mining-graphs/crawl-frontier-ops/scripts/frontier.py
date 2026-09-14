#!/usr/bin/env python3
"""Polite priority frontier prototype over sqlite (stdlib only)."""
import argparse, hashlib, sqlite3, time, urllib.parse

def canon(u):
    p = urllib.parse.urlparse(u)
    q = "&".join(sorted(x for x in p.query.split("&") if x and not x.startswith(("utm_", "fbclid"))))
    return urllib.parse.urlunparse((p.scheme, p.netloc.lower(), p.path or "/", "", q, ""))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default="frontier.db")
    ap.add_argument("cmd", choices=["add", "next", "done", "stats"])
    ap.add_argument("--seed", default="")
    ap.add_argument("--score", type=float, default=1.0)
    ap.add_argument("--delay", type=float, default=1.0)
    args = ap.parse_args()
    c = sqlite3.connect(args.db)
    c.execute("CREATE TABLE IF NOT EXISTS f(id TEXT PRIMARY KEY, url TEXT, host TEXT, score REAL, state TEXT, ts REAL)")
    c.execute("CREATE TABLE IF NOT EXISTS h(host TEXT PRIMARY KEY, last REAL)")
    if args.cmd == "add":
        u = canon(args.seed)
        host = urllib.parse.urlparse(u).netloc
        k = hashlib.sha256(u.encode()).hexdigest()[:16]
        c.execute("INSERT OR IGNORE INTO f VALUES(?,?,?,?,'ready',?)", (k, u, host, args.score, time.time()))
        c.commit()
        print("added %s" % u)
    elif args.cmd == "next":
        now = time.time()
        for k, u, host, s in c.execute("SELECT id,url,host,score FROM f WHERE state='ready' ORDER BY score DESC LIMIT 20"):
            last = c.execute("SELECT last FROM h WHERE host=?", (host,)).fetchone()
            if last and now - last[0] < args.delay:
                continue
            c.execute("UPDATE f SET state='out' WHERE id=?", (k,))
            c.execute("INSERT OR REPLACE INTO h VALUES(?,?)", (host, now))
            c.commit()
            print(u)
            return
        print("none-ready (all delayed or empty)")
    elif args.cmd == "done":
        c.execute("UPDATE f SET state='done' WHERE id=?", (args.seed,))
        c.commit()
        print("done")
    else:
        for r in c.execute("SELECT state,COUNT(*) FROM f GROUP BY state"):
            print(r)

if __name__ == "__main__":
    main()
