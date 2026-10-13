import sys
from collections import Counter

# Log lines look like: 2026-10-12 08:01:13 [INFO] [auth-service] [req-39999] ...
FIELD_INDEX = 3  # 0=date, 1=time, 2=level, 3=service
TOP_N = 5

if len(sys.argv) != 2:
    sys.exit("Usage: python3 summary.py <logfile>")

filename = sys.argv[1]

with open(filename, "r") as f:
    lines = f.readlines()

print("Total lines:", len(lines))

counts = Counter()
for line in lines:
    fields = line.split()
    if len(fields) > FIELD_INDEX:
        key = fields[FIELD_INDEX]
        counts[key] += 1

print(f"Top {TOP_N}:")
for item, n in counts.most_common(TOP_N):
    print(item, n)
