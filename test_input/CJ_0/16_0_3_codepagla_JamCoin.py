from random import randint as RI
from math import sqrt
RANGE=1000000
ROOT_RANGE=1000

least_factor=[0 for i in xrange(RANGE+1)]   # actually least prime factors

#compute least factor for numbers upto RANGE

def sieve() :
	for i in xrange(2,ROOT_RANGE+1) :
		if not least_factor[i] :
			for j in xrange(i*i,RANGE+1,i) :
				least_factor[j]=i

sieve()    #gives correct result


# test primality for numbers greater than RANGE

def isPrime(n) : # tested
	if n!=1 :
		for t in xrange(3) :
			rNum=RI(1,n-1)
			if pow(rNum,n-1,n)!=1 :
				return False
		return True
	else :
		return False


# return the least factor for numbers greater than RANGE

def getLeastFactor(n) :   # tested  # actually least prime factors
	for i in xrange(2,int(sqrt(n))+1) :
		if not n%i :
			return i

#for small input

T=int(input())
N,J=map(int,raw_input().split())

LIMIT=16383   # 2^14-1

cnt=1

N-=2  # first and last digits are '1'
num=0

def jamcoin(num_bin,factors) :
	for base in xrange(2,11) :
		num=int(num_bin,base)
#		print "num in base", base, " =",num
		if num <= RANGE :
			if not least_factor[num] :
				return False
			else :
				factors.append(least_factor[num])
		else :
			if isPrime(num) :
				return False
			else :
				factors.append(getLeastFactor(num))
	return True
print "Case #1:"
while cnt <= J :
	num_bin=bin(num)[2:]
	l=len(num_bin)
	num_bin='1'+'0'*(N-l)+num_bin+'1'  # tested
	factors=[]
	if jamcoin(num_bin,factors) :
		print num_bin,
		for f in factors :
			print f,
		print
		cnt+=1
	num+=1
'''factors=[]
jamcoin("100011",factors)
for f in factors :
	print f,
print'''



