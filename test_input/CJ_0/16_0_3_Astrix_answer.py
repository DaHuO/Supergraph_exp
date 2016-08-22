from itertools import product
from math import sqrt, ceil

def no_primes(list_of_numbers):
	divisors = []
	for number in list_of_numbers:
		if number % 2 == 0:
			divisors.append(2)
		else:
			divisor = is_prime(number)
			if divisor == True:
				return False
			else:
				divisors.append(divisor)

	return divisors

def is_prime(number):
	for x in range(2, ceil(sqrt(number))):
		if number % x == 0:
			return x

	return True

def base_x_values(number):
	bases = []

	for x in range(2, 11):
		bases.append(int(str(number), x))

	return bases

def write_answer(correct_jamcoin):
	with open('cout.txt', 'w') as cout:
		cout.write("Case #1:\n")
		for jamcoin in correct_jamcoin:
			cout.write(' '.join(str(i) for i in jamcoin)+"\n")

if __name__ == "__main__":
	with open('test.txt', 'r') as doc:

		correct_jamcoin = []
		cases = int(doc.readline())
		length, jamcoins = doc.readline().rstrip().split()

	for jamcoin in product(['0','1'], repeat=(int(length)-2)):
		jamcoin = '1'+''.join(i for i in jamcoin)+'1'
		bases = base_x_values(jamcoin)

		divisors = no_primes(bases)
		if divisors:
			divisors.insert(0, jamcoin)
			correct_jamcoin.append(divisors)
			if len(correct_jamcoin) == int(jamcoins):
				break

	write_answer(correct_jamcoin)

