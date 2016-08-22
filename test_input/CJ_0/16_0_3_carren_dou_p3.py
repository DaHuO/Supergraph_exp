import random

def jamcoin(N, J):
	strings = {}
	while len(strings.keys())<J:
		string = generate(N)
		if not strings.has_key(''.join(string)):
			interp = interpret(string)
			is_prime, divisor = zip(*[check_prime(inp) for inp in interp])
			if all(s == False for s in is_prime):
				strings[''.join(string)] = divisor
	return strings
			
def check_prime(num):
	if not num & 1:
		return False, 2
	is_prime = True
	for t in xrange(3, int(num**0.5)+1,2):
		if num % t == 0:
			is_prime = False
			break
	return is_prime, t

def generate(N):
	string = ['1']
	string = string + [str(random.randint(0,1)) for tmp in xrange(N-2)]
	string.append('1')
	return string

def interpret(string):
	interpretation = []
	for base in xrange(2,11):
		acc = 0
		for i,s in enumerate(string[::-1]):
			acc = acc + int(s)*(base**i)
		interpretation.append(acc)
	return interpretation


f_output = open('C-small-attempt0.out','w')
f_output.writelines('Case #1:\n')
with open('C-small-attempt0.in','r') as f:
	t = int(f.readline())
	N, J = [int(s) for s in f.readline().split(' ')]
	output = jamcoin(N,J)
	for string, divisor in output.items():
  		f_output.writelines('{}'.format(string))
  		for d in divisor:
  			f_output.writelines(' {}'.format(d))
  		f_output.writelines('\n')
f_output.close()




