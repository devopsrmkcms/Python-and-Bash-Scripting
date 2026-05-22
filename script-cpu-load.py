#!/usr/bin/env python3

import os
import sys

# Step 1: Load average (CPU usage indicator)
load1, load5, load15 = os.getloadavg()

# Step 2: Get CPU core count
cpu_count = os.cpu_count()

# Step 3: Calculate CPU usage percentage (approx)
cpu_usage = (load1 / cpu_count) * 100

# Step 4: Define thresholds
warning_threshold = 70
critical_threshold = 90

# Step 5: Check status
if cpu_usage >= critical_threshold:
    print(f"CRITICAL - CPU usage {cpu_usage:.2f}%")
    sys.exit(2)
elif cpu_usage >= warning_threshold:
    print(f"WARNING - CPU usage {cpu_usage:.2f}%")
    sys.exit(1)
else:
    print(f"OK - CPU usage {cpu_usage:.2f}%")
    sys.exit(0)
``
