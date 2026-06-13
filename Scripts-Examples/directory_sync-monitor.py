#!/usr/bin/env python3
import os
import sys
import hashlib

DIR1 = "/source"
DIR2 = "/destination"

OK, WARNING, CRITICAL = 0, 1, 2

def file_hash(path):
    h = hashlib.md5()
    with open(path, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()

def get_files(base):
    files = {}
    for root, _, filenames in os.walk(base):
        for name in filenames:
            full = os.path.join(root, name)
            rel = os.path.relpath(full, base)
            files[rel] = full
    return files

try:
    src_files = get_files(DIR1)
    dst_files = get_files(DIR2)

    missing = []    # in dest but not in source
    extra = []      # in source but not in dest
    modified = []   # same file but changed

    for f in src_files:
        if f not in dst_files:
            missing.append(f)
        else:
            if file_hash(src_files[f]) != file_hash(dst_files[f]):
                modified.append(f)

    for f in dst_files:
        if f not in src_files:
            extra.append(f)

    if missing or extra or modified:
        print(f"WARNING: Missing={len(missing)}, Extra={len(extra)}, Modified={len(modified)}")
        sys.exit(WARNING)

    print(f"OK: Directories are in sync ({len(src_files)} files checked)")
    sys.exit(OK)

except Exception as e:
    print(f"CRITICAL: {str(e)}")
    sys.exit(CRITICAL)
