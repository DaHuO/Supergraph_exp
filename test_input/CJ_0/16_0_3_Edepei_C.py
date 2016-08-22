import math

def jamcoins2(num_digits, j):

	# define bases 2-10 inclusive
	bases = list(range(2,11))

	# Calculate maximum and minimum value for jamcoins in each base
	min_jamcoin = '1' + '0'*(num_digits-2) +'1'
	max_jamcoin = '1' + '1'*(num_digits-2) +'1'

	base_mins = [int(min_jamcoin, b) for b in bases]
	base_maxs = [int(max_jamcoin, b) for b in bases]

	# print base_mins
	# print base_maxs

	# Any proposed jamcoin cannot be a prime in any of the defined bases.
	# Find prime numbers between each range.
	primes = []
	for min_val, max_val in zip(base_mins, base_maxs):
		primes.extend(find_primes(min_val, max_val))


	# blacklist those numbers in each base
	# clean up the blacklist for non-jamcoin compliant formats
	blacklisted = [baseN(p,b) for b in bases for p in primes]
	blacklisted = filter(check_jamcoin(num_digits), blacklisted)
	# print 'blacklisted: ', blacklisted

	# Start creating non-blacklisted jamcoins and find factors for each base
	# Use base 2 since it is the most similar to jamcoin.
	candidates = [baseN(n, 2) for n in xrange(int(min_jamcoin, 2), int(max_jamcoin, 2)+1) if baseN(n,2) not in blacklisted]
	# print 'candidates: ', candidates
	c2 = filter(check_jamcoin(num_digits), candidates)
	# print 'candidates: ', c2

	# For J candidates, find a factor in each base.
	for i in xrange(j):
		# candidate in jamcoin
		candidate = candidates[i]

		# find corresponding numbers in each base,
		# then find nontrivial factors
		base_numbers = [int(candidate, b) for b in bases]
		factors = map(find_factor, base_numbers)

		print '{} {}'.format(candidate, ' '.join(map(str,factors)))


def jamcoins(num_digits, j):

	num_examples = 0

	# define bases 2-10 inclusive
	bases = list(range(2,11))

	# Calculate maximum and minimum value for jamcoins in each base
	min_jamcoin = '1' + '0'*(num_digits-2) +'1'
	max_jamcoin = '1' + '1'*(num_digits-2) +'1'

	for n in xrange(int(min_jamcoin, 2), int(max_jamcoin, 2)+1):
		candidate = baseN(n,2)

		# Check if candidate is of a valid coinjam form
		if not check_jamcoin(num_digits)(candidate):
			continue
		
		# find corresponding numbers in each base,
		# then find nontrivial factors
		base_numbers = [int(candidate, b) for b in bases]
		factors = map(find_factor, base_numbers)
		
		# If no factor could be found in a reasonable time, skip
		if None in factors:
			continue

		print '{} {}'.format(candidate, ' '.join(map(str,factors)))
		num_examples += 1

		if num_examples >= j:
			break



def find_factor(x):
	# Finds the first nontrivial factor for a number.
	# Returns None is no nontrivial factor is found.
	
	i = 2
	while True:
		if i > math.sqrt(x)+1:
			return None

		if i > 1000:
			return None

		if x % i == 0:
			return i

		i += 1
		
	return None


def check_jamcoin(n):
	def jamcoin_compliant(x):
		# Checks if a proposed jamcoin x:
		# begins with a 1 and ends with 1
		# has n length.
		digits = [d for d in str(x)]
		
		# Has n length
		if len(digits) != n:
			return False

		# Begins with 1 and ends with 1
		if not (digits[0] == '1' and digits[-1] == '1'):
			return False

		# Contains only 0s and 1s
		for i in digits:
			if not (i == '0' or i == '1'):
				return False
		return True
	return jamcoin_compliant


def find_primes(a, b):
	# Finds primes between a and b.

	def is_prime(x):
		# Checks if a number is prime
		if x < 1:
			return False

		for i in xrange(2,x):
			if x % i == 0:
				return False

		return True

	primes = []
	for n in xrange(a, b+1):
		if is_prime(n):
			primes.append(n)
	return primes

def baseN(num, b, numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
	# from stackoverflow
	return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])


if __name__ == '__main__':

	num_test_cases = int(raw_input())

	for i in xrange(1, num_test_cases+1):
		(n, j) = map(int, raw_input().split())

		print 'Case #{}:'.format(i)
		jamcoins(n, j)