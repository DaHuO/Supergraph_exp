# You can install sympy with pip with the following command: pip install sympy
from sympy.ntheory import isprime, pollard_pm1

t = int(raw_input())
N, J = [int(s) for s in raw_input().split(" ")]

for j in xrange(1, t+1):
	print "Case #{}:".format(j)
	found = 0

	for i in xrange(2**(N-2), 2**(N-1)):

		if found == J:
			break

		jamcoin = str(bin(i))[2:] + '1'
		non_trivial_divisors = []

		for base in xrange(2, 11):
			jamcoin_base = int(jamcoin, base)
	
			if isprime(jamcoin_base):
				break
		
			else:
				div = pollard_pm1(jamcoin_base, retries = 6)
				if div:
					non_trivial_divisors.append(div)
	
		if len(non_trivial_divisors) == 9:
			found += 1
			divisors_str = ""
			for i in non_trivial_divisors:
				divisors_str += str(i) + " "
		
			print jamcoin, divisors_str[:-1]
