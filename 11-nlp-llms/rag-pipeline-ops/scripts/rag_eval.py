#!/usr/bin/env python3
"""Score RAG citation + abstention from judged QA JSONL (stdlib only)."""
import argparse, json, re

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--qa", required=True, help="JSONL: answerable, answer, citations[]")
    args = ap.parse_args()
    n = ab_ok = cite_ok = cite_n = 0
    for line in open(args.qa, encoding="utf-8"):
        r = json.loads(line)
        n += 1
        ans = r.get("answer", "")
        abstained = "not in sources" in ans.lower() or "don't know" in ans.lower()
        if bool(r.get("answerable")) != (not abstained):
            pass
        else:
            ab_ok += 1
        claims = [s for s in re.split(r"(?<=[.!?])\s+", ans) if len(s.split()) > 4 and not abstained]
        cited = sum(1 for s in claims if re.search(r"\[\d+\]", s))
        cite_ok += cited
        cite_n += len(claims)
    print("n=%d abstention_correct=%.2f citation_coverage=%.2f" % (
        n, ab_ok / max(1, n), cite_ok / max(1, cite_n)))
    print("add human faithfulness grades for supported/total claims.")

if __name__ == "__main__":
    main()
