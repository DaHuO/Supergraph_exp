# -*- coding: utf-8 -*-

import pdb

primes = set()

def solve(length, count):
	coins = []
	proofs = []
	num_str = '1' + '0' * (length - 2) + '1'
	while len(coins) < count:
		proof = find_proof(num_str)
		if proof != None:
			coins.append(num_str)
			proofs.append(proof)
		num_str = bin(int(num_str, 2) + 2)[2:]
	return coins, proofs

def find_proof(num_str):
	proof = []
	for base in range(2, 11):
		num = int(num_str, base)
		divisor = find_divisor(num)
		if divisor == None:
			return None
		else:
			proof.append(divisor)
	return proof

def find_divisor(num):
	assert(primes != set())
	max_divisor = int(num ** 0.5)
	for divisor in primes:
		if num % divisor == 0:
			return divisor
		if divisor > max_divisor:
			return None



def main():
	# pdb.set_trace()

	# input_file = 'D-large.in.txt'
	output_file = 'out'
	# output_format = 'Case #{0}: {1}\n'

	results = []

	global primes
	with open('prime_list.txt', 'r') as f:
		primes = tuple(int(x) for x in f)

	length = 32
	count = 500
	coins, proofs = solve(length, count)
	# with open(input_file, 'r') as f:
	# 	case_total = str_to_int(f.readline())
	# 	# for each case:
	# 	for i in range(case_total):
	# 		X, R, C = str_to_int_list(f.readline())
	# 		if could_win(X, R, C):
	# 			results.append('RICHARD')
	# 		else:
	# 			results.append('GABRIEL')
			
	with open(output_file, 'w') as f:
		f.write('Case #1:\n')
		for i in range(len(coins)):
			# for each result
			f.write('{0} {1}\n'.format(coins[i], ' '.join([str(x) for x in proofs[i]])))	


# --------------------------------------------

def str_to_int(s):
	return int(s.strip())

def str_to_int_list(s):
	return [int(x) for x in s.strip().split()]

if __name__ == '__main__':
	main()



