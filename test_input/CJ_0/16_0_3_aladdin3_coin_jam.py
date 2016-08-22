# Google CodeJam 2016 - Qualification Round
# Problem C. Coin Jam
# Author: Mahmoud Aladdin <aladdin3>

import sys
import math

def firstDiv(x):
	if x == 2: return -1
	if x % 2 == 0: return 2
	ff = min(int(math.sqrt(x)), 10**8)
	for i in xrange(3, ff + 1, 2):
		if x % i == 0:
			return i
	return -1

def solve(cn):
	n, j = map(int, raw_input().strip().split())
	print "Case #%d:" % (cn,)
	
	for i in xrange(1 << (n - 2)):
		if j == 0: break
		
		val = '1' + '{0:b}'.format(i).zfill(n - 2) + '1'
		elems = []
		for base in xrange(2, 11):
			ival = int(val, base)
			div = firstDiv(ival)
			if div != -1:
				elems.append(div)
				#print >>sys.stderr, '\t', ival, div
			else:
				break
		
		if len(elems) == 9:
			print val, " ".join(map(str, elems))
			print >>sys.stderr, 'Rem', j, val, " ".join(map(str, elems))
			j -= 1


		

if __name__ == "__main__":
	tc = input()
	for i in xrange(tc):
		solve(i + 1)
