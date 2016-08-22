from math import floor, sqrt

def is_spsp(n, a):
	d, s = n-1, 0
	while d%2 == 0:
		d /= 2
		s += 1
	if pow(a, d, n) == 1:
		return True
	for r in xrange(s):
		if pow(a, d*pow(2, r), n) == n-1:
			return True
	return False

def is_prime(n):
	ps = [2, 3, 5, 7, 11, 13, 17]
	if n in ps:
		return True
	for p in ps:
		if not is_spsp(n, p):
			return False
	return True

def fac(num):
	step = lambda x: 1 + (x << 2) - ((x >> 1) << 1)
	maxq = long(floor(sqrt(num)))
	d = 1
	q = num % 2 == 0 and 2 or 3
	while q <= maxq and num % q != 0:
		q = step(d)
		d += 1
	if q <= maxq:
		yield q
		for gen in fac(num/q):
			yield gen
	else:
		yield num


for t in xrange(1, int(raw_input()) + 1):
	n, j = map(int, raw_input().split())

	a = 2**(n - 1) + 1
	b = bin(a)[2:]

	print 'Case #%s:' % t

	while j:
		a += 2
		b = bin(a)[2:]
		for base in xrange(2, 11):
			nm = int(b, base)
			if is_prime(nm):
				break
		else:
			j -= 1
			print nm,
			for base in xrange(2, 11):
				nm = int(b, base)
				print fac(nm).next(),
			print
