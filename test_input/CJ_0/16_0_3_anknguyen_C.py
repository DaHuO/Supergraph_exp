#!/usr/bin/env python3
import math

def isprime(n):
	sqrt = int(math.sqrt(n))
	if n % 2 == 0:
		return 2
	for i in range(3, sqrt + 1, 2):
		if n % i == 0:
			return i

	return 0

def zpad(s, a):
	return "0" * (a - len(s)) + s

n = 16
j = 50

js = {}

for i in range(2**(n-2)):
	if len(js) == j:
		break

	candidate = "1" + zpad(bin(i)[2:], n - 2) + "1"
	current = []

	for base in range(2, 11):
		m = int(candidate, base = base)
		current.append(isprime(m))

	if current.count(0) == 0:
		js[candidate] = current


for c in js:
	print("{} {}".format(c, " ".join([str(x) for x in js[c]])))