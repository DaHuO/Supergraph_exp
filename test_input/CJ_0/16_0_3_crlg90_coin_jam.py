def change_base(arr, base):
	r = reversed(arr)
	total = 0
	for i, val in enumerate(r):
		total += val * pow(base,i)
	return total

def next_permutation(length):
	initial = None
	for p in permutation(length-2):
		yield [1] + p + [1]

def permutation(length):
	for prefix in xrange(2):
		if length == 1:
			yield [prefix]
		else:
			for p in permutation(length - 1):
				yield [prefix] + p

def primes_up_to(top):
	primes = [2]
	for i in xrange(3, top, 2):
		isPrime = True
		for prime in primes:
			if i % prime == 0:
				isPrime = False
				break
			if prime * prime >= i:
				break;
		if isPrime:
			primes.append(i)
	return primes

t = int(raw_input())
for case in xrange(1, t+1):
	number, jamcoins = map(int, raw_input().split())
	# constants to play
	top = 100000
	first_primes = primes_up_to(top)
	js = []
	for p in next_permutation(number):
		divisors = []
		for base in xrange(2,11):
			currNum = change_base(p, base)
			for divisorCandidate in first_primes:
				if currNum % divisorCandidate == 0:
					divisors.append(divisorCandidate)
					break
				if divisorCandidate * divisorCandidate > currNum:
					break
		if len(divisors) == 9:
			js.append((''.join([str(i) for i in p]), divisors))
			if len(js) == jamcoins: break

	print "Case #{}:".format(case)
	for cad, divisors in js:
		print cad , ' '.join(map(str,divisors))
	 
