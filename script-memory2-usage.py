#!/usr/bin/env python3

import sys

# Step 1: Read file
with open("/proc/meminfo") as f:
    data = f.read()

# Step 2: Initialize variables
mem_total = 0
mem_available = 0

# Step 3: Extract values
for line in data.split("\n"):
    if "MemTotal" in line:
        mem_total = int(line.split()[1])

    if "MemAvailable" in line:
        mem_available = int(line.split()[1])

# Step 4: Calculate usage
mem_used = mem_total - mem_available
mem_used_pct = (mem_used / mem_total) * 100

# Step 5: Check thresholds
if mem_used_pct > 90:
    print(f"CRITICAL - Memory {mem_used_pct:.2f}%")
    sys.exit(2)

elif mem_used_pct > 70:
    print(f"WARNING - Memory {mem_used_pct:.2f}%")
    sys.exit(1)

else:
    print(f"OK - Memory {mem_used_pct:.2f}%")
    sys.exit(0)
