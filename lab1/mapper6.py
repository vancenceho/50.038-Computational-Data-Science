#!/usr/bin/env python3

# Mapper for: number of hits per IP address
#
# Log line format (Apache common/combined-like):
# ip identity username datetime tz method page http_version status content_size

import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) != 10:
        continue
    ip = data[0]
    # Emit (IP, 1) for each request
    print("{0}\t{1}".format(ip, 1))

