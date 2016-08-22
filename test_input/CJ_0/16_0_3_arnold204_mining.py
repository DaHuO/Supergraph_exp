import math
import itertools

def is_composite(n):
    if n % 2 == 0: 
        return True, 2
    for i in range(3, int(math.ceil(math.sqrt(n))), 2):
        if n % i == 0:
            return True, i
    return False, None

def is_legit(seq):
	bases = [2, 3, 4, 5, 6, 7, 8, 9, 10]
	acc = []
	for base in bases:
		is_valid, divisor = is_composite(int(seq, base))
		if is_valid:
			acc.append(str(divisor))
		else:
			return False, None
	return True, acc

def mine_coins(l, n):
	'''
	l for  bit length
	n numbers of coins to mine
	'''
	counter = 0
	coins = {}
	permute_l = l - 2
	for ran_seq in ["".join(seq) for seq in itertools.product("01", repeat=permute_l)]:
		if counter == n:
			break
		coin = '1' + ran_seq + '1'
		it_is, divs = is_legit(coin)
		if it_is:
			counter += 1
			print '{} {}'.format(coin, ' '.join(divs))


mine_coins(16, 50)