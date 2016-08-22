from sys import argv

#stolen from stack overflow
def get_primes(n):
	correction = (n%6>1)
	n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
	sieve = [True] * (n/3)
	sieve[0] = False
	for i in xrange(int(n**0.5)/3+1):
		if sieve[i]:
			k=3*i+1|1
			sieve[((k*k)/3)::2*k]=[False]*((n/6-(k*k)/6-1)/k+1)
			sieve[(k*k+4*k-2*k*(i&1))/3::2*k]=[False]*((n/6-(k*k+4*k-2*k*(i&1))/6-1)/k+1)
	return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]

def inclusive(num):
	return num+1

def exclusive(num):
	return num
	
primelist = get_primes(333)

with open(argv[1], 'r') as of:
	cases = int(of.next())
	for i, x in enumerate(of):
		inp = x.strip().split()
		n = int(inp[0])
		j = int(inp[1])
		
		print('Case #' + str(1) + ':')
		
		coins = []
		coin = [1] + [0 for _ in range(n-2)] + [1]
		
		while len(coins) < j:
			notcoin = False
			tested = [''.join(str(x) for x in coin)]
			flip_coin = list(reversed(coin))
			for base in range(2, inclusive(10)):
				b10 = 0
				for i, bit in enumerate(flip_coin):
					b10 += bit * (base**i)
				if b10 in primelist:
					notcoin = True
					break
				else:
					divisible = False
					for prime in primelist:
						if b10 % prime == 0 and base % prime != 0:
							divisible = True
							tested.append(str(prime))
							break
					if not divisible:
						notcoin = True
						break
			if notcoin:
				pass
			else:
				coins.append(tested)
			co = 0
			for i, bit in enumerate(flip_coin):
				if i == len(flip_coin)-1 or i == 0:
					continue
				if co == 1 or i == 1:
					if flip_coin[i] == 0:
						flip_coin[i] = 1
						co = 0
					else:
						flip_coin[i] = 0
						co = 1
			coin = list(reversed(flip_coin))
		for found in coins:
			print(' '.join(found))