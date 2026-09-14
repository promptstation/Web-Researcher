#!/usr/bin/env python3
"""Raw DNS query audit over UDP + DoH comparison (stdlib only)."""
import argparse, json, random, socket, struct, sys, urllib.request, urllib.parse

QTYPE = {"A": 1, "AAAA": 28, "CNAME": 5, "NS": 2, "MX": 15, "TXT": 16}

def build_query(domain, qtype):
    hdr = struct.pack(">HHHHHH", random.randint(0, 65535), 0x0100, 1, 0, 0, 0)
    qname = b"".join(struct.pack(">B", len(p)) + p.encode() for p in domain.split(".")) + b"\x00"
    return hdr + qname + struct.pack(">HH", QTYPE[qtype], 1)

def query_udp(domain, qtype, resolver, timeout):
    pkt = build_query(domain, qtype)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(timeout)
    import time
    t0 = time.monotonic()
    s.sendto(pkt, (resolver, 53))
    data, _ = s.recvfrom(4096)
    dt = (time.monotonic() - t0) * 1000
    rcode = data[3] & 0x0F
    ancount = struct.unpack(">H", data[6:8])[0]
    return {"rcode": rcode, "answers": ancount, "bytes": len(data), "ms": round(dt, 1)}

def query_doh(domain, qtype, endpoint, timeout):
    url = endpoint + "?name=" + urllib.parse.quote(domain) + "&type=" + qtype
    req = urllib.request.Request(url, headers={"Accept": "application/dns-json",
                                               "User-Agent": "Mozilla/5.0 dns-audit"})
    import time
    t0 = time.monotonic()
    r = json.loads(urllib.request.urlopen(req, timeout=timeout).read().decode())
    dt = (time.monotonic() - t0) * 1000
    return {"status": r.get("Status"), "answers": len(r.get("Answer", [])), "ms": round(dt, 1)}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--domain", required=True)
    ap.add_argument("--resolver", default="1.1.1.1")
    ap.add_argument("--qtype", default="A", choices=sorted(QTYPE))
    ap.add_argument("--doh", default="https://cloudflare-dns.com/dns-query")
    ap.add_argument("--timeout", type=int, default=10)
    args = ap.parse_args()
    rep = {"domain": args.domain, "qtype": args.qtype}
    try:
        rep["udp_" + args.resolver] = query_udp(args.domain, args.qtype, args.resolver, args.timeout)
    except Exception as e:
        rep["udp_error"] = str(e)
    try:
        rep["doh"] = query_doh(args.domain, args.qtype, args.doh, args.timeout)
    except Exception as e:
        rep["doh_error"] = str(e)
    print(json.dumps(rep, indent=2))

if __name__ == "__main__":
    main()
