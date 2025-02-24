# Port Hawk 🦅

**Port Hawk** is an advanced Python port scanner designed for network reconnaissance and security auditing. Inspired by professional tools, it provides fast, reliable, and customizable port scanning capabilities with support for TCP, UDP, and banner grabbing.

---

## Features ✨

- **TCP Connect Scan**: Standard port scanning for open ports.
- **SYN Scan**: Stealthy half-open scanning (requires root privileges).
- **UDP Scan**: Scan UDP ports for services like DNS, DHCP, and more.
- **Banner Grabbing**: Retrieve service banners from open ports.
- **Service Detection**: Identify services running on open ports.
- **Multi-Threading**: Fast and efficient scanning with concurrent threads.
- **IP Range Scanning**: Scan multiple IP addresses in a range.
- **Export Results**: Save scan results in JSON, CSV, or text format.
- **Verbose Mode**: Detailed output for debugging and analysis.
- **Progress Bar**: Real-time progress tracking during scans.

---

## Installation 🛠️

### Prerequisites
- Python 3.7 or higher
- `scapy` library (for SYN scans)
- `colorama` library (for colored output, optional)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/bytebeem/PortHawk.git
   cd PortHawk
