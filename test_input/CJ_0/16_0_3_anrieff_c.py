#!/usr/bin/env python

# Contestant: Veselin 'anrieff' Georgiev
# Round: Google Code Jam Qualification 2016
# Task: Coin Jam
# Solution: Use python's big integers for the computation. Generate random numbers and use trial division until d = 10000 to check for primality.
#           A number that has no divisors less than 10k is deemed prime. Thus the output solutions only contain numbers, that are somewhat "smooth" in each base for 2 to 10.

import random

random.seed(42)

TC = int(raw_input().strip())

l, n = map(int, raw_input().strip().split())

seen = {}

def generate_number():
	while True:
		s = '1'
		for j in xrange(l - 2):
			s += str(random.randint(0, 1))
		s += '1'
		if s in seen: continue
		
		# check for non-primality in each base:
		divisors = []
		for base in xrange(2, 11):
			x = int(s, base)
			found = False
			for d in xrange(2, min(10000, x)):
				if x % d == 0:
					divisors.append(d)
					found = True
					break
			if not found:
				divisors.append(-1)
				break
		if divisors.count(-1) != 0:
			continue
		return (s, divisors)
		
		

for i in xrange(n):
	# generate the number:
	number, divisors = generate_number()
	seen[number] = divisors

print "Case #1:"
for item in seen:
	print item, " ".join(map(str, seen[item]))

