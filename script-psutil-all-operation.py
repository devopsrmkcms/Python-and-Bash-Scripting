#!/usr/bin/env python3

import psutil
import time

# ---------------- CPU ----------------
def cpu_info():
    print("\n=== CPU ===")
    print(f"CPU %: {psutil.cpu_percent(interval=1)}")
    print(f"CPU cores: {psutil.cpu_count(logical=True)}")
    print(f"Load avg (1,5,15): {psutil.getloadavg()}")

# ---------------- Memory ----------------
def memory_info():
    print("\n=== MEMORY ===")
    mem = psutil.virtual_memory()
    print(f"Total: {mem.total}")
    print(f"Available: {mem.available}")
    print(f"Used %: {mem.percent}")

# ---------------- Disk ----------------
def disk_info():
    print("\n=== DISK ===")
    disk = psutil.disk_usage("/")
    print(f"Total: {disk.total}")
    print(f"Used: {disk.used}")
    print(f"Free: {disk.free}")
    print(f"Used %: {disk.percent}")

# ---------------- Disk IO ----------------
def disk_io():
    print("\n=== DISK IO ===")
    io = psutil.disk_io_counters()
    print(f"Read: {io.read_bytes}")
    print(f"Write: {io.write_bytes}")

# ---------------- Network ----------------
def network_info():
    print("\n=== NETWORK ===")
    net = psutil.net_io_counters()
    print(f"Sent: {net.bytes_sent}")
    print(f"Received: {net.bytes_recv}")

# ---------------- Top Processes ----------------
def top_processes():
    print("\n=== TOP PROCESSES ===")

    # initialize cpu %
    for p in psutil.process_iter():
        p.cpu_percent()

    time.sleep(1)

    procs = sorted(psutil.process_iter(['pid', 'name', 'cpu_percent']),
                   key=lambda p: p.info['cpu_percent'],
                   reverse=True)[:5]

    for p in procs:
        print(p.info)

# ---------------- Main ----------------
def main():
    cpu_info()
    memory_info()
    disk_info()
    disk_io()
    network_info()
    top_processes()

if __name__ == "__main__":
    main()
