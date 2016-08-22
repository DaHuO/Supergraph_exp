def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

def jamcoin(length):
	start = 0
	length -= 2
	for i in range(2**length):
		yield '1' + bin(start)[2:].zfill(length) + '1'
		start += 1

prime_list = primes(2**25)
prime_set = set(prime_list)

def is_composite(n):
	return n not in prime_set

def find_divisor(n):
	for prime in prime_list:
		if n % prime == 0:
			return prime


T = input()
N, J = list(map(int, input().split()))
jamcoin_generator = jamcoin(N)

print("Case #1:")
while J > 0:
	number = next(jamcoin_generator)
	numbers = [int(number, base) for base in range(2, 11)]
	if all(is_composite(n) for n in numbers):
		divisors = list(map(find_divisor, numbers))
		if all(d is not None for d in divisors):
			print(number + ' ' + ' '.join(map(str, divisors)))
			J -= 1
