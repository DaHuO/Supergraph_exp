import math

def sieveOfAtkin(limit):
    P = [2,3]
    sieve=[False]*(limit+1)
    for x in range(1,int(math.sqrt(limit))+1):
        for y in range(1,int(math.sqrt(limit))+1):
            n = 4*x**2 + y**2
            if n<=limit and (n%12==1 or n%12==5) : sieve[n] = not sieve[n]
            n = 3*x**2+y**2
            if n<= limit and n%12==7 : sieve[n] = not sieve[n]
            n = 3*x**2 - y**2
            if x>y and n<=limit and n%12==11 : sieve[n] = not sieve[n]
    for x in range(5,int(math.sqrt(limit))):
        if sieve[x]:
            for y in range(x**2,limit+1,x**2):
                sieve[y] = False
    for p in range(5,limit):
        if sieve[p] : P.append(p)
    return P

primes = sieveOfAtkin(10000)[:5000]

def is_prime(x):
	_x = math.sqrt(x)
	for p in primes:
		if p > _x: break
		if x % p == 0: return False
	return True
n = 32
t = 500
p = {}
bases = range(2,11)
for i in bases:
	p[i] = [1]
	for j in range(1,n + 1):
		p[i].append(p[i][j-1] * i)
	# print p[i]
# print (1 << (n-1)) + 1
# print 1 << n
print 'Case #1:'
for z in xrange((1 << (n-1)) + 1, 1 << n, 2):
	ok = True
	for base in bases:
		x = z
		y = 0
		i = 0
		# print base
		while x > 0:
			y += p[base][i] * (x % 2);
			# print p[base][i], (x & 1)
			x /= 2
			i += 1
		if is_prime(y):
			ok = False
			break
	if ok:
		t -= 1
		print y, 
		for base in bases:
			x = z
			y = 0
			i = 0
			while x > 0:
				y += p[base][i] * (x & 1);
				x >>= 1
				i += 1
			i = 0
			while y % primes[i] != 0:
				i += 1
			print primes[i],
		print
		if t <= 0: break;
# print len(p)