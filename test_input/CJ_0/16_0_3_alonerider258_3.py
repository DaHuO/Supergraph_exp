import itertools
import math

prime = []

def generateJam (n):
	a = '1'
	jams = []

	for i in range(n - 1):
		a += '1'
		
	p = (2, n-2)

	lst = list(itertools.product([0, 1], repeat=n-2))
	
	k  = 0
	for i in lst:
		jams.append('1')
		for s in i:
			jams[k] += str(s)
		jams[k] += '1'

		k += 1

	return jams

def divisor(a):
	for i in range(1, int(math.sqrt(a) + 1) ):
		if a % i == 0 and i != 1 and i != a:
			return i
	return -1

def generatePrime(m, n):
	for num in range(m,n):
		if all(num%i!=0 for i in range(2,num)):
			prime.append(num)

def checkPrime(l):

	for n in l:
		if divisor(n) == -1:
			return False
	return True
			
		
def checkEnds(n):
	n = str(n)
	if (n[0] == 0 or n[-1] == 1):
		return False

	return True

def getBases(s):

	s = str(s)
	l = []

	for x in range(2, 11):
		l.append(int(s, x))

	return l

def main():

	f = open('input.txt', 'r')
	tc = int(f.readline())
	t = 0
	r = open('output.txt', 'w')

	while (tc > 0):
		t += 1
		k = "Case #" + str(t) + ':' '\n'

		jg = f.readline()
		jg = jg.partition(' ')

		j = int(jg[-1])
		jams = generateJam(int(jg[0]))

		print(j, int(jg[0]))

		i = 0

		while (j > 0):	

			print(j)
			num = int(jams[i]) 
			l = getBases(num)
			d = []

			if checkEnds(l) == False : 
				i += 1
				continue

			if checkPrime(l) == False:
				i += 1

				continue
			
			for n in l:
				d.append(divisor(n))
				
			k += str(num) + ' '

			for e in d:
				k += str(e) + ' '
				
			k += '\n'	

			i += 1
			j -= 1
		
		tc -= 1
		r.write(k)
main()
