from scapy.all import *

def detect_os(target):
    try:
        ip = IP(dst=target)
        tcp = TCP(dport=80, flags="S")
        response = sr1(ip/tcp, timeout=1, verbose=0)

        if response and response.haslayer(TCP):
            ttl = response.ttl
            window_size = response.window
            if ttl <= 64:
                return "Linux (Ubuntu/Debian/Fedora)"
            elif ttl <= 128:
                return "Windows (XP/7/10/Server)"
            elif ttl <= 255:
                return "Cisco/Network Device"
        return "Unknown OS"
    except:
        return "OS detection failed"
