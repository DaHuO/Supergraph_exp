import math

def isPrime(x):
	
	s = int(math.sqrt(x)) + 1
	
	if x%2 == 0:
		return (False, 2)

	i = 3
	while i < s:
		if x % i == 0:
			return (False, i)
		i += 2
	return (True, -1)

def _try_composite(a, d, n, s):
	if pow(a, d, n) == 1:
		return False
	for i in range(s):
		if pow(a, 2**i * d, n) == n-1:
			return False
	return True # n  is definitely composite
 
def is_prime(n, _precision_for_huge_n=16):
	if n in _known_primes or n in (0, 1):
		return True
	if any((n % p) == 0 for p in _known_primes):
		return False
	d, s = n - 1, 0
	while not d % 2:
		d, s = d >> 1, s + 1
	# Returns exact according to http://primes.utm.edu/prove/prove2_3.html
	if n < 1373653: 
		return not any(_try_composite(a, d, n, s) for a in (2, 3))
	if n < 25326001: 
		return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
	if n < 118670087467: 
		if n == 3215031751: 
			return False
		return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
	if n < 2152302898747: 
		return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
	if n < 3474749660383: 
		return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
	if n < 341550071728321: 
		return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
	# otherwise
	return not any(_try_composite(a, d, n, s) 
				   for a in _known_primes[:_precision_for_huge_n])

_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]


import random

def gcd(a,b):
	while b:
		a,b=b,a%b
	return a

def brent(N):
		if N%2==0:
				return 2
		y,c,m = random.randint(1, N-1),random.randint(1, N-1),random.randint(1, N-1)
		g,r,q = 1,1,1
		while g==1:			 
			x = y
			for i in range(r):
				y = ((y*y)%N+c)%N
			k = 0
			while (k<r and g==1):
				ys = y
				for i in range(min(m,r-k)):
					y = ((y*y)%N+c)%N
					q = q*(abs(x-y))%N
				g = gcd(q,N)
				k = k + m
			r = r*2
		if g==N:
			while True:
				ys = ((ys*ys)%N+c)%N
				g = gcd(abs(x-ys),N)
				if g>1:
					break
		 
		return g


def check(x):
	ret = []
	for b in range(2, 11):

		u = x
		v = 0
		mul = 1
		while u != 0:
			v += mul*(u&1)
			u = u>>1
			mul *= b

		# print v
		t = is_prime(v)
		if t == False:
			fact = brent(v)
			ret.append(fact)
			# print v
		else:
			ret = []
			return ret
	return ret		

upperb = 1<<30
i = 0
x = 0
count = 0
while i < upperb and count < 500:
	x = i<<1 | 1 | 1<<31
	
	ret = check(x)
	if len(ret) != 0:
		count += 1
		print bin(x)[2:],
		for p in ret:
			print p,
		print
	i += 1

# print check(int('10000000000000000000000001010011', 2))