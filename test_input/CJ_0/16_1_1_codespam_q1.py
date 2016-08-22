#!/usr/bin/env pypy

import sys


def conv(l):
	return l


def run(case):
	s = case[0]
	r = s
	for f in case[1:]:
		if r + f >= f + r:
			r = r + f
		else:
			r = f + r
		#print r, f
	print r


CASES = [conv(x.strip()) for x in sys.stdin.readlines()[1:]]

for case_no, case in enumerate(CASES):
	print 'Case #%d:' % (case_no + 1),
	run(case)
