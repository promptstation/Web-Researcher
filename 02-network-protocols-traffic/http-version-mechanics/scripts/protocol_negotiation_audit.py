#!/usr/bin/env python3
"""Census ALPN negotiation across target origins (stdlib only)."""
import argparse, json, socket, ssl, urllib.request

def alpn_for(host, port=443, timeout=12):
    ctx = ssl.create_default_context()
    ctx.set_alpn_protocols(["h3", "h2", "http/1.1"])
    try:
        with ctx.wrap_socket(socket.socket(), server_hostname=host) as s:
            s.settimeout(timeout)
            s.connect((host, port))
            return {"alpn": s.selected_alpn_protocol(), "tls": s.version(),
                    "cipher": (s.cipher() or [None])[0]}
    except Exception as e:
        return {"error": str(e)}

def hints(url, timeout):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 version-audit"}, method="HEAD")
        r = urllib.request.urlopen(req, timeout=timeout)
        h = dict(r.headers.items())
        return {"server": h.get("Server"), "alt_svc": h.get("Alt-Svc"), "via": h.get("Via")}
    except Exception as e:
        return {"error": str(e)}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--targets", required=True, help="file with one https URL per line")
    ap.add_argument("--timeout", type=int, default=12)
    args = ap.parse_args()
    urls = [l.strip() for l in open(args.targets) if l.strip() and not l.startswith("#")]
    rows = []
    for u in urls:
        host = urllib.request.urlparse(u).hostname
        row = {"url": u, "host": host}
        row.update(alpn_for(host, timeout=args.timeout) if host else {"error": "bad-url"})
        row["hints"] = hints(u, args.timeout)
        rows.append(row)
        print(json.dumps(row))
    mix = {}
    for r in rows:
        mix[r.get("alpn", "error")] = mix.get(r.get("alpn", "error"), 0) + 1
    print("MIX " + json.dumps(mix), file=__import__("sys").stderr)

if __name__ == "__main__":
    main()
