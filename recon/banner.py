import socket

def grab_banner(target, port, timeout=2):
    """Attempt to grab a banner from an open port using protocol-specific requests."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((target, port))

         
            if port in [21]:  
                s.send(b"USER anonymous\r\n")
            elif port in [22]: 
                pass  
            elif port in [25, 587]:  
                s.send(b"EHLO example.com\r\n")
            elif port in [110, 995]:  
                s.send(b"USER test\r\n")
            elif port in [143, 993]:  
                s.send(b"A1 CAPABILITY\r\n")
            elif port in [80, 443, 8080, 8443]:  
                s.send(b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n")
            elif port in [3306]: 
                s.send(b"\x00\x00\x00\x01\x85\xa2\x03\x00") 
            elif port in [5432]:  
                s.send(b"\x00\x00\x00\x08\x04\xd2\x16\x2f")  
            
         
            banner = s.recv(1024).decode(errors="ignore").strip()
            return banner if banner else "No banner received"
    
    except Exception as e:
        return f"Unable to retrieve banner: {str(e)}"
