import math
import sys

def binaryStr(n):
	s=bin(n)[2:]
	#print str(n)+" --> "+str(s)
	return s

def is_prime(n):
	if n==2 or n==3: return True
	if n%2==0 or n<2: return False
	for i in range(3,int(n**0.5)+1,2):   # only odd numbers
		if n%i==0:
			return False    
	return True
    #return all(a % i for i in xrange(2, int(math.sqrt(a))))

def CheckPrimeBases(s):
	for base in range(2,11):
		a=long(s,base)
		if is_prime(a):
			return False
			break

	return True

def largest_prime_factor(n):
	i = 2
	while i * i <= n:
		if n % i:
			i += 1
		else:
			n //= i
	return n

def findDivisors(s):
	
	divisors=[]
	for base in range(2,11):
		k=long(s,base)
		divisors.append(largest_prime_factor(k))
		#for i in range(2,(k/2)+1):
		#	if k % i==0:
				#print str(base)+" ^^^^^ "+str(i)
		#		divisors.append(i)
		#		break

	#print len(divisors)
	return divisors


def process(n,j):

	counter=0
	for i in range(int(math.pow(2,n-1)),int(math.pow(2,n))):
		if i % 2==1:
			s=binaryStr(i)
			#print str(i)+" :: "+s
			if CheckPrimeBases(s):
				#print "now we need to find divisors"
				divs=findDivisors(s)
				#print str(int(s, 2))+"  ",
				#print str(i)+" :: "+s+" --->"	+str(int(s, 2))+" &&&&& "+str(is_prime(i))+" ###### "+str(divs)
				sys.stdout.write(s+" ")
				for d in divs:
					sys.stdout.write(str(d)+" ")
				sys.stdout.write("\n")
				#+" --->"	+str(int(s, 2))+" &&&&& "+str(is_prime(i))+" ###### "+str(divs)
				counter+=1
			if counter==j:
				return

		#print i,


	#print "hello "+str(n)+" *** "+str(j)



def main():
	index=0
	with open("C-small-attempt1.in", "r") as ins:
		numOfTestCases=int(ins.readline())
		#print "#cases "+str(numOfTestCases)
		

		cases=[]
		for i in range(numOfTestCases):
			inp=ins.readline().rstrip().split()
			n=int(inp[0])
			j=int(inp[1])
			
			# Case #1: 2 3
			print "Case #"+str(i+1)+": "
			process(n,j)
			
			#break



main()