import sys

def solve(s):
	if len(s) == 1:
		if s == '-':
			return 1
		else:
			return 0
	swaps = 0
	p = s[0]
	for i in xrange(1, len(s)):
		if s[i] != p:
			p = s[i]
			swaps += 1
	if s[-1] == '-':
		swaps += 1
	return swaps

cases = int(sys.stdin.readline().strip())

for case in xrange(cases):
	print 'Case #%d:' % (case + 1),
	print solve(sys.stdin.readline().strip())
