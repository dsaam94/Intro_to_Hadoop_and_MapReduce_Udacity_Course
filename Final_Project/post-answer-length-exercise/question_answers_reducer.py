#!/usr/bin/python

import sys


oldKey = None
answerCount = 0;
totalAnswerLength = 0.0;
ques_length = 0;
# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue

    id, type, length = data_mapped
	
    if oldKey and oldKey != id:
	if(answerCount > 0):
		averageAnswerLength = totalAnswerLength / answerCount
        else:
		averageAnswerLength = 0
	print "{0}\t{1}\t{2}".format(oldKey, ques_length, averageAnswerLength)
        oldKey = id;
        answerCount = 0;
	totalAnswerLength = 0.0;
	ques_length = 0;
    if type == 'question':
	ques_length = length
    else:
	answerCount += 1
	totalAnswerLength = totalAnswerLength + float(length) 


    oldKey = id



