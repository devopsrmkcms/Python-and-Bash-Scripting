#!/usr/bin/env python3

import subprocess

services = ["sshd", "crond"]

def check_status(service):
    try:
        result = subprocess.run(
            ["systemctl", "is-active", service],
            capture_output=True,
            text=True
        )
        return result.stdout.strip(), result.stderr.strip()

    except subprocess.SubprocessError as e:
        print(f"Failed to check {service}: {e}")
        return None, None

def main():
    for service in services:
        stdout, stderr = check_status(service)   # ✅ pass argument

        if stdout:
            print(f"{service} -> {stdout}")
        else:
            print(f"{service} -> ERROR: {stderr}")

if __name__ == "__main__":
    main()
