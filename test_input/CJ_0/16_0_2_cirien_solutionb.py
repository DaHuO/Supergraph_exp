#!/usr/bin/python

import sys
import array

f = open(sys.argv[1],'r')
t = int(f.readline())

def allHappy(pancakes):
	for p in pancakes:
		if (p == '-'):
			return False
	return True

for case in range(t):
	pancakestate = list(f.readline())
	flips = 0
	#print ("case: " + str(case) + "pancakestate: " + str(pancakestate) + "flips: "+ str(flips))
	while(not allHappy(pancakestate)):
		#print(pancakestate)
		#find the first block of unhappy pancakes
		unhappyStart  = -1
		unhappyEnd = -1
		for index in range(len(pancakestate)-1):
			if ((unhappyStart == -1) and (pancakestate[index] == '-')):
				unhappyStart = index
				continue
		#find end of the block of unhappy pancakes
			if ((unhappyStart != -1) and (pancakestate[index] == '+')):
				unhappyEnd = index - 1
				break
		if (unhappyEnd == -1):
			unhappyEnd = len(pancakestate) - 1
		#print ("unhappyStart: " + str(unhappyStart) + "unhappyEnd: " + str(unhappyEnd))
		if (unhappyStart == 0):
			flips += 1
		else:
			flips += 2
		for flipped in range(unhappyStart, unhappyEnd+1):
			pancakestate[flipped] = '+'
	print ("Case #" + str(case+1) + ": " + str(flips))