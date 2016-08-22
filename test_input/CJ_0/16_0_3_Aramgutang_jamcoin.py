#!/usr/bin/env python

import sys

with open(sys.argv[1]) as input:
	input.next()
	for case, line in enumerate(input, 1):
		N, J = map(int, line.strip().split(' '))
		print 'Case #%s:' % case
		found = 0
		for inner in xrange(2**(N-2)):
			full = '1%s1' % bin(inner)[2:].zfill(N-2)
			divisors = []
			for base in range(2, 11):
				number = int(full, base)
				#for divisor in range(2, number // 2):
				for divisor in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]:
					if not number % divisor:
						divisors.append(divisor)
						break
				else:
					break
			if len(divisors) < 9:
				continue
			found += 1
			print ' '.join([full] + map(str, divisors))
			if found >= J:
				break