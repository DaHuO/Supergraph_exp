import sys
from math import ceil

def solve(l, q):
	coins = []
	f = '{:0%db}' % (l - 2)
	i = 0
	while len(coins) < q:
		b = '1%s1' % f.format(i)
		d = []
		for base in xrange(2, 11):
			n = int(b, base)
			for t in xrange(2, 10000):
				if n % t == 0:
					d.append(str(t))
					break
		if len(d) == 9:
			coins.append('%s %s' % (b, ' '.join(d)))
			print coins[-1]
		i += 1
	return '\n'.join(coins)

cases = int(sys.stdin.readline().strip())

for case in xrange(cases):
	print 'Case #%d:' % (case + 1)
	n, j = map(int, sys.stdin.readline().strip().split())
	solve(n, j)
