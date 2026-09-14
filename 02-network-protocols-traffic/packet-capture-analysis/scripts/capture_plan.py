#!/usr/bin/env python3
"""Generate minimal capture plans: BPF + commands (no root needed)."""
import argparse

TASKS = {
    "tls-debug": "tcp port {port} and host {host}",
    "dns-debug": "udp port 53 and host {host}",
    "http-debug": "tcp port {port} and host {host}",
    "loss-proof": "tcp and host {host}",
    "quic-debug": "udp port 443 and host {host}",
}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--host", required=True)
    ap.add_argument("--port", type=int, default=443)
    ap.add_argument("--task", default="tls-debug", choices=sorted(TASKS))
    ap.add_argument("--iface", default="eth0")
    ap.add_argument("--seconds", type=int, default=120)
    args = ap.parse_args()
    bpf = TASKS[args.task].format(host=args.host, port=args.port)
    print("task: %s" % args.task)
    print("bpf: %s" % bpf)
    print("tcpdump: tcpdump -i %s -s 0 -G %d -W 1 -w %s.pcap '%s'" % (args.iface, args.seconds, args.task, bpf))
    print('tshark-live: tshark -i %s -a duration:%d -w %s.pcap -f "%s"' % (args.iface, args.seconds, args.task, bpf))
    print("follow: tshark -r %s.pcap -q -z follow,tcp,raw,0" % args.task)
    print("note: confirm authorization; minimize window; redact before sharing.")

if __name__ == "__main__":
    main()
