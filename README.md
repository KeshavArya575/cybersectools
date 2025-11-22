
---

## Tools Overview

### 1. Packet Sniffer 

A raw socket packet sniffer that:

- Captures incoming packets on the network interface
- Parses Ethernet, IPv4, TCP/UDP layers
- Prints packet metadata and hex‑dump payload


 
### 2. Port Scanner
A fast, multi‑threaded TCP port scanner.

- Scans TCP ports using connect_ex
- Uses threading for speed
- Displays open ports clearly

### 3. Log Analyzer
A security-focused web server log analysis tool.

Detects:
- SQL Injection attempts
- XSS payloads
- Directory traversal
- Command injection attempts

Additional functions:

- Top IP address summary
- Attack frequency statistics

**Usage:**

```` bash
sudo python3 packet_sniffer.py
python3 port_scanner.py
python3 log_analyzer.py access.log

````
---
