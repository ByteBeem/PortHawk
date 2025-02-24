import argparse
import json
from concurrent.futures import ThreadPoolExecutor
from .scanner import tcp_connect_scan, syn_scan, udp_scan, null_scan, fin_scan
from .utils import resolve_target, parse_ports
from .banner import grab_banner
from .header import display_header
from .os_detection import detect_os 
from tqdm import tqdm

# Load services from JSON
def load_services(filename="services.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading services.json: {e}")
        return {}

SERVICES = load_services()

def main():
    display_header()

    parser = argparse.ArgumentParser(description="PortHawk - Advanced Python Port Scanner")
    parser.add_argument("target", help="Target IP or hostname")
    parser.add_argument("-p", "--ports", default="1-1024", help="Port range (e.g., 80,443,1-1000)")
    parser.add_argument("-s", "--scan-type", choices=['syn', 'connect', 'udp', 'null', 'fin'], default='syn', help="Scan type")
    parser.add_argument("-t", "--threads", type=int, default=100, help="Number of threads")
    parser.add_argument("-b", "--banner", action="store_true", help="Attempt banner grabbing")
    parser.add_argument("-T", "--timeout", type=int, default=1, help="Connection timeout in seconds")
    parser.add_argument("-o", "--output", help="Save results to a file")
    parser.add_argument("-O", "--os-detect", action="store_true", help="Attempt OS detection")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")

    args = parser.parse_args()

    target = resolve_target(args.target)
    ports = parse_ports(args.ports)

    print(f"[*] Scanning {target} ({len(ports)} ports) using {args.scan_type.upper()} scan")

    if args.verbose:
        print(f"[*] Using {args.threads} threads with a timeout of {args.timeout}s per request.")

    scan_funcs = {
        "syn": syn_scan,
        "connect": tcp_connect_scan,
        "udp": udp_scan,
        "null": null_scan,
        "fin": fin_scan,
    }
    scan_func = scan_funcs[args.scan_type]

    open_ports = []

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = {executor.submit(scan_func, target, port, args.timeout): port for port in ports}
        for future in tqdm(futures, total=len(ports), desc="Scanning ports"):
            result = future.result()
            if result[1] == "open":
                port, status = result[0], result[1]
                service = SERVICES.get(str(port), "Unknown")
                banner = grab_banner(target, port) if args.banner else None
                output_line = f"[+] Port {port} is {status} - {service} - {banner or ''}"
                print(output_line)
                open_ports.append(output_line)

    print(f"\nScan complete. Found {len(open_ports)} open ports.")

    if args.os_detect:
        print("\n[*] Attempting OS detection...")
        os_info = detect_os(target)
        print(f"[+] Detected OS: {os_info}")

    # Save results if -o flag is provided
    if args.output:
        try:
            with open(args.output, "w") as f:
                f.write("\n".join(open_ports) + "\n")
                if args.os_detect:
                    f.write(f"\nDetected OS: {os_info}\n")
            print(f"[*] Results saved to {args.output}")
        except Exception as e:
            print(f"[!] Error saving results: {e}")

if __name__ == "__main__":
    main()
