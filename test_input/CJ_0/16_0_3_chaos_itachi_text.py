import random
from math import sqrt

def mrange(start, stop, step):
    while start < stop:
        yield start
        start += step


def is_prime(num):
    if num == 2:
        return True
    if (num < 2) or (num % 2 == 0):
        return False
    return all(num % i for i in mrange(3, int(sqrt(num)) + 1, 2))

def sieve(maxNum):
    yield 2
    D, q = {}, 3
    while q <= maxNum:
        p = D.pop(q, 0)
        if p:
            x = q + p
            while x in D: x += p
            D[x] = p
        else:
            yield q
            D[q*q] = 2*q
        q += 2
    raise StopIteration

lll = list(sieve(5000000)) 
lll = sorted(lll)
tc = int(raw_input())
for lol in xrange(1,tc+1):

	N,J = map(int,raw_input().split())
	ll = []
	while len(set(ll)) < J:
		
		temp = '1000000' + ''.join(random.choice('01') for _ in range(N-8)) + '1'
		if not(is_prime(int(temp,2)) or is_prime(int(temp,3)) or is_prime(int(temp,4)) or is_prime(int(temp,5)) or is_prime(int(temp,6)) or is_prime(int(temp,7)) or is_prime(int(temp,8)) or is_prime(int(temp,9)) or is_prime(int(temp,10))):
			ll.append(temp)
		
	ll = list(set(ll))	
	print "Case", "#"+ str(lol)+":"
	for ci in ll:
		v2 = int(ci,2)
		v3 = int(ci,3)
		v4 = int(ci,4)
		v5 = int(ci,5)
		v6 = int(ci,6)
		v7 = int(ci,7)
		v8 = int(ci,8)
		v9 = int(ci,9)
		v10 = int(ci,10)
		for ic in lll:
			if v2%ic == 0:
				l2 = ic
				break
		for ic in lll:
			if v3%ic == 0:
				l3 = ic
				break	
		for ic in lll:
			if v4%ic == 0:
				l4 = ic
				break	
		for ic in lll:
			if v5%ic == 0:
				l5 = ic
				break
		for ic in lll:
			if v6%ic == 0:
				l6 = ic
				break
		for ic in lll:
			if v7%ic == 0:
				l7 = ic
				break
		for ic in lll:
			if v8%ic == 0:
				l8 = ic
				break
		for ic in lll:
			if v9%ic == 0:
				l9 = ic
				break
		for ic in lll:
			if v10%ic == 0:
				l10 = ic
				break
		print ci,l2,l3,l4,l5,l6,l7,l8,l9,l10