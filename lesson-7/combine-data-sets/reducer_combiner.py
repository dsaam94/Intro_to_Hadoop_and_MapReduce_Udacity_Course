#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys

user_id = None
new_user_id = None

def reducer():
    for line in sys.stdin:
        
        # YOUR CODE HERE
        data = line.strip().split("\t")
        if (len(data) != 6 or len(data) != 19):
            continue
        
        if(len(data) == 6):
            new_user_id, key_users, reputation, gold, silver, bronze = data
        else:
            new_user_id, key_node, title, tagnames,  author_id,  node_type,  parent_id,  abs_parent_id,  added_at, score = data 
        
        if user_id and user_id != new_user_id:
           print user_id, "\t",  title,"\t",  tagnames, "\t",  node_type,"\t",  parent_id,"\t",  abs_parent_id, "\t", added_at,"\t", score,"\t",  reputation,"\t",  gold,"\t",  silver,"\t",  bronze
           user_id = new_user_id
        
        user_id = new_user_id
        
        if user_id != None:
           print user_id, "\t",  title,"\t",  tagnames,"\t",  node_type,"\t",  parent_id,"\t",  abs_parent_id, "\t", added_at,"\t", score,"\t",  reputation,"\t",  gold,"\t",  silver,"\t",  bronze
 
 reducer()