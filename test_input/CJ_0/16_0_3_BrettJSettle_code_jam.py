lines = open('A-small-attempt0.in', 'r').readlines()
cases = int(lines[0])
if cases < 1 or cases > 100:
	print("Cases out of range")
	exit(0)

s = ''

def convert(s, base, power=0):
	val = int(s[-1]) * (base ** power)
	return val if len(s) == 1 else val + convert(s[:-1], base, power+1)

def primes1(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

primes = primes1(2 ** 20)

def isPrime(num):
	return [i for i in primes if num % i == 0 and i != num]

for case in range(1, cases+1):
	s += "Case #%s:\n" % case
	N, J = [int(i) for i in lines[case].split()]
	coins = []
	for coin in range(1 + (2 ** (N-1)), eval('0b' + '1' * N)+1, 2):
		coin = bin(coin)[2:]
		nums = []
		for base in range(2, 11):
			num = convert(coin, base)
			div = isPrime(num)
			if len(div) == 0:
				break
			nums.append(div[-1])
		if len(nums) == 9:
			coins.append(coin)
			s += "%s %s\n" % (coin, ' '.join(map(str, nums)))
		if len(coins) == J:
			break
open("out.txt", "w").write(s)


