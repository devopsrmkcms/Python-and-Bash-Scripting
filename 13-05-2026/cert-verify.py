#!/usr/bin/env python3

import ssl
import socket
import time
from datetime import datetime

# ✅ List of hosts to check
hosts = [
    "google.com",
    "github.com",
    "expired.badssl.com"   # test failure case
]

# ✅ Thresholds (like Nagios)
WARNING_DAYS = 30
CRITICAL_DAYS = 10


def check_ssl(host):
    try:
        context = ssl.create_default_context()

        start = time.time()

        with socket.create_connection((host, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:

                # ✅ Response time
                response_time = round(time.time() - start, 2)

                # ✅ Certificate
                cert = ssock.getpeercert()

                # Extract details
                subject = dict(cert['subject'][0])
                expiry_str = cert['notAfter']

                # Convert expiry to datetime
                expiry_date = datetime.strptime(expiry_str, "%b %d %H:%M:%S %Y %Z")

                # Calculate days left
                days_left = (expiry_date - datetime.utcnow()).days

                # ✅ Status logic
                if days_left < CRITICAL_DAYS:
                    status = "CRITICAL"
                elif days_left < WARNING_DAYS:
                    status = "WARNING"
                else:
                    status = "OK"

                return f"{status} | Host: {host} | CN: {subject.get('commonName')} | Days Left: {days_left} | Time: {response_time}s"

    except ssl.SSLError as e:
        return f"CRITICAL | Host: {host} | SSL Error: {e}"

    except Exception as e:
        return f"UNKNOWN | Host: {host} | Error: {e}"


def main():
    for host in hosts:
        result = check_ssl(host)
        print(result)


if __name__ == "__main__":
    main()
