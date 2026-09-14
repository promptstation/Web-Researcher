"""Scoped mitmproxy addon: allowlist hosts, log JSONL, redact auth.

Run: mitmdump -s mitm_flows_addon.py --set out=flows.jsonl --set allow=api.test,app.test
Requires: mitmproxy installed. Scope: test traffic you own only.
"""
import json
from mitmproxy import ctx

REDACT = {"authorization", "cookie", "set-cookie", "proxy-authorization", "x-api-key"}

class ScopedLogger:
    def load(self, loader):
        loader.add_option("out", str, "flows.jsonl", "JSONL output path")
        loader.add_option("allow", str, "", "comma-separated allowed hosts")

    def request(self, flow):
        allow = [h.strip() for h in ctx.options.allow.split(",") if h.strip()]
        host = flow.request.host
        if allow and not any(host == a or host.endswith("." + a) for a in allow):
            flow.kill()

    def response(self, flow):
        if flow.error or not flow.response:
            return
        hdrs = {k.lower(): ("REDACTED" if k.lower() in REDACT else v)
                for k, v in flow.request.headers.items()}
        row = {"host": flow.request.host, "method": flow.request.method,
               "path": flow.request.path.split("?")[0], "status": flow.response.status_code,
               "req_headers": hdrs, "ms": int((flow.response.timestamp_end - flow.request.timestamp_start) * 1000)}
        with open(ctx.options.out, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(row) + "\n")

addons = [ScopedLogger()]
