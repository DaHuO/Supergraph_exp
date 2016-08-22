import itertools
import os
import sys
from math import sqrt

bases = [2,3,4,5,6,7,8,9,10]
n_p_list = []
p_div_pair = {}
def tobase(n, base):
	l = "0123456789"
	o = ""
	while n != 0:
		o = l[n % base] + o
		n = n / base
	return o
	
def isPrime(n):
	if n < 2: return False
	for x in range(2, int(sqrt(n)) + 1):
		if n % x == 0:
			return False
	return True
	
def firstDivisor(n):
	for x in range(2,int(sqrt(n)) + 1):
		if (n % x == 0 and x != 1 and x != n):
			return x
	return -1
		
def generate(n):
	return ["".join(seq) for seq in itertools.product("01", repeat=n)]
	
def power(n, base):
	ret = 1
	for i in range(base):
		ret = ret * n
	return ret
	
def str_to_base(s):
	sum = 0
	idx = 0
	for i in bases:
		r = 0
		if (i == '1'):
			r = 1
		sum += r * power(i, idx)
		idx = idx + 1
	return sum
	
def can_convert(s):
	#print s
	p = []
	for j in bases:
		sum = 0
		idx = 0
		for i in s[::-1]:
			r = 0
			if i == '1':
				r = 1
			sum += r * power(j, idx)
			#print power(j,idx)
			idx = idx + 1
		if (isPrime(sum)):
			return False
		else:
			p.append(sum)
	divs = []
	for d in p:
		divs.append( firstDivisor(d) )
	p_div_pair[s] = divs
	return True
	
def d_find(l,limit):
	for c in l:
		#p = '1' + c + '1'
		if (c[0] == '1' and c[len(c) - 1] == '1'):
			if (can_convert(c)):
				n_p_list.append(c)
				limit = limit - 1
			if (limit == 0):
				break
				
					
				
		 

def process(n,j):
	l = generate(n)
	#print l
	d_find(l,j)
	
	
line = raw_input()
cases = 0
for i in range(int(line)):
	cases = cases + 1
	n,j = raw_input().split(" ")
	process(int(n), int(j))
	print 'Case #{}: '.format(cases)
	for k in p_div_pair:
		print k,
		for i in p_div_pair[k]:
			print i,
		print '\n'
	