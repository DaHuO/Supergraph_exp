# Google CodeJam 2016 - Round 1A
# Problem A. The Last Word
# Author: Mahmoud Aladdin <aladdin3>

import sys
import math

def solve(cn):
	S = raw_input().strip()
	sol = S[0]
	for ch in S[1:]:
		if ord(ch) >= ord(sol[0]):
			sol = ch + sol
		else:
			sol += ch
	print "Case #%d: %s" % (cn, sol)
	


		

if __name__ == "__main__":
	tc = input()
	for i in xrange(tc):
		solve(i + 1)
