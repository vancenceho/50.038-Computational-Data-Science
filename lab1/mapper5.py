# !/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment

# We need to write our output to standard output, separated by a tab

import sys

for line in sys.stdin:
  data = line.strip().split()
  if len(data) == 10:
    ip, identity, username, datetime, tz, method, page, http_version, status, content_size = data
    # Normalise the page to the path only (drop any query string, e.g. ?a=b)
    path = page.split('?', 1)[0]
    print("{0}\t{1}".format(path, 1))