#!/usr/bin/env python3

import socket
from datetime import datetime

def dns_check(domain):
    try:
        start_time = datetime.now()

        # Convert domain -> IP
        ip = socket.gethostbyname(domain)

        end_time = datetime.now()
        response_time = (end_time - start_time).total_seconds()

        return ip, response_time

    except socket.gaierror as e:
        print(f"DNS Resolution Failed: {e}")
        return None, None


def main():
    domain = input("Enter domain (e.g., google.com): ").strip()

    ip, response_time = dns_check(domain)

    if ip is None:
        print(f"{domain} -> DNS FAILED")
    else:
        print(f"{domain} -> IP: {ip}")
        print(f"Response Time: {response_time:.4f} seconds")


if __name__ == "__main__":
    main()

