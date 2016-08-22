from math import sqrt, ceil
from itertools import islice, count

infile = open('coin.in', 'r')
outfile = open('coin.out', 'w')

T = int(infile.readline().strip())
N, J = map(int, infile.readline().strip().split(' '))

def findDiv(N):
	for i in [2,3,5,7]:
		if N % i == 0:
			return i
	start = 11
	stop = int(ceil(sqrt(N)))+1
	step = 6
	for i in islice(count(start, step), (stop-start+step-1+2*(step<0))//step):
		if N % i == 0:
			return i
		if N % (i+2) == 0:
			return i+2
	return N

outfile.write('Case #1:\n')

start = 2 ** (N/2-1) + 1
stop = 2 ** (N/2)
step = 1
for i in islice(count(start, step), (stop-start+step-1+2*(step<0))//step):
	if J < 1:
		break
	number = bin(i)[2:] + bin(i)[::-1][:-2]
	works = True
	ans = []
	for base in xrange(2, 10):
		tmp = int(number, base)
		div = findDiv(tmp)
		if div == tmp:
			works = False
			break
		else:
			ans.append(str(div))
	ans.append('11')
	if works:
		outfile.write(number + ' ' + ' '.join(ans) + '\n')
		J -= 1