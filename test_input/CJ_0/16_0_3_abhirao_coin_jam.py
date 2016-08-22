primes = [2]
for i in range(3, 2**16):
	is_prime = True
	for p in primes:
		if i % p == 0:
			is_prime = False
			break
	if is_prime:
		primes.append(i)
	# print(i)
def base(N, target):
	N = N[::-1]
	p = 1
	result = 0
	for i in N:
		result += int(i) * p
		p *= target
	return result
def isprime(N):
	if N in primes:
		return True
	return False
T = int(input())
for i in range(T):
	N, J = input().split(" ")
	N, J = int(N), int(J)
	count = 0
	n = 0
	print("Case #"+str(i+1)+":")
	while count < J:
		startN = 2**(N - 1) + 1 + n
		isCoin = True
		baseNum = []
		startNBinary = bin(startN)[2:]
		# print(len(startNBinary))
		sol = []
		for b in range(2, 11):
			num = base(startNBinary, b) 
			if(isprime(num)):
				isCoin = False
				break
			baseNum.append(num)
		solFound = True
		if isCoin:
			sol.append(startNBinary)
			for num in baseNum:
				index = 0
				while index < len(primes) and num%primes[index] != 0:
					index+=1
					# print(num, index)
				if index == len(primes):
					solFound = False
					break
				sol.append(str(primes[index]))

			if solFound:
				print(' '.join(sol))
				count += 1
		n+=2
