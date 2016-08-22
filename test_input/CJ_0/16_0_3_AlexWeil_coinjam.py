# Every digit is either 0 or 1.
# The first digit is 1 and the last digit is 1.
# If you interpret the string in any base between 2 and 10, inclusive, the resulting number is not prime.
from functools import lru_cache
from itertools import product
from fractions import gcd
from random    import randint

@lru_cache(None)
def miller_rabin_prime(n):
	if n < 3:
		return True
	d, s = n - 1, 0
	while not d % 2:
		d >>= 1
		s +=  1
	test = lambda a: not pow(a, d, n) == 1 and all(pow(a, 2**i * d, n) != n - 1 for i in range(s))
	return not any(test(a) for a in (2, 7, 61))

def brent_factor(n):
	if n % 2 == 0:
		return 2

	y, c, m = (randint(1, n-1, ) for _ in range(3))
	g = r = q = 1
	fx = lambda y: ((y * y) % n + c) % n
	
	while g == 1:
		x = y
		for _ in range(r):
			y = fx(y)
		
		k = 0
		while k < r and g == 1:
			ys = y
			for _ in range(min(m, r - k)):
				y = fx(y)
				q *= abs(x - y) % n
			g = gcd(q, n)
			k += m
		r += r

	if g == n:
		while g <= 1:
			ys = fx(ys)
			g = gcd(abs(x - ys), n)
	return g

def valid_factor(n):
	factor = brent_factor(n)
	while factor in (1, n):
		factor = brent_factor(n)
	return factor

def is_jamcoin(n):
	starts_and_ends_with_1 = lambda n: n[0] == n[-1] == '1'
	is_binary			   = lambda n: all(d in ('0', '1') for d in n)
	has_prime_base		   = lambda n: any(miller_rabin_prime(int(n, i)) for i in range(2, 11))
	return starts_and_ends_with_1(n) and is_binary(n) and not has_prime_base(n)
		
def generate_jamcoins(n, j):
	possible_coins = (''.join(combination) for combination in product('10', repeat=n))
	jamcoins = (coin for coin in possible_coins if is_jamcoin(coin))
	for _ in range(j):
		coin = next(jamcoins)
		factors = ' '.join(str(valid_factor(int(coin, base))) for base in range(2, 11))
		print(coin, factors)
print("Case #1:")
generate_jamcoins(16, 50)

# with open('A-large.in') as data:
# 	first = int(data.readline())
# 	for i in range(1, first + 1):
# 		line = int(data.readline())
# 		digits = has_all_digits(line)
# 		if digits:
# 			print("Case #%i: %i" % (i, digits))
# 		else:
# 			print("Case #%i: InSOMnIA" % i)