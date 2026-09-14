# Capture Filters

BPF patterns: host 203.0.113.7; port 443; tcp port 443 and host X; net 198.51.100.0/24; udp port 53; tcp[tcpflags] & tcp-syn != 0 for handshakes; vlan and ... when tagged. Combine with and/or/not and parentheses. Capture filters use BPF; display filters use Wireshark syntax like tls.handshake.type == 1 or http2.streamid == 3 or dns.qry.name contains example.

Recording: tcpdump -i eth0 -s 0 -C 100 -W 5 -w cap.pcap 'filter'; dumpcap adds ring discipline; tshark -r in.pcap -Y 'display' -T fields -e fields for stats. Check drops in status output.

Stream work: right-click follow TCP/TLS/HTTP/QUIC streams; use ssl.keylog_file for owned decryption; reassemble with care on retransmitting paths. Statistics menus beat scrolling: conversations, protocol hierarchy, IO graphs, flow graphs.

Hygiene: capture windows not days; rotate files; encrypt at rest; redact Authorization, Cookie, Set-Cookie, tokens, and payloads with PII; delete on schedule.
