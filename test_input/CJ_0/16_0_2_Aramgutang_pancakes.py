#!/usr/bin/env python

import sys

with open(sys.argv[1]) as input:
	input.next()
	for case, line in enumerate(input, 1):
		stack = line.strip()
		previous = stack[0]
		flips = 0
		for pancake in stack:
			if pancake != previous:
				flips += 1
			previous = pancake
		if ((0 if stack[0] == '+' else 1) + flips) % 2:
			flips += 1
		print 'Case #%s: %s' % (case, flips)