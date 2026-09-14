#!/usr/bin/env python3
"""Phased connectivity probe: DNS, TCP, TLS, TTFB (stdlib only)."""
import argparse, json, socket, ssl, statistics, time, urllib.request

def phase_dns(host):
    t0 = time.monotonic()
    socket.getaddrinfo(host, 443)
    return (time.monotonic() - t0) * 1000

def phase_tcp(host, port, timeout):
    t0 = time.monotonic()
    s = socket.create_connection((host, port), timeout=timeout)
    dt = (time.monotonic() - t0) * 1000
    s.close()
    return dt

def phase_tls(host, port, timeout):
    ctx = ssl.create_default_context()
    t0 = time.monotonic()
    with ctx.wrap_socket(socket.socket(), server_hostname=host) as s:
        s.settimeout(timeout)
        s.connect((host, port))
    return (time.monotonic() - t0) * 1000

def phase_ttfb(url, timeout):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 probe"}, method="HEAD")
    t0 = time.monotonic()
    try:
        urllib.request.urlopen(req, timeout=timeout).read(1)
    except Exception:
        pass
    return (time.monotonic() - t0) * 1000

def pct(xs, p):
    return statistics.quantiles(sorted(xs), n=100)[min(99, max(0, p - 1))] if xs else 0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--host", required=True)
    ap.add_argument("--port", type=int, default=443)
    ap.add_argument("--url", default="")
    ap.add_argument("--samples", type=int, default=10)
    ap.add_argument("--timeout", type=int, default=15)
    args = ap.parse_args()
    url = args.url or ("https://%s/" % args.host)
    out = {"dns_ms": [], "tcp_ms": [], "tls_ms": [], "ttfb_ms": []}
    for _ in range(args.samples):
        try: out["dns_ms"].append(phase_dns(args.host))
        except Exception: pass
        try: out["tcp_ms"].append(phase_tcp(args.host, args.port, args.timeout))
        except Exception: pass
        try: out["tls_ms"].append(phase_tls(args.host, args.port, args.timeout))
        except Exception: pass
        out["ttfb_ms"].append(phase_ttfb(url, args.timeout))
    rep = {"host": args.host, "samples": args.samples}
    for k, v in out.items():
        rep[k] = {"n": len(v), "p50": round(pct(v, 50), 1), "p95": round(pct(v, 95), 1)} if v else {"n": 0}
    print(json.dumps(rep, indent=2))

if __name__ == "__main__":
    main()
