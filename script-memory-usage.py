#!/usr/bin/env python3

import sys

# Step 1: Read memory info from /proc
with open("/proc/meminfo") as f:
    lines = f.readlines()

# Step 2: Extract required values
mem_total = int([x for x in lines if "MemTotal" in x][0].split()[1])
mem_available = int([x for x in lines if "MemAvailable" in x][0].split()[1])

# Step 3: Calculate used memory
mem_used = mem_total - mem_available

# Step 4: Convert to percentage
mem_used_pct = (mem_used / mem_total) * 100

# Step 5: Define thresholds
warning_threshold = 70
critical_threshold = 90

# Step 6: Check condition
if mem_used_pct >= critical_threshold:
    print(f"CRITICAL - Memory usage {mem_used_pct:.2f}%")
    sys.exit(2)
elif mem_used_pct >= warning_threshold:
    print(f"WARNING - Memory usage {mem_used_pct:.2f}%")
    sys.exit(1)
else:
    print(f"OK - Memory usage {mem_used_pct:.2f}%")
    sys.exit(0)
