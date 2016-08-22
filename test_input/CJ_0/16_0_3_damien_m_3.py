import random

N = 32
J = 500

found = set()
sols = []
while len(sols) < J:
	digits = '1' + ''.join([random.choice('01') for _ in range(N-2)]) + '1'
	if digits not in found:
		#print('try', digits)
		divisors = []
		for base in range(2, 11):
			n = int(digits, base)
			#print(base, int(digits, base))
			for divisor in range(2, min(n, 10000)):
				if n % divisor == 0:
					#print('divisor', divisor)
					divisors.append(divisor)
					break
			else:
				#print('no divisors for base',base)
				break
		else:
			found.add(digits)
			sols.append((digits, divisors))

for d,s in sols:
	print(d, *s)