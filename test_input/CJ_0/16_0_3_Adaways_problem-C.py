import math

with open('C-small-attempt0.in') as f:
	lines = f.read().splitlines()
	nj = lines[1].split(' ')
	f.close()

N = int(nj[0])
J = int(nj[1])

N_Num = filter(lambda n : len(n) == N and n[0] == '1' and n[-1:] == '1', [bin(n)[2:] for n in range(2**(N))])

def isPrime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3 , int(math.sqrt(n)) + 1 , 2))

def divisor(n):
    for i in xrange(2,int(math.sqrt(n)) + 1):
        if n%i == 0 : 
        	return i
        	break

with open('output.txt','wb') as output:
	print >> output, 'case #1:'
	j = 0
	for n in N_Num:
		l = ([(int(n,i),i) for i in range(2,11) if not isPrime(int(n,i))])
		if len(l) == 9:
			print >> output, ' '.join([n]+map(lambda a: str(divisor(a[0])) ,l))
			j=j+1
		if j == J: break
	output.close()
