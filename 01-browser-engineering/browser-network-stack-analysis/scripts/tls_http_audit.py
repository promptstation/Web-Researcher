#!/usr/bin/env python3
"""TLS + HTTP audit using only the standard library."""
import argparse, json, socket, ssl, sys, urllib.request

def handshake(host, port=443):
    ctx = ssl.create_default_context()
    ctx.set_alpn_protocols(["h2", "http/1.1"])
    out = {}
    with ctx.wrap_socket(socket.socket(), server_hostname=host) as s:
        s.settimeout(15)
        s.connect((host, port))
        out["tls_version"] = s.version()
        out["cipher"] = s.cipher()[0] if s.cipher() else None
        out["alpn"] = s.selected_alpn_protocol()
        cert = s.getpeercert() or {}
        out["subject"] = dict(x[0] for x in cert.get("subject", []))
        out["issuer"] = dict(x[0] for x in cert.get("issuer", []))
        out["notAfter"] = cert.get("notAfter")
    return out

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

def headers_for(url, timeout):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 tls-audit"},
                                 method="HEAD")
    opener = urllib.request.build_opener(NoRedirect)
    try:
        r = opener.open(req, timeout=timeout)
        return {"status": r.status, "headers": dict(r.headers.items()), "final": r.geturl()}
    except urllib.request.HTTPError as e:
        return {"status": e.code, "headers": dict(e.headers.items()), "final": url}
    except Exception as e:
        return {"error": str(e), "final": url}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", required=True)
    ap.add_argument("--timeout", type=int, default=20)
    args = ap.parse_args()
    host = urllib.request.urlparse(args.url).hostname
    if not host:
        print("bad URL", file=sys.stderr)
        sys.exit(2)
    report = {"host": host}
    try:
        report["handshake"] = handshake(host)
    except Exception as e:
        report["handshake_error"] = str(e)
    chain, seen, cur = [], set(), args.url
    for _ in range(10):
        h = headers_for(cur, args.timeout)
        chain.append({"url": cur, "status": h.get("status"), "location": h.get("headers", {}).get("Location")})
        loc = h.get("headers", {}).get("Location")
        if h.get("status") in (301, 302, 303, 307, 308) and loc and loc not in seen:
            seen.add(cur)
            cur = urllib.request.urljoin(cur, loc)
            continue
        report["final_headers"] = h.get("headers", {})
        break
    report["redirect_chain"] = chain
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
