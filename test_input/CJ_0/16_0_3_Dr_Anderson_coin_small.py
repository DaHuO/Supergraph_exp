# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:39:53 2016

@author: aanderson
"""


#100011 5 13 147 31 43 1121 73 77 629

import numpy as np
import pyprimes
from util import listAsBase
import signal


N = 32
J = 500
cnt = 0
t0 = 2

minNum = listAsBase([1] + [0]*(N-2) + [1], 2)
maxNum = listAsBase([1] + [1]*(N-2) + [1], 2)

#BadList = [2147483657, 2147483671, 2147483731, 2147483773, 2147483803, 2147483809, 2147483837, 2147483839, 2147483843]

def handler(signum, frame):
	raise Exception("timing out")

signal.signal(signal.SIGALRM, handler)

print "Case #1:"
for n in xrange(minNum, maxNum+1, 2):
	numList = [int(x) for x in list(bin(n))[2:]]
	
#	if n in BadList:
#		continue
	signal.alarm(t0)
	factList = []*0
	for B in xrange(2,11):
		num = listAsBase(numList, B)
		if pyprimes.isprime(num):
			break
		try:
			facts = pyprimes.factorise(num)
			factList.append(next(facts)[0])
		except Exception, exc: 
			break

	if len(factList) == 9:
		cnt = cnt + 1
		print ''.join(map(str, list(bin(n))[2:])) + ' ' + ' '.join(map(str, factList))
	
	if cnt >= J:
		break