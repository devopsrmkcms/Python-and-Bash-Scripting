#!/usr/bin/env python3

import subprocess
from datetime import datetime

services = ["sshd", "crond"]

def check_status(service):
    try:
        result = subprocess.run(
            ["systemctl", "is-active", service],
            capture_output=True,
            text=True
        )
        return result.stdout.strip()

    except subprocess.SubprocessError as e:
        print(f"Failed to check {service}: {e}")
        return None

def main():
    for service in services:
        status = check_status(service)

        # ✅ Get current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if status == "active":
            print(f"[{timestamp}] {service} -> OK")
        elif status:
            print(f"[{timestamp}] {service} -> CRITICAL ({status})")
        else:
            print(f"[{timestamp}] {service} -> ERROR")

if __name__ == "__main__":
    main()

