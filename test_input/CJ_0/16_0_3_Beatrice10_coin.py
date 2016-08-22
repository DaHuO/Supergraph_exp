# 160409 by beatrice
import sys
import re

def base2(num):
	ret=[]
	i=1
	while num>=(2**i):
		i+=1
	i-=1
	
	while i>=0:
		ret.append(1)
		num-=(2**i)
		i-=1
		if num == 0:
			while i>= 0:
				ret.append(0)
				i-=1
			break;
		while num<(2**i):
			ret.append(0)
			i-=1
	return ret

def prime(num):
	num1 = int(num**0.1)
	for i in range(2,num1+1):
		if (num % i == 0):
			return i # is a composite
	num2 = int(num**0.3)
	for i in range(num1+1,num2+1):
		if (num % i == 0):
			return i # is a composite
	num3 = int(num**0.5)
	for i in range(num2+1,num3+1):
		if (num % i == 0):
			return i # is a composite
	return -1 # is a prime
	
def baseN(num):
	ret = []	
	for i in range(2,11):
		result=0
		for j in range(0,len(num)):
			if num[j] == 0:
				continue
			else:
				result += num[j] * (i**(len(num)-j-1))
		if prime(result) == -1:
			return []
		ret.append(result)		
	return ret

def list2int(list):
	ret = 0
	for i in range(0,len(list)):
		if list[i] == 0:
			continue
		else:
			ret += list[i] * 10**(len(list)-i-1)
	return ret

	
input = raw_input()
T = int(input)
result = []
for i in range(0, T):
	result.append([])
	input = raw_input()
	r = re.compile('[ \t\n\r:]+')
	input = r.split(input)
	N=int(input[0])
	J=int(input[1])
	MM = 2**(N-1)
	NN = 2**N
	for j in range(MM, NN+1):
		if j % 2 == 0:
			continue
		num = base2(j)
		numlist = baseN(num)
		if numlist == []:
			continue
		qualify = 1
		numlist2 = []
		for k in range(0, 9):
			p = prime(numlist[k])
			if p < 0:
				qualify = 0
				break;
			numlist2.append(p)
		if qualify == 1:
			numlist2.insert(0, list2int(num))
			result[i].append(numlist2)
		if len(result[i]) == J:
			break;
		
for i in range(0, T):
	print("Case #%d:" % (i+1))
	for j in range(0, len(result[i])):
		s = ''
		for k in range(0, len(result[i][j])):
			s += str(result[i][j][k])
			s += ' '
		print(s)

