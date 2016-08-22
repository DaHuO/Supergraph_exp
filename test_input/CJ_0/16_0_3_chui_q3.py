primes = {}
prime_list = []

class num(object):
	
	def __init__(self,len):
		self.len = len
		self.n = [0] * len
		self.n[0] = 1
		self.n[-1] = 1
		self.factors = []
	
	def plus(self):
		carry = 1
		for i in range(2,self.len+1):
			if carry == 0:
				return
			d = self.n[self.len - i] + carry
			carry = 0
			if d == 2:
				d = 0
				carry = 1
			self.n[self.len - i] = d
		if carry == 1:
			self.n.insert(0,carry)
			self.len += 1

	def toto(self, base = 10):
		s = 0
		for nn in self.n:
			s = s * base + nn
		return s

	def toString(self):
		return str(self.n)

	def iscoin(self):
		factors = []
		for i in range(2,11):
			ispri , factor = isprime(self.toto(i))
			if ispri:
				return False
			factors.append(factor)
		self.factors = factors
		return True 


def isprime(num):
	h = int(num**0.5)
	if num in primes:
		return (True, 0)
	for p in prime_list:
		if p > h:
			return (True, 0)
		if num % p == 0:
			return (False, p)
	return (True, 0)

def solving(line):
	N,J = line.split(' ')
	n = num(int(N))
	ret = []
	while True:
		if n.len > int(N) or len(ret) == int(J):
			break
		if n.iscoin():
			ret.append(str(n.toto())+ ' ' + ' '.join(map(str,n.factors)))
		n.plus()
	return ret

for i in range(2,2**16):
	ispri, f = isprime(i)
	if ispri:
		primes[i] = True
		prime_list.append(i)

with open('input', 'r') as input:
	count = 0
	for line in input:
		if count == 0:
			count+=1
			continue
		print 'Case #%d:\n%s' % (count, ' \n'.join(solving(line)))
		count+=1

# n = num(6)

# while True:
# 	if n.len > 6:
# 		break
# 	if n.iscoin():
# 		print n.toString()
# 	n.plus()

	