#!/usr/bin/python


import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter = '\t', lineterminator="\N", quotechar = '"', quoting = csv.QUOTE_ALL)
#writer = csv.writer(sys.stdout, delimiter = '\t', quotechar = '"', quoting = csv.QUOTE_ALL)
for line in reader:
	node_id = line[0]
	node_type = line[5]
	author_id = line[3]
	abs_parent_id = line[7]
	if(node_type == "question"):
		print "{0}\t{1}".format(node_id,author_id)
	else:
		identifier = abs_parent_id
		print "{0}\t{1}".format(identifier,author_id)


