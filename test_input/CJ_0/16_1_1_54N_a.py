#!/usr/bin/python

import sys

data_lines = sys.stdin.read().splitlines()
data_lines.reverse()
data_lines.pop()

case = 1
while len(data_lines):
	S = data_lines.pop()
	ls = S[0]
	for c in S[1:]:
		if c >= ls[0]:
			ls = c + ls
		else:
			ls = ls + c
	print "Case #%d: %s" % (case, ls)
	case += 1
