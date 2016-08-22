def getPrimeDiv(n, primes):
	for p in primes:
		if n % p == 0:
			return p
	return None

def isNotPrimeInAnyBase(b, primes):
	for i in xrange(2, 11):
		nInBase = int(b, i)
		if getPrimeDiv(nInBase, primes) == None:
			return False
	return True

def printNumberAndDivisors(b, primes):
	print "%s" % (b),
	# print "%s" % (int(b,2)),
	for i in xrange(2, 11):
		nInBase = int(b, i)
		div = getPrimeDiv(nInBase, primes)
		# print "%d / %d = %d, " % (nInBase, div, nInBase/div),
		print "%d" % (div),
	print

def main():
	primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]

	for TEST in xrange(1, int(raw_input())+1):
		N, J = map(int, raw_input().split())

		print "Case #%d:" % (TEST)

		found = 0

		n = (1<<(N-1))+1
		limit = (1<<N)-1
		while n <= limit:
			b = bin(n)[2:]
			if isNotPrimeInAnyBase(b, primes):
				printNumberAndDivisors(b, primes)
				found += 1
				if found >= J:
					break
			n += 2

main()
