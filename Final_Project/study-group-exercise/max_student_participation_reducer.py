#!/usr/bin/python

import sys


oldKey = None
participants = []
# Loop around the data
# It will be in the format key\tval

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    question_id, author_id = data_mapped
	
    if oldKey != None and oldKey != question_id:
	print "{0}\t{1}".format(oldKey, participants)
        oldKey = question_id;
	participants = []
    
    oldKey = question_id
    participants.append(author_id)


