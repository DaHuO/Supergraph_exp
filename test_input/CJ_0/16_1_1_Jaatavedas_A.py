#!/usr/bin/env python3.4
import math
import re


ip=open("A-large.in",'r')
op=open("A.out",'w')
case=1
no = ip.readline()
no = int(no)

for i in range(0,no):
	s=ip.readline()
	res=""
	for j in range(0,len(s)): 
		if j==0:
			res=s[0]
		elif s[j]<res[0]:
			res=res+s[j]
		else:
			res=s[j]+res

	op.write("Case #"+str(case)+": "+res)
	case+=1
ip.close()
op.close()
