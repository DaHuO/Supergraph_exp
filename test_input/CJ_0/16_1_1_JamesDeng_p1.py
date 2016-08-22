# -*- coding: utf-8 -*-
"""
Created on Fri Apr 08 23:09:21 2016

@author: dan
"""

import copy
def solve(t):
	current=""
	mylist=[]
	rest=t
	finder(t,current,mylist,rest)
	mylist.sort()
	print mylist[-1]

def finder(t,current,mylist,rest):
	if len(rest)==0:
		mylist.append(current)
	else:
		finder(t,current+rest[0],mylist,rest[1:])
		finder(t,rest[0]+current,mylist,rest[1:])
		


t = int(raw_input())  
test=[[0 for _ in range(3)] for _ in range(t)] 

for i in xrange(1, t + 1):
	test[i-1]=raw_input().strip()
	


for i in range(1,t+1):
	print "Case #"+str(i)+":",
	solve(test[i-1])
