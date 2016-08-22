import numpy as np

#This is run aftet the preprocessor

def factor(l, n):
	for p in l:
		if n == p:
			return False
		if n % p == 0:
			return p
	return False


def get_jam(N,J):
	j = 0
	with open('Cprimes.pkl','rb') as f:
		primes = np.load(f)
		max_mid = int(str(10**(N-2)),2)
		for i in range(max_mid):
			num_str = '1{}1'.format(np.binary_repr(i,N-2))
			divisors = []
			for base in range(2,11):
				divisor = factor(primes, int(num_str,base))
				if not divisor:
					break
				divisors.append(divisor)
			if len(divisors) == 9:
				divisors = map(str,divisors)
				print('{} {}'.format(num_str, ' '.join(divisors)))
				j += 1
				if j == J:
					return

					
get_jam(16, 50)