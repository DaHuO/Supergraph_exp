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


def naive(length,count):

	jamcoins = set()
	n = 0
	while count:
		n += 1
		b = '1' + ''.join(str(random.randint(0,1)) for _ in range(length-2)) + '1'
		
		if b in jamcoins:
			continue
		
		factors = []
		for base in range(2,10+1):
			k = int(b, base)
			factor = None
			for i in range(3, 1000):
				if i*i > k: break
				if k % i == 0:
					factor = i
					break
			if factor == None:
				factors = None
				break
			else:
				factors.append(factor)
		
		if factors != None:
			print b,' '.join(map(str,factors))
			jamcoins.add(b)
			count -= 1
	# print n


n_cases = input()

for case in range(1, n_cases+1):
	n,j = map(int,raw_input().split(' '))
	print 'Case #%d:' % case
	naive(n,j)