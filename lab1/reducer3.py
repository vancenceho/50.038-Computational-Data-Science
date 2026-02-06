#!/usr/bin/env python3

import sys

salesTotal = 0
maxSales = None
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the item name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisItem, thisSale = data_mapped
    
    try:
      thisSale = float(thisSale)
    except ValueError:
      continue

    if oldKey and oldKey != thisKey:
        #print(oldKey, "\t", salesTotal)
        # oldKey = thisKey;
        #salesTotal = 0
        print(oldKey, "\t", maxSales)
        maxSales = None

    oldKey = thisKey
    #salesTotal += float(thisSale)
    if maxSales is None or thisSale > maxSales:
      maxSales = thisSale

# do not forget to output the last store if needed! This happens after looping through the standard input
if oldKey != None:
    #print (oldKey, "\t", salesTotal)
    print(oldKey, "\t", maxSales)