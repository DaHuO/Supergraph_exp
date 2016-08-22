#!/usr/bin/python

import math

txt = open("B-large.in", "r")

out = open("a.txt", "w")
dic = {}
case = 0

def aaaa(x):
	if x == '-':
		x = '+'
	else:
		x = '-'
	return x

for k in range(int(txt.readline().strip())):
	for i in txt:
		i = i.strip()
		case = case + 1
		count = 0
		out.write("Case #"+  str(case) + ": ")
		end = len(i)
		while 1:
			if len(filter(lambda x: x == '-', i)) == 0:
				out.write(str(count) + '\n')
				break
			end = len(i) - list(reversed(i)).index('-')
			if i[0] == '+':
				first = i.index('-')
				if first != 0:
					i = ''.join(['-']*first) + i[first:]
					count = count + 1
			i = "".join(map(aaaa, reversed(i[:end]))) + i[end:]
			count = count + 1
		