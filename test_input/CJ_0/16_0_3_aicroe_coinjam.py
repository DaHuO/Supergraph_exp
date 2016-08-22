
firstDivisors = dict()

def getFirstDivisor(num):
	divisor = 2
	if num in firstDivisors:
		return firstDivisors[num]
	else:
		while divisor < num**(0.5):
			if num % divisor == 0:
				firstDivisors[num] = divisor
				return divisor
			divisor += 1
		firstDivisors[num] = None
		return None

def convertToDec(vnum, base):
	num = 0
	power = base**(len(vnum) - 1)
	for n in vnum:
		num += n * power
		power /= base
	return num

def generateDivisors(vnum):
	divisors = list()
	for base in xrange(2, 11):
		divisor = getFirstDivisor(convertToDec(vnum, base))
		if divisor == None:
			return None
		divisors.append(divisor)
	return divisors

def containsCoin(coin, coins):
	for (x, _) in coins:
		if coin == x:
			return True
	return False

def containsNone(vector):
	for v in vector:
		if v == None:
			return True
	return False

def generateCoins(coin, N, i, coins, J):
	if len(coins) == J:
		return
	if i >= N - 1:
		if not containsCoin(coin, coins):# and not containsNone(coin):
			divisors = generateDivisors(coin)
			if divisors != None:
				coins.append((list(coin), divisors))
	else:
		for n in [0, 1]:
			coin[i] = n
			for j in xrange(i, N):
				generateCoins(coin, N, j + 1, coins, J)
		#coin[i] = None

def generateCoinJams(N, J):
	startCoin = [None for i in xrange(N)]
	startCoin[0] = 1
	startCoin[N - 1] = 1
	coins = list()
	generateCoins(startCoin, N, 1, coins, J)
	return coins

T = int(raw_input())
for i in xrange(1, T + 1):
	line = raw_input().split(' ')
	N = int(line[0])
	J = int(line[1])
	coins = generateCoinJams(N, J)
	print 'Case #{}: '.format(i)
	for (coin, divisors) in coins:
		print convertToDec(coin, 10), \
				'{} {} {} {} {} {} {} {} {}'.format(*divisors)
		
	


