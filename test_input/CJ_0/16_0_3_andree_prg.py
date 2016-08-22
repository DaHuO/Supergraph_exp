#!/usr/bin/env python3

import numpy
import math

DEBUG=True
DEBUG=False

PRIME_LIMIT = None

def generator(n):
	first = (1 << (n - 1)) + 1
	last = (1 << (n)) - 1
	for i in range(first, last + 1):
		if not i % 2:
			continue
		yield i

def getPrimeDivisor(v):
	# CPU time looks less expensive to memory for such big numbers...
	if v in [2, 3]:
		# the number itself is a prime, we don't want that...
		raise("Shouldn't happen for the test range...")

	if v % 2 == 0:
		return 2
	if v % 3 == 0:
		return 3

	iMax = math.sqrt(v)
	if PRIME_LIMIT != None:
		iMax = PRIME_LIMIT
	i = 5
	w = 2
	while i <= iMax:
		if v % i == 0:
			return i
		i += w
		w = 6 - w

	return None

def checkCoinity(v):
	strV = "{0:b}".format(v)
	rv = []
	if DEBUG:
		print("--- ", strV)

	for base in range(2, 11):
		parsedV = int(strV, base)
		if DEBUG:
			print("  == ({}) {}".format(base, parsedV))
		div = getPrimeDivisor(parsedV)

		if div == None:
			# not a coin...
			return []
		else:
			rv += [div]
	return rv

def calculate(n, j):
	rv = []

	for v in generator(n):
		divs = checkCoinity(v)
		if divs != []:
			rv += ["{0:b} {1}".format(v, ' '.join([str(d) for d in divs]))]
			if len(rv) == j:
				break
	return rv

t = int(input())
for i in range(1, t + 1):
	n, j = [int(x) for x in input().split(' ')]
	PRIME_LIMIT = 1021
	r = calculate(n, j)
	if len(r) != j:
		# bad luck finding 'j' results, let's go full hardcore...
		PRIME_LIMIT = None
		r = calculate(n, j)
	print("Case #{}:\n{}".format(i, '\n'.join(r)))
