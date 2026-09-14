#!/usr/bin/env python3
"""Scaffold docker-compose for queue + workers + storage (stdlib only)."""
import argparse

TPL = """services:
  queue:
    image: redis:7-alpine
    ports: ["6379:6379"]
  worker:
    build: .
    deploy:
      resources:
        limits: {cpus: '1.0', memory: 2G}
    environment:
      - QUEUE_URL=redis://queue:6379/0
    depends_on: [queue]
    scale: %d
  storage:
    image: postgres:16-alpine
    environment:
      - POSTGRES_PASSWORD_FILE=/run/secrets/db_pw
    volumes: ["pg:/var/lib/postgresql/data"]
volumes: {pg: {}}
"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--out", default="docker-compose.yml")
    args = ap.parse_args()
    open(args.out, "w").write(TPL % args.workers)
    print("wrote %s workers=%d — pin digests + add secrets before prod." % (args.out, args.workers))

if __name__ == "__main__":
    main()
