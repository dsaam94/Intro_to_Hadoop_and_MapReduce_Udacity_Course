#!/usr/bin/python

import sys


oldKey = None
posts_per_hour = {}

def exists(key):
	return posts_per_hour.has_key(key)


for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
		continue
    	thisKey, thisHour = data_mapped	
	thisHour = int(thisHour)
	if (len(data_mapped) == 2):
		if(~exists(thisHour)):
			posts_per_hour[thisHour] = 0 
		posts_per_hour[thisHour] += 1

	if(oldKey and oldKey!=thisKey ):
		max_posts_count = max(posts_per_hour.values())
		hour_with_max_posts = [hour for hour,count in posts_per_hour.items() if count == max_posts_count]
		for post_hour in sorted(hour_with_max_posts):
			print oldKey, "\t", post_hour

		posts_per_hour = {}

	oldKey = thisKey


if oldKey != None and posts_per_hour.values():
	max_posts_count = max(posts_per_hour.values())
	hour_with_max_posts = [hour for hour,count in posts_per_hour.items() if count == max_posts_count]
	for post_hour in hour_with_max_posts:
		print oldKey, "\t", post_hour



