#!/usr/bin/env python3

# Reducer for: number of hits per IP address
#
# Input (from mapper6.py, sorted by key):
# ip\t1
# Output:
# ip\t<total_hits>

import sys

oldKey = None
hitTotal = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisCount = data_mapped

    if oldKey and oldKey != thisKey:
        print(oldKey, "\t", hitTotal)
        hitTotal = 0

    oldKey = thisKey
    try:
        hitTotal += int(thisCount)
    except ValueError:
        continue

if oldKey is not None:
    print(oldKey, "\t", hitTotal)

