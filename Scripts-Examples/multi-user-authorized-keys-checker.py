#!/usr/bin/env python3

import os
import sys

HOME_DIR = "/home"

def check_all_users():
    try:
        users = os.listdir(HOME_DIR)
        issues = []
        total_keys = 0

        for user in users:
            auth_file = os.path.join(HOME_DIR, user, ".ssh", "authorized_keys")

            if os.path.exists(auth_file):
                with open(auth_file, "r") as f:
                    keys = [line.strip() for line in f if line.strip()]

                if not keys:
                    issues.append(f"{user}: No keys")
                else:
                    total_keys += len(keys)
            else:
                issues.append(f"{user}: authorized_keys missing")

        # ✅ Output
        if issues:
            print(f"WARNING: Issues found -> {', '.join(issues)}")
            sys.exit(1)
        else:
            print(f"OK: All users have keys (Total keys: {total_keys})")
            sys.exit(0)

    except Exception as e:
        print(f"UNKNOWN: {str(e)}")
        sys.exit(3)

if __name__ == "__main__":
    check_all_users()
