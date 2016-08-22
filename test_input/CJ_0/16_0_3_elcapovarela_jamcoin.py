new_file = open("jamcoinLargeSol", "w")

primes = [2,   3,   5,   7,  11,  13,  17,  19,  23,  29,  31,  37,  41,
  43,  47,  53,  59,  61,  67,  71,  73,  79,  83,  89,  97, 101,
 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239,
 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467,
 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569,
 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643,
 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733,
 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823,
 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911,
 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

import random
def generate_random_strings(n, J):
	list_randoms = []
	random_string = [1]
	for i in range(n):
		current = random_string[:]
		for j in range(J-2):
			current.append(random.randint(0,1))
		current.append(1)
		if current not in list_randoms:
			list_randoms.append(current)
	return list_randoms

def get_numbers_given_jamcoin(jamcoin):
	jamcoin_copy = jamcoin[:]
	# print jamcoin
	jamcoin_copy.reverse()
	# print jamcoin_copy
	numbers = []
	for i in range(2,11):
		current_number = 0
		for power in range(0,len(jamcoin_copy)):
			if int(jamcoin_copy[power]) == 1:
				current_number += i**power
		numbers.append(current_number)
	return numbers

# print list(str(1001011000110101))
# print get_numbers_given_jamcoin(list(str(1010110001101001)))
def numbers_not_prime(numbers):
	divisors = []
	for number in numbers:
		for prime in primes:
			if number % prime == 0:
				divisors.append(prime)
				break
	if len(divisors) == len(numbers):
		return divisors
	else:
		return None
# print numbers_not_prime(get_numbers_given_jamcoin(list(str(1001011000110101))))


def get_jamcoin(n,J):
	possible_jamcoins = generate_random_strings(n,J)
	# print possible_jamcoins
	jamcoins = {}
	possible_jamcoins_to_numbers = {}
	for possible_jc in possible_jamcoins:
		# print possible_jc
		numbers_given_jamcoin = get_numbers_given_jamcoin(possible_jc)
		# print possible_jc
		string_jamcoin = ''.join([str(i) for i in possible_jc])
		# print string_jamcoin
		possible_jamcoins_to_numbers[string_jamcoin] = numbers_given_jamcoin
	for jamcoin in possible_jamcoins_to_numbers.keys():
		divisors = numbers_not_prime(possible_jamcoins_to_numbers[jamcoin])
		if divisors != None:
			jamcoins[jamcoin] = divisors
	# print jamcoins
	return jamcoins
# 
good_jamcoins = get_jamcoin(2000,32)

if len(good_jamcoins) >= 500:
	new_file.write("Case #"+str(1)+ ":"+"\n")
	good_jamcoins_keys = good_jamcoins.keys()
	for i in range(1,501):
		joined_divisors = " ".join([str(x) for x in good_jamcoins[good_jamcoins_keys[i-1]]])
		string_jamcoin_divisors = good_jamcoins_keys[i-1]+" "+joined_divisors
		new_file.write(string_jamcoin_divisors+"\n")





