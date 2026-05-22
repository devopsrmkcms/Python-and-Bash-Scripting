#!/usr/bin/env python3

import shutil
import sys

# Step 1: Get disk usage
total, used, free = shutil.disk_usage("/")

# Step 2: Convert bytes to GB
total_gb = total // (1024**3)
used_gb = used // (1024**3)
free_gb = free // (1024**3)

# Step 3: Define threshold (example: 10 GB free)
threshold = 10

# Step 4: Check disk condition
if free_gb < threshold:
    print(f"CRITICAL - Low disk space | free={free_gb}GB")
    sys.exit(2)
else:
    print(f"OK - Disk space sufficient | free={free_gb}GB")
    sys.exit(0)
