import sys
import csv

def max_key():
	l = {};

reader = csv.reader(sys.stdin, delimiter='\t')
writer = \
	csv.writer(
	sys.stdout, delimiter='\t', quotechar='"',
	quoting=csv.QUOTE_MINIMAL)
tag_count = 0
current_tag = None
top_10 = []
for line in reader:
	if len(line) == 2:
		tag = line[0]
		if current_tag is None or tag != current_tag:
			if ~(current_tag is None):
				top_10.append([tag,tag_count])
				#print "{0}\t{1}".format(current_tag,tag_count)
				#top_10.sort(key=lambda count_tup: count_tup[1], reverse=True)
				#top_10 = top_10[:10]
			tag_count = 0
			current_tag = tag
		tag_count += 1
	top_10.append([tag,tag_count])
	#print "{0}\t{1}".format(current_tag,tag_count)

	#top_10.sort(key=lambda count_tup: count_tup[1], reverse=True)
	#top_10 = top_10[:10]
count_list = []
prevTag = None
max_count = 0
d = {}
for tag, tag_count in top_10:
	if(prevTag!= None and prevTag != tag):
		
		max_count = max(count_list)
		#print "{0}\t{1}".format(prevTag,max_count)
		d[prevTag] = max_count
		prevTag = tag
		count_list = []
		max_count = 0
	prevTag = tag
	count_list.append(tag_count)
counter = 0
for key, value in sorted(d.iteritems(), reverse = True, key = lambda (k,v):(v,k)):
	print "{0}\t{1}".format(key,value)
	counter += 1
	if (counter == 10):
		break
