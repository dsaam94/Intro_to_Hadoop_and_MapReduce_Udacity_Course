#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import re

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        ip, identity, username, date, timeZone, method, url, protocol, status, size_of_obj = data
	removed_path = re.sub(r"http://www.the-associates.co.uk",'', url)
        print "{0}\t{1}".format(removed_path,1)

