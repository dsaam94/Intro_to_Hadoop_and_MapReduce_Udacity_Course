import sys
import csv
import re

def mapper():
	reader = csv.reader(sys.stdin, delimiter = '\t', lineterminator="\N", quotechar = '"', quoting = csv.QUOTE_ALL)
	writer = csv.writer(sys.stdout, delimiter = '\t', quotechar = '"', quoting = csv.QUOTE_ALL)
	#characters = ['.',',','!','?',':',';','"','<','>','(',')','[',']','#','$','=','-','/',' ']
	for line in reader:

		body = line[4]
		line_id = line[0]
		body = re.sub('\W+',' ',body)
		words = body.strip().split(' ')
		
		for word in words:
			print "{0}\t{1}".format(word.lower(),line_id)
mapper()
