#!/usr/bin/python

import sys

data_lines = sys.stdin.read().splitlines()
data_lines.reverse()
data_lines.pop()

def solve(line):
	changes = 0
	for i in range(1,len(line)):
		if line[i-1] != line[i]:
			changes += 1

	if line[-1] == '-':
		changes += 1

	return changes

case = 1
while len(data_lines):
	x = data_lines.pop()
	flips = solve(x)
	print 'Case #%d: %d' % (case, flips)
	case += 1
