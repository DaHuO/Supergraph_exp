#!/usr/bin/env python

import time
import threading
import random
import sys
from math import sqrt

N = 32
J = 500

used = set()

def getDivisor(x):
	if x % 2 == 0:
		return 2
	for p in range(3, int(sqrt(x))+2, 2):
		if x % p == 0:
			return p
	return 0

def changeBase(x, b):
	res = 0
	e = 1
	while x:
		res += e * (x & 1)
		e *= b
		x >>= 1
	return res

def check(x):
	div = [0,0,0,0,0,0,0,0,0,0,0]
	ok = True
	for b in range(2,11):
		n = changeBase(x, b)
		d = getDivisor(n)
		if d == 0:
			ok = False
			break
		div[b] = d
		
	if ok:
		return div
	else:
		return None

def compute(j, threadId):
	while j > 0:
		x = random.getrandbits(N)
		x |= 1
		x |= 1 << (N-1)
		
		div = check(x)
		if div != None and not x in used:
			j -= 1
			used.add(x)
			
			res = str(changeBase(x, 10)) + " "
			for b in range(2,11):
				res += str(div[b]) + " "
			print(res, flush=True)
			
			print("thread=" + str(threadId) + " j=" + str(int(j)) + " J=" + str(500-len(used)), file=sys.stderr)

T = 2
threads = []
for t in range(T):
	thread = threading.Thread(target=compute, args=(J/T,t,))
	thread.daemon = True
	thread.start()
	threads.append(thread)

time.sleep(3)
exit(0)
