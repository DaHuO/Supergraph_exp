prime_list = [2]
for i in range(3, 1000):
	for prime in prime_list:
		if ((i % prime) == 0):
			break
	else:
		prime_list.append(i)

import random
def attempt_gen(size):
	n = random.randint(0, 2**(size - 2) - 1)
	n *= 2
	n += 1
	n += 2**(size - 1)
	str_n = bin(n)[2:]
	divisors = []
	for i in range(2, 11):
		base_i_n = int(str_n, i)
		for prime in prime_list:
			if (base_i_n % prime == 0):
				divisors.append(prime)
				break
		else:
			return
	return (str_n, divisors)

T = input()
NJ = raw_input().split()
N = int(NJ[0])
J = int(NJ[1])

found = {}
while len(found) < J:
	out = attempt_gen(N)
	if out:
		str_n, divisors = out
		found[str_n] = divisors
print 'Case #1:'
for str_n in found:
	print ' '.join([str_n] + [str(i) for i in found[str_n]])


