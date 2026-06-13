#!/usr/bin/env python3
import os
import sys
import subprocess

REPO_DIR = "/path/to/repo"

def update_repo():
    # Check repo directory
    if not os.path.isdir(REPO_DIR):
        print("CRITICAL: Repo directory not found")
        return 2

    # Check .git folder
    if not os.path.isdir(REPO_DIR + "/.git"):
        print("CRITICAL: Not a git repository")
        return 2

    # Go inside repo
    os.chdir(REPO_DIR)

    # Check uncommitted changes
    status = subprocess.getoutput("git status --porcelain")

    if status:
        print("WARNING: Uncommitted changes present")
        return 1

    # Pull latest changes
    result = os.system("git pull")

    if result != 0:
        print("CRITICAL: git pull failed")
        return 2

    print("OK: Repository updated successfully")
    return 0


if __name__ == "__main__":
    exit_code = update_repo()
    sys.exit(exit_code)
