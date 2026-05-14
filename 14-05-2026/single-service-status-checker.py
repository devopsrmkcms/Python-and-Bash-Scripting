#!/usr/bin/env python3

# Single systemd service status checker

import subprocess

service = "sshd"

def check_status(service):
    try:
        result = subprocess.run(
            ["systemctl", "is-active", service],
            capture_output=True,
            text=True
        )

        return result.stdout.strip()   # ✅ return only status like "active"

    except Exception as e:
        print(f"Failed to check: {e}")
        return None


def main():
    service_status = check_status(service)

    if service_status:
        print(f"{service} status: {service_status}")
    else:
        print("Error checking service")


if __name__ == "__main__":
    main()

