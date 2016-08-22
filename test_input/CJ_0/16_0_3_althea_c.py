from sys import stdin
import random 
import string 

def interpret(string, base):
	number = 0
	for i in xrange(smallL, 0, -1):
		if int(string[smallL-i])==1:
			number += base **(i-1)
	return number

def checknonprime(num):
	if num > 1:
	   # check for factors
	   for i in range(2,10000):
		   if (num % i) == 0:
			   return i
	   else:
		   return 0
	
small = '1000000000000001'
smallL=16
large = '100000000000000000000000000000001'
largeL=32
N=50
coins = set([])
print 'Case #1:'
while (len(coins)<50):
	mutated = '1'
	for i in range(1, 15):
		if random.randint(0,1):
			mutated= ''.join((mutated,'1'))
		else:
			mutated= ''.join((mutated,'0'))
	mutated= ''.join((mutated,'1'))
	result = mutated
	broken = 0
	for i in range(2, 11):
		N = interpret(mutated, i)
		if (checknonprime(N)):
		  result = ' '.join((result, str(checknonprime(N))))
		else: 
			broken = 1
	if ((broken ==0) and (mutated not in coins)):
		coins.add(mutated)
		print result