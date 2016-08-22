#!/usr/bin/env python3

def flips(s):
	n = 0
	other = {"-": "+", "+": "-"}
	s = list(s)
	while "-" in s:
		first = s[0]
		try:
			i = s.index(other[first])
		except:
			i = len(s)

		for j in range(i):
			s[j] = other[first]
		n += 1

	return n

cases = int(input())

for i in range(cases):
	print("Case #{}: {}".format(i + 1, flips(input())))