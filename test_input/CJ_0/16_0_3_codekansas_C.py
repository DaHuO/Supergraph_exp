# program

from math import sqrt
from itertools import count, islice

N = 32
J = 500

def isPrime(n):
	if n < 2:
		return None
	try:
		return (i for i in islice(count(2), int(10)) if n % i == 0).next()
	except StopIteration:
		return None

c = 0
n = 2 ** (N-1) + 1

print('Case #1:')

while c < J:
	s = bin(n)[2:]
	for i in range(2, 11):
		if not isPrime(long(s, i)):
			break
	else:
		c += 1
		print(s + ' ' + ' '.join([str(isPrime(long(s, i))) for i in range(2, 11)]))
	n += 2
