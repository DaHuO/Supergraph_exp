import numpy as np

def findDivisor(number):
	sq = np.sqrt(number)
	for i in range(2, int(np.floor(sq))+1):
		if (number % i) == 0:
			return i
	return -1

def convert(seq, base):
	ret = 0
	l = len(seq)
	for i in range(l):
		if int(seq[l-1-i]) == 1:
			ret += (base**i)
	return ret

filename = 'C-small-attempt0'
with open(filename + '.in') as f_in:
	T = int(f_in.readline())
	N, J = f_in.readline().split(' ')
	N = int(N)
	J = int(J)

coins = []
divisors = []
i = 0
while (len(coins) < J) and (i < 2**(N-2)):
	seq = bin(i).split('b')[1]
	seq = '1' + '0'*(N-2-len(seq)) + seq + '1'

	d_temp = []
	for k in range(2, 11):
		num = convert(seq, k)
		d = findDivisor(num)
		if d == -1:
			break
		else:
			d_temp.append(d)

	if len(d_temp) == 9:
		coins.append(seq)
		divisors.append(d_temp)

	i = i + 1

with open(filename + '.out', 'w') as f_out:
	f_out.write('Case #' + str(T) + ':\n')
	for k in range(len(coins)):
		f_out.write(coins[k] + ' ')
		for j in divisors[k]:
			f_out.write(str(j) + ' ')
		f_out.write('\n')

