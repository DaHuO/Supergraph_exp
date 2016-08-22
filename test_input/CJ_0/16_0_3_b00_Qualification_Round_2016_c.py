#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Qualification_Round_2016_c.py
#
#  Copyright 2016 nerio
#
#

import fileinput

def create_jamcoin(N, start = ''):
	
	if not start:
		num = '1' + (N - 2) * '0' + '1'
		if not is_prime(num):
			return num
		else:
			num = create_jamcoin(N, num)
			return num
	else:
		num = str(bin(int(start, base = 2) + 2)[2:])
		if not is_prime(num):
			return num
		else:
			num = create_jamcoin(N, num)
			return num

def is_prime(num):
	#print('-------------------')
	# Calc. and check number for all bases
	for b in range(2, 10 + 1):
		b10_num = int(num, base = b)
		#print(b, b10_num)
		# If it isn't a prime number,
		# then there will be more than 2 divisors
		prime = True
		for j in range(2, b10_num):
			# workaround for faster search of proper codejam
			if j == 200000:
				break
			elif (b10_num % j) == 0:
				prime = False
				break
		
		if prime:
			#print('-------------------')
			return True
	
	#print('-------------------')
	return False

def find_divisors(jamcoin):
	
	divisors = []
	
	for b in range(2, 10 + 1):
		b10_num = int(jamcoin, base = b)
		
		for j in range(2, b10_num):
			if (b10_num % j) == 0:
				divisors.append(str(j))
				break
		
	return divisors

def main():

	curr_t_case = 1
	first_line = True
	for line in fileinput.input():
		line = line.strip()
		
		if first_line:
			t_cases = int(line)
			first_line = False
			continue
		
		N, J = list(map(int, line.split(' ')))
		print('Case #', curr_t_case, ': ', sep='')
		j = 1
		while j <= J:
			if j == 1:
				jamcoin = create_jamcoin(N)
			else:
				jamcoin = create_jamcoin(N, jamcoin)
			
			divisors = find_divisors(jamcoin)
			divisors = ''.join([' {0}'.format(d) for d in divisors]).strip()
			print(jamcoin, ' ', divisors, sep='')
			j += 1
		
		curr_t_case += 1

	return 0

if __name__ == '__main__':
	main()
