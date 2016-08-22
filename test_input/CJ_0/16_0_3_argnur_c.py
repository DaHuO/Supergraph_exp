#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

def divider(n):
	for i in range(2, 256):
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
	# print(b)
	divs = []
	for j in range(2, 11):
		num = int(b, j)
		# print(num)
		d = divider(num)
		if d != -1:
			divs.append(d)
		else:
			break
	# print(divs)
	if len(divs) == 9:
		print(b, end=" ")
		for j in divs:
			print(j, end=" ")
		count+=1;
		print()

