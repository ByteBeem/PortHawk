import json
import socket
import logging
from scapy.all import *

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

# Load services from services.json
def load_services():
    try:
        with open("services.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Warning: services.json not found. Using default services.")
        return {}

SERVICES = load_services()

def tcp_connect_scan(target, port, timeout=1):
    """TCP Connect Scan (requires no root privileges)."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            if s.connect_ex((target, port)) == 0:
                return (port, "open", SERVICES.get(str(port), "Unknown"))
    except:
        pass
    return (port, "closed", None)

def syn_scan(target, port, timeout=1):
    """Stealth SYN Scan (requires root privileges)."""
    ip = IP(dst=target)
    tcp = TCP(dport=port, flags="S")
    response = sr1(ip/tcp, timeout=timeout, verbose=0)
    if response and response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
        send(IP(dst=target)/TCP(dport=port, flags="R"), verbose=0)  
        return (port, "open", SERVICES.get(str(port), "Unknown"))
    return (port, "closed", None)

def udp_scan(target, port, timeout=1):
    """UDP Scan to check if a port is open (best effort, as UDP has no handshake)."""
    ip = IP(dst=target)
    udp = UDP(dport=port)
    response = sr1(ip/udp, timeout=timeout, verbose=0)
    
    if not response:
        return (port, "open|filtered", SERVICES.get(str(port), "Unknown"))
    elif response.haslayer(ICMP) and response.getlayer(ICMP).type == 3:
        return (port, "closed", None)
    
    return (port, "open", SERVICES.get(str(port), "Unknown"))

def fin_scan(target, port, timeout=1):
    """FIN Scan (stealthy scan, requires root)."""
    ip = IP(dst=target)
    fin = TCP(dport=port, flags="F")
    response = sr1(ip/fin, timeout=timeout, verbose=0)
    
    if not response:
        return (port, "open|filtered", SERVICES.get(str(port), "Unknown"))
    elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x14:
        return (port, "closed", None)
    
    return (port, "open", SERVICES.get(str(port), "Unknown"))

def null_scan(target, port, timeout=1):
    """NULL Scan (stealthy scan, no TCP flags set)."""
    ip = IP(dst=target)
    null_packet = TCP(dport=port, flags="")
    response = sr1(ip/null_packet, timeout=timeout, verbose=0)
    
    if not response:
        return (port, "open|filtered", SERVICES.get(str(port), "Unknown"))
    elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x14:
        return (port, "closed", None)
    
    return (port, "open", SERVICES.get(str(port), "Unknown"))
