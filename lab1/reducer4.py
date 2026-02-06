#!/usr/bin/env python3

# Input format:
# ALL\t<cost>
#
# Output:
# TotalSales\t<sum>
# TotalCount\t<count>

import sys

total_sales = 0.0
total_count = 0

for line in sys.stdin:
    parts = line.strip().split("\t")
    if len(parts) != 2:
        continue
    _, sale = parts
    try:
        sale = float(sale)
    except ValueError:
        continue
    total_sales += sale
    total_count += 1

print("TotalSales\t{0}".format(total_sales))
print("TotalCount\t{0}".format(total_count))

