import sys
import math

def nextString(s, pos, length):
	if pos < length - 1: 
		if s[pos] == 0 :
			s[pos] = 1
		else :
			s[pos] = 0
			nextString(s, pos+1 , length)

def isPrime(p):
	sroot = math.sqrt(p)
	for i in range(2, int(sroot) + 1):
		if p % i == 0:
			#composite
			d = i
			return (0,d)
	return (1,0) #prime

def isCompositeforall(s, length, divs) :
	for i in range(2, 11):
		number = 0
		for j in range(length) :
			number = number + s[j] * (i**j)
		(v,d) = isPrime(number)
		if v :
			return 0 # the number is prime
		else :
			divs[i-2] = d
	return 1

print "Case #1:"
j = 50
s= [x * 0 for x in range(16)]
s[0] = 1
s[15]=1
while j!=0 :
	divisors = [x * 0 for x in range(9)]
	if isCompositeforall(s, 16, divisors) :
		s.reverse()
		for i in range(16):
			sys.stdout.write(str(s[i]))
		s.reverse()
		for i in range(9):
			sys.stdout.write(" " + str(divisors[i]))
		print
		nextString(s, 1,16)
		j = j-1
	else :
		nextString(s,1,16)

