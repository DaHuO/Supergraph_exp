# Google CodeJam 2016 - Qualification Round
# Problem B. Revenge of the Pancakes
# Author: Mahmoud Aladdin <aladdin3>

import sys

def getLast(st, val):
	try:
		return (len(st) - 1) - st[::-1].index(val)
	except:
		return -1

def reverse(st, cnt):
	st[:cnt] = map(lambda x: not x, st[:cnt])
	st[:cnt] = st[:cnt][::-1]
	return st

def solve(cn):
	line = raw_input().strip()
	st = [True if x == '+' else False for x in line]
	
	cnt = 0
	swap = True
	while swap:
		swap = False
		ind = getLast(st, False)
		if ind != -1:
			swap = True
			if st[0]:
				ind2 = getLast(st[:ind], True)
				print >>sys.stderr, '\t', ind2, st
				st = reverse(st, ind2 + 1)
				print >>sys.stderr, '\t', st
				cnt += 1
			print >>sys.stderr, ind, st
			st = reverse(st, ind + 1)
			print >>sys.stderr, st
			cnt += 1
	print "Case #%d: %d" % (cn, cnt)


if __name__ == "__main__":
	tc = input()
	for i in xrange(tc):
		solve(i + 1)
