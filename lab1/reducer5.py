#!/usr/bin/env python3

import sys

# Count number of hits per page/file
hitTotal = 0
oldKey = None

# Input from mapper5.py:
# page\t1
# where page is the file/URL requested, and 1 is a single hit

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisCount = data_mapped

    if oldKey and oldKey != thisKey:
        print(oldKey, "\t", hitTotal)
        hitTotal = 0

    oldKey = thisKey
    try:
        hitTotal += int(thisCount)
    except ValueError:
        # Bad count; skip
        continue

# do not forget to output the last page if needed! This happens after looping through the standard input
if oldKey is not None:
    print(oldKey, "\t", hitTotal)