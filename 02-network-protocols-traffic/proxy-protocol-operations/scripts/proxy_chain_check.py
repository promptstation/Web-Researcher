#!/usr/bin/env python3
"""Verify HTTP CONNECT and SOCKS5 proxies + exit identity (stdlib only)."""
import argparse, base64, json, socket, ssl, sys, urllib.request

def http_connect(proxy, target_host, timeout):
    host, _, port = proxy.partition(":")
    port = int(port or 8080)
    s = socket.create_connection((host, port), timeout=timeout)
    req = "CONNECT %s:443 HTTP/1.1\r\nHost: %s\r\n\r\n" % (target_host, target_host)
    s.sendall(req.encode())
    data = s.recv(4096).decode("latin1")
    s.close()
    return data.splitlines()[0] if data else "no-response"

def socks5_hello(proxy, timeout):
    host, _, port = proxy.partition(":")
    port = int(port or 1080)
    s = socket.create_connection((host, port), timeout=timeout)
    s.sendall(bytes([5, 1, 0]))
    rep = s.recv(2)
    s.close()
    if len(rep) == 2 and rep[0] == 5:
        return {0: "no-auth-ok", 2: "user-pass-required", 255: "no-method"}.get(rep[1], "method-%d" % rep[1])
    return "bad-reply"

def exit_identity(proxy_url, timeout):
    req = urllib.request.Request("https://api.ipify.org?format=json",
                                 headers={"User-Agent": "Mozilla/5.0 egress-check"})
    opener = urllib.request.build_opener(urllib.request.ProxyHandler(
        {"http": proxy_url, "https": proxy_url}))
    try:
        return json.loads(opener.open(req, timeout=timeout).read().decode())
    except Exception as e:
        return {"error": str(e)}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--proxy", required=True, help="host:port (raw) or full URL for echo test")
    ap.add_argument("--scheme", default="http", choices=["http", "socks5", "echo"])
    ap.add_argument("--target", default="example.com")
    ap.add_argument("--timeout", type=int, default=15)
    args = ap.parse_args()
    if args.scheme == "http":
        print("connect_line: %s" % http_connect(args.proxy, args.target, args.timeout))
    elif args.scheme == "socks5":
        print("socks5: %s" % socks5_hello(args.proxy, args.timeout))
    else:
        print(json.dumps(exit_identity(args.proxy, args.timeout), indent=2))

if __name__ == "__main__":
    main()
