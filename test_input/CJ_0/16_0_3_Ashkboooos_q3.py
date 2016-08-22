from math import sqrt
def eratosthenes(limit):
    lst = range(2, limit)
    for i in range(2, int(sqrt(limit)) + 1):
        lst = filter(lambda x: x == i or x % i, lst)  # sieve
    return lst
all_primes = eratosthenes(65540)
def divisorGenerator(n):
	#for i in xrange(2,n/2+1):
	for i in all_primes:
		if i > n/2+1:
			break	
		if n%i == 0: 
			return i
def main():
	file_name = 'q3.in'
	f = open(file_name , 'r')
	lines = f.read().splitlines()
	test_cases = int(lines[0])
	result = ''
	#for i in xrange(1, test_cases + 1):
	line = lines[1]
	sp = line.split()
	N, total_j = int(sp[0]), int(sp[1])
	j = 0
	r = 'Case #1:'
	#for i in xrange(32769, 65535):
	#for i in xrange(32769, 32772):
	for i in xrange(int('1' + '0'* (N-2) + '1' , 2), int('1'*N, 2)+1 ):
		if i %2 == 0:
			continue
		s = "{0:b}".format(i)
		in_bases = [ int(s,b) for b in xrange(2,11) ]
		if any(x in all_primes for x in in_bases):
			continue
		#the number is not prime in any bases, now find the first devisor
		r += s +' '
		for b in in_bases:
			div = divisorGenerator(b)
			r += str(div) + ' '
		r = r[:-1]
		r += '\n'
		j += 1
		if j == total_j:
			break
	result = r
	print result
	f = open('q3.out', 'w')
	f.write(result)
	f.close()
if __name__ == '__main__':
	main()
