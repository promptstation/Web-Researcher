#!/usr/bin/env python3
"""Dump local TLS client profile: versions, ciphers, options (stdlib only)."""
import json, ssl

def main():
    ctx = ssl.create_default_context()
    print(json.dumps({
        "openssl": ssl.OPENSSL_VERSION,
        "protocol": ctx.protocol.name if hasattr(ctx.protocol, "name") else str(ctx.protocol),
        "check_hostname": ctx.check_hostname,
        "verify_mode": ctx.verify_mode.name if hasattr(ctx.verify_mode, "name") else str(ctx.verify_mode),
        "options": [o.name for o in ssl.Options if ctx.options & o][:25],
        "ciphers_offered": [c["name"] for c in ctx.get_ciphers()][:40],
        "cipher_count": len(ctx.get_ciphers()),
        "alpn_we_offer": ["h2", "http/1.1"],
    }, indent=2))

if __name__ == "__main__":
    main()
