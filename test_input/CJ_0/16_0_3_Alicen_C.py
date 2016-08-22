#!/usr/bin/python3

import random

smallData = dict()
bigData = dict()

def getSmallDivisor(num):
	for i in range(2, 1000):
		if num % i == 0 and num != i:
			return i
	return None

def verify(num):
	erg = (str(num), [])
	for i in range(2, 11):
		interpret_number = int(num, i)
		a = getSmallDivisor(interpret_number)
		if a is None:
			return None
		erg[1].append(str(a))
	return erg


def calcHelper(mem, N, J, found):
	while found < J:	
		s = "1" + ''.join(random.choice(["0", "1"]) for __ in range(N-2)) + "1"	
		erg = verify(s)
		if erg is not None and erg[0] not in mem:
			mem.update({erg[0]:erg[1]})
			found+=1


def calcbefore():
	calcHelper(smallData, 16, 50, 0)
	calcHelper(bigData, 32, 500, 0)	

calcbefore()

T = int(input())
N, J = map(float, input().split(' '))

if(N == 16):
	act = smallData
else:
	act = bigData

print("Case #1:")

for num, div in act.items():
	print(num, ' '.join(div))
