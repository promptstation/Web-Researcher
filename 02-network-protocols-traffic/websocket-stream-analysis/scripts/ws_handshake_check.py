#!/usr/bin/env python3
"""Verify a WebSocket upgrade handshake (stdlib, http only check)."""
import argparse, base64, hashlib, os, socket, ssl, sys, urllib.parse

GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", required=True)
    ap.add_argument("--timeout", type=int, default=15)
    args = ap.parse_args()
    u = urllib.parse.urlparse(args.url)
    if u.scheme not in ("ws", "wss"):
        print("need ws:// or wss:// URL", file=sys.stderr)
        sys.exit(2)
    host, port = u.hostname, u.port or (443 if u.scheme == "wss" else 80)
    key = base64.b64encode(os.urandom(16)).decode()
    req = ("GET %s HTTP/1.1\r\nHost: %s\r\nUpgrade: websocket\r\nConnection: Upgrade\r\n"
           "Sec-WebSocket-Key: %s\r\nSec-WebSocket-Version: 13\r\n\r\n") % (u.path or "/", host, key)
    s = socket.create_connection((host, port), timeout=args.timeout)
    if u.scheme == "wss":
        s = ssl.create_default_context().wrap_socket(s, server_hostname=host)
    s.sendall(req.encode())
    data = s.recv(4096).decode("latin1")
    s.close()
    print(data.split("\r\n\r\n")[0])
    expect = base64.b64encode(hashlib.sha1((key + GUID).encode()).digest()).decode()
    print("expected_accept: %s" % expect)
    print("verdict: %s" % ("101-SWITCHED" if " 101 " in data else "NO-UPGRADE"))

if __name__ == "__main__":
    main()
