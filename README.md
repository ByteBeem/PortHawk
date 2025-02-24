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
2. Set up a virtual environment (recommended):
  ```bash
  python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies:
  ```bash
   pip install -r requirements.txt

Usage 🚀
Basic TCP Connect Scan
Scan a target for open ports:
   ``bash
   python -m recon.cli example.com -p 1-1000 -s connect -t 200

SYN Scan (Requires Root)
Perform a stealthy SYN scan:
   ```bash
   sudo python -m recon.cli example.com -p 1-1000 -s syn -t 200

Contributing 🤝
Contributions are welcome! If you'd like to contribute to Port Hawk, please follow these steps:

Fork the repository.

Create a new branch for your feature or bugfix.

Submit a pull request with a detailed description of your changes.

License 📜
Port Hawk is licensed under the MIT License. See the LICENSE file for details.

Disclaimer ⚠️
This tool is intended for educational and authorized testing purposes only. Do not use it for illegal or malicious activities. The developers are not responsible for any misuse of this tool.

Support 💬
If you have any questions, issues, or feature requests, please open an issue on the GitHub repository.

Credits 🙏
Developed by Bytebeem.

Inspired by tools like Nmap and Masscan.
