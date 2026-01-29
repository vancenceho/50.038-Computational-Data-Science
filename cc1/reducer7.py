#!/usr/bin/env python3

# Reducer for: most popular file on the website
#
# Input (from mapper5.py, sorted by key, optionally via reducer5 as combiner):
# page\t1  OR  page\t<count>
# We aggregate counts per page, and track the page with the maximum total.
#
# Output (single line):
# <most_popular_page>\t<max_hits>

    if currentTotal > maxHits:
        maxHits = currentTotal
        maxPage = oldKey

if maxPage is not None:
    print(maxPage, "\t", maxHits)

