#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

def myDivi(n):
	for i in range(2, math.floor(math.sqrt(n)) + 1):
		if n%i==0: return i
	return -1

t = input()
case = input()

n, m = map(int, case.split())

s = 2**(n-1) + 1
f = 2**n
count = 0

print("Case #1:")

for i in range(s, f):
	if count == m:
		break
	b = "{0:b}".format(i)
	if b[-1] == '0': continue
	divis = []
	for j in range(2, 11):
		number = int(b, j)
		d = myDivi(number)
		if d != -1:
			divis.append(d)
		else:
			break
	if len(divis) == 9:
		print(b, end=" ")
		for j in divis:
			print(j, end=" ")
		count+=1;
		print()