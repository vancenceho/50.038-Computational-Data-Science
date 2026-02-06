#!/usr/bin/env python3

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# Goal (Q4):
# Emit a single key so that (with one reducer) we can compute totals globally.

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 6:
        continue
    _, _, _, _, cost, _ = data
    # Key everything to a constant so all records end up in the same reducer group
    print("ALL\t{0}".format(cost))

