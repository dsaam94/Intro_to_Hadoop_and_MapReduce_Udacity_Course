#!/usr/bin/python


import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter = '\t', lineterminator="\N", quotechar = '"', quoting = csv.QUOTE_ALL)
#writer = csv.writer(sys.stdout, delimiter = '\t', quotechar = '"', quoting = csv.QUOTE_ALL)
for line in reader:
	author_id = line[3]
	if(author_id == "author_id"):
		continue
	added_at = line[8].strip().split(".")[0] 
	hour = re.findall(r'.*? (\d{2}):.*?', added_at)
	hour = ''.join(map(str,hour))
	print "{0}\t{1}".format(author_id,hour)

