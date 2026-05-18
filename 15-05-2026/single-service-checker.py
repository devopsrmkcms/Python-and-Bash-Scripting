#!/usr/bin/env python3

import subprocess
import sys

services = ["sshd", "crond"]

def check_status(service):
    try:
        result = subprocess.run(["systemctl", "is-active", service], capture_output=True, text=True)
        return result.stdout.strip(), result.stderr.strip()
    
    except subprocess.SubprocessError as e:
        print(f"Failed to check")
        return None
    
def main():
    for service in services:
        service_status = check_status(service)
        print(f"{service_status}")
    
if __name__ == "__main__":
    main()
