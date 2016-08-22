# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:39:53 2016

@author: aanderson
"""

#7
#CAB
#JAM
#CODE
#ABAAB
#CABCBBABC
#ABCABCABC
#ZXCASDQWE

import numpy as np

N = int(raw_input())
for i in xrange(1, N + 1):
	S = raw_input()
	Sout = S[0]
	for s in xrange(1,len(S)):
		if S[s] >= Sout[0]:
			Sout = S[s] + Sout
		else:
			Sout = Sout + S[s]
	
	print "Case #{}: {}".format(i, Sout)