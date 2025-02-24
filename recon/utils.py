import socket

def resolve_target(target):
    """Resolve hostname to IP if necessary."""
    try:
        return socket.gethostbyname(target)
    except socket.gaierror:
        raise ValueError(f"Unable to resolve {target}")

def parse_ports(port_arg):
    """Parse port range or list from string."""
    ports = set()
    for part in port_arg.split(','):
        if '-' in part:
            start, end = map(int, part.split('-'))
            ports.update(range(start, end + 1))
        else:
            ports.add(int(part))
    return sorted(ports)