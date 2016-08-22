import sys
import os

def solve(x):
	ret ="\n"
	b, a = x.split()
	a = int(a)
	b = int(b)

	vc = []
	for i in range(2**(b-2)):
		st = bin(i)
		lst = len(st)
		rem = b - lst
		s = "1"
		for i in range(rem):
			s = s+"0"
		s = s+st[2:] + "1"
		vc.append(s)

	cnt = 0
	for s in vc:
		if test(s):
			cnt+=1
			ret += s
			for i in range(2, 11):
				n = getnum(s, i)
				t = factors(n)
				tt = 0
				for tm in t:
					if (tm != n) and (tm != 1):
						tt = tm
						break
				ret += " " + str(tm)
			ret += "\n"
			if (cnt == a):
				break
	return ret



def test(s):
	for i in range(2, 11):
		n = getnum(s, i)
		if isPrime(n):
			return False
	return True



import itertools
flatten_iter = itertools.chain.from_iterable
def factors(n):
    return set(flatten_iter((i, n//i)
                for i in range(1, int(n**0.5)+1) if n % i == 0))

from math import sqrt
from itertools import count, islice

def isPrime(n):
    if n < 2: return False
    for number in islice(count(2), int(sqrt(n)-1)):
        if not n%number:
            return False
    return True


def getnum(s, d):
	l = len(s)
	n = 0
	for i in range(l):
		n = n + int(s[i]) * (d**(l-i-1))
	return n



if __name__ == "__main__":
	testcases = input()

	for caseNr in xrange(1, testcases+1):
		cipher = raw_input()
		print("Case #%i: %s" % (caseNr, solve(cipher)))
