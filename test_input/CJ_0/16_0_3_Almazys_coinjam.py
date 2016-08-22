#!/bin/env python3

import sys
import os
from math import sqrt; from itertools import count, islice

def isprime(n):
	return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def doChallenge(_input_filename):
	try:
		with open(_input_filename, 'r') as f:
			lines = f.read().split('\n')
	except FileNotFoundError:
		print("Input file '" + _input_filename + "' not found !")
		sys.exit()
	except PermissionError:
		print("Input file '" + _input_filename + "' could not be read !")
		sys.exit()
	except Exception:
		print("Unknown shit has happened")
		sys.exit()

	del lines[0] # First line is useless
	for i in range(len(list(filter(None, lines)))):
		length = lines[i].split(' ')[0]
		amount = lines[i].split(' ')[1]

		found = 0
		print("Case #" + str(i+1) + ":")
		for j in range(100000000):
			_ = format(j, 'b')

			#Adds padding to make the correct length
			while len(_) < int(length)-2:
				_ = "0" + _

			if len(format(j, 'b')) >= int(length)-1:
				break
			_ = "1" + _ + "1"

			#check the bases
			is_prime = False
			for k in range(2, 11):
				if isprime(int(str(_), k)):
					is_prime = True
					break

			if is_prime == True:
				continue

			found = found +1

			#calculates nontrivial divisors
			factors = []
			for k in range(2, 11):
				for l in range(2, int(str(_), k)):
					if not int(str(_), k) % l:
						factors = factors + [str(l)]
						break

			print(_ + ' ' + ' '.join(factors))
			if found == int(amount):
				break



if __name__ == '__main__':
	try:
		sys.argv[1]
	except IndexError:
		print("Usage : " + sys.argv[0] + " filename")
	else:
		doChallenge(sys.argv[1])
