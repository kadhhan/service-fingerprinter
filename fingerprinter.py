import socket

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS"
}

def grab_banner(host, port, timeout=3):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((host, port))

        # Some services send banner immediately (SSH, FTP)
        try:
            banner = sock.recv(1024).decode(errors="ignore").strip()
        except socket.timeout:
            banner = ""

        sock.close()
        return banner if banner else "No banner"
    except Exception:
        return None

def main():
    target = input("Enter target IP or domain: ").strip()

    print("\nPORT  STATE  SERVICE  BANNER")
    print("-" * 50)

    for port, service in COMMON_PORTS.items():
        banner = grab_banner(target, port)
        if banner is not None:
            print(f"{port:<5} OPEN   {service:<7} {banner}")

if __name__ == "__main__":
    main()
