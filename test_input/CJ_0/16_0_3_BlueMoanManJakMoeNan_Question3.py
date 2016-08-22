import random
import math
import sympy

def get_divisor(val):
	val = int(val)
	for i in range(2, val/2):
		if(val % i == 0): return i

def get_primes(current_val):
	for i in range(2, 10):
		if sympy.isprime(current_val): return True
	return False

def get_bin_string(N):
	string = '1'
	for i in range(N-2):
		string += str(random.randint(0, 1))
	string += '1'
	if(not get_primes(int(string))):
		return string
	else:
		return get_bin_string(N)
	
def get_and_print_divisor(bin_string):
	outs = [bin_string]
	for i in range(2, 10):
		current_val = int(bin_string, i)
		divisor = get_divisor(current_val) 
		outs.append(divisor)
	print " ".join(str(v) for v in outs)

T = input()
for i in range(T):
	inputs = raw_input().split()
	N = int(inputs[0])
	J = int(inputs[1])

	bin_strings = []
	while len(bin_strings) < J:
		rand_binary_string = get_bin_string(N)
		if rand_binary_string not in bin_strings:
			bin_strings.append(rand_binary_string)

	print 'Case #{}:'.format('1')
	for bin_string in bin_strings:
		get_and_print_divisor(bin_string)
