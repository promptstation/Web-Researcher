#!/usr/bin/env python3
"""Index JSONL into SQLite FTS5 + BM25 query (stdlib only)."""
import argparse, json, sqlite3

def build(db, inp, idk, fields):
    c = sqlite3.connect(db)
    cols = ", ".join(fields)
    c.execute("DROP TABLE IF EXISTS docs")
    c.execute("CREATE VIRTUAL TABLE docs USING fts5(id UNINDEXED, %s)" % cols)
    rows = 0
    for line in open(inp, encoding="utf-8"):
        try:
            r = json.loads(line)
        except Exception:
            continue
        c.execute("INSERT INTO docs VALUES(?, %s)" % ",".join("?" * len(fields)),
                  [str(r.get(idk, ""))] + [str(r.get(f, "")) for f in fields])
        rows += 1
    c.commit()
    print("indexed %d docs" % rows)

def query(db, q, n):
    c = sqlite3.connect(db)
    for row in c.execute("""SELECT id, bm25(docs), snippet(docs, -1, '[', ']', '...', 30)
                            FROM docs WHERE docs MATCH ? ORDER BY rank LIMIT ?""", (q, n)):
        print("%s score=%.1f %s" % (row[0][:40], row[1], row[2][:200]))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", default="")
    ap.add_argument("--db", default="search.db")
    ap.add_argument("--id", default="record_id")
    ap.add_argument("--fields", default="title,body")
    ap.add_argument("--q", default="")
    ap.add_argument("--n", type=int, default=10)
    args = ap.parse_args()
    fields = args.fields.split(",")
    if args.inp:
        build(args.db, args.inp, args.id, fields)
    if args.q:
        query(args.db, args.q, args.n)

if __name__ == "__main__":
    main()
