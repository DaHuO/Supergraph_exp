import random
from math import log
def primecheck(prime):
	v = 1
	n = prime - 1
	s = 0
	while n%2 ==0:
		n = n/2
		s = s + 1
	pot = 100.00
	a = random.SystemRandom().randrange(2, int(pot))
	for z in range(2, int(pot)):
		prtest = False
		for w in range(s):
			a = z
			binp = bin((2**w)*n)
			sig = 1	
			for x in range(len(binp)-2):
				a = (a*a)%prime
				if binp[len(binp) - (x+1)] is '1':
					sig = sig * (a)
			if (sig%prime) == 1 or prime-(sig%prime) == 1:
				prtest = True
				break
	return prtest