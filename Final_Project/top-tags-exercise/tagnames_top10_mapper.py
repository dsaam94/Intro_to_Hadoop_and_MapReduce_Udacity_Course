#!/usr/bin/python


import sys
import csv

reader = csv.reader(sys.stdin, delimiter = '\t', lineterminator="\N", quotechar = '"', quoting = csv.QUOTE_ALL)
writer = csv.writer(sys.stdout, delimiter = '\t', quotechar = '"', quoting = csv.QUOTE_ALL)
for line in reader:
	tagnames = line[2]
	node_type = line[5]
	if(node_type == 'question'):

		if len(tagnames) == 1:
			words = tagnames
		else:
			words = tagnames.strip().split(' ')
		for tag in words:
			writer.writerow([tag, "1"])
	
