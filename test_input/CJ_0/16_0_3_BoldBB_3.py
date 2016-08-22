def toBase(num, base):
	return sum(base**i * int(digit) for i, digit in enumerate(reversed(list(str(num)))))

primesnum = {}

def isPrimeNum(num):
	if num <= 1:
		return (False, 1)
	if primesnum.get(num, None) != None:
		return primesnum.get(num)
	i = 2
	while i < int(num**0.5 + 1):
		if num % i == 0:
			primesnum[num] = (False, i)
			return primesnum[num]
		i += 1
	primesnum[num] = (True,)
	return (True,)

def isJamcoin(coin):
	if(len(coin) > 0 and coin[0] == "0" or coin[-1] == "0"):
		return (False,)
	divs = list()
	for i in range(2, 11):
		isprime = isPrimeNum(toBase(coin, i))
		if isprime[0]:
			return (False,)
		else:
			divs.append(isprime[1])
	return (True, divs) 

print "Case #1:"

seen = list()

n, j = 32, 500
start = 2**(n-1)
conststart = 2**(n-1) + 1
endbefore = 2**n
i = 1
while j > 0 and start < endbefore:
	for x in range(1, n-3):
		for y in range(x+1, n-2, 2):
			for z in range(y+1, n-3, 2):
				for a in range(z+1, n-4, 2):
					start = conststart + 2**x + 2**y + 2**z + 2**a
					coin = "{0:b}".format(start)
					if coin in seen:
						continue
					seen.append(coin)
					jamcoin = isJamcoin(coin)
					if jamcoin[0]:
						print "{0:b}".format(start), " ".join(str(s) for s in jamcoin[1])
						j -= 1
					if j == 0:
						exit()