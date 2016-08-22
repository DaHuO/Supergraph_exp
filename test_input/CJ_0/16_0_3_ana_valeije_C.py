import sys
from math import sqrt

global primes

class Base:
	def __init__(self, digits):
		self.n_digits = len(digits)
		self.digits = {}
		for i in xrange(len(digits)):
			self.digits[i] = digits[i]
			self.digits[digits[i]] = i

	# Receives a decimal number and converts it to the base represented in the object
	def toMyBase(self, n_dec):
		n_self = ''
		while n_dec > 0:
			n_self = self.digits[n_dec % self.n_digits] + n_self
			n_dec /= self.n_digits
		return n_self
	
	def toDecimal(self, n_self):
		n_dec = 0
		dec_counter = 1
		while n_self:
			last = n_self[-1]
			n_dec += self.digits[last] * dec_counter
			dec_counter *= self.n_digits
			n_self = n_self[0:len(n_self) - 1]
		return n_dec

def min_div(n):
	if n%2 == 0:
		return 2
	i = 3
	max_n = min(sqrt(n),10e5)
	while i <= max_n:
		if n % i == 0:
			return i
		i += 2
	return 1
	
	
def generate_jamcoins(N,J):
	global primes
	n = 0
	jamcoins_dict = {}
	bases_dict = {}
	dec_digits = '0123456789'
	for i in xrange(2,11):
		bases_dict[i] = Base(dec_digits[0:i])
	while len(jamcoins_dict) < J:
		print len(jamcoins_dict)
		b = bin(n)[2:]
		jamcoin = '1' + (N - 2 - len(b))*'0' + b + '1'
		jamcoins_dict[jamcoin] = []
		for i in xrange(2,11):
			number = bases_dict[i].toDecimal(jamcoin)
			if number not in primes:
				div = min_div(number)
				if div == 1:
					primes.add(number)
					jamcoins_dict.pop(jamcoin)
					break
				jamcoins_dict[jamcoin].append(div)
			else:
				jamcoins_dict.pop(jamcoin)
				break
		n += 1
	return jamcoins_dict
					
def solveCase(case, f, fout):
	N, J = f.readline().strip().split('\t')
	N = int(N)
	J = int(J)
	
	jamcoins_dict = generate_jamcoins(N,J)
	
	result = '\n'
	for jamcoin in jamcoins_dict:
		result += jamcoin + ' '
		for item in jamcoins_dict[jamcoin]:
			result += str(item) + ' '
		result += '\n'
	
	writeLine(fout, case, str(result))

def writeLine(fout, n, result):
	print("Case #%d: %s\n" %(n, result))
	fout.write("Case #%d: %s" %(n, result))

if __name__ == '__main__':
	
	inputFileName = sys.argv[1]
	
	global primes	
	
	primes = set()
	
	f = file(inputFileName)
	fout = file("%s.out" %(inputFileName.split(".")[0]), "w")
	
	T = eval(f.readline())
	
	for case in xrange(T):
		solveCase(case + 1, f, fout)
		
	f.close()
	fout.close()
