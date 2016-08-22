import sys
import math

def primes(n): 
	if n==2: return [2]
	elif n<2: return []
	s=range(3,n+1,2)
	mroot = n ** 0.5
	half=(n+1)/2-1
	i=0
	m=3
	while m <= mroot:
		if s[i]:
			j=(m*m-3)/2
			s[j]=0
			while j<half:
				s[j]=0
				j+=m
		i=i+1
		m=2*i+3
	return [2]+[x for x in s if x]



def readFile(fname):
	data = []
	with open(fname, 'r') as f:
		N = int(f.readline())
		print N
		for i in range(N):
			(N, J) = f.readline().split()
			N = int(N); J = int(J)
			data.append((N, J))
	return data


def process(data, primes):
	out = []
	for N, J in data:
		for mid in range(2**(N-8)):
			start = '1' + format(mid, '#0'+str(N)+'b')[2:] + '1'
			temp = [start]
			
			for base in range(2, 11):
				num = int(start, base)
				#print num
				for p in primes:
					if p >= num:
						break
					elif num % p == 0:
						temp.append(str(p))
						break
			if len(temp) == 10:
				out.append(temp)
			if len(out) == J:
				break
	return out

def output(fname, out):
	with open(fname, 'w') as f:
		f.write('Case #1:\n')
		for r in out:
			#print r
			f.write(' '.join(r) + '\n')

if __name__ == '__main__':
	p = primes(10000)
	data = readFile(sys.argv[1])
	out = process(data, p)
	output(sys.argv[2], out)