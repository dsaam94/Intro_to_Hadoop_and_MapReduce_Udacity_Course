#!/usr/bin/python

import sys

salesTotal = 0
oldKey = None
count = 0

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 1:
        # Something has gone wrong. Skip this line.
        continue

    thisSale = data_mapped
    count += 1	
    #if oldKey and oldKey != thisKey:
        #print oldKey, "\t", salesTotal
     #   oldKey = thisKey;
        #salesTotal = 0

    #oldKey = thisKey
    salesTotal += float(thisSale)

#if oldKey != None:
print count, "\t", salesTotal

