#!/usr/bin/env python3

# Certificate validity checker
import ssl, socket
from datetime import datetime

def cert_check(domain):
    try:
        context = ssl.create_default_context()

        with socket.create_connection((domain, 443), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()

                expiry_date_str = cert['notAfter']
                return expiry_date_str

    except Exception as e:
        return f"Error: {e}"


def main():
    domain = input("Enter the domain: ").strip()

    expiry = cert_check(domain)   # ✅ capture return value

    print(f"Expiry Date for {domain}: {expiry}")   # ✅ print


if __name__ == "__main__":
    main()

