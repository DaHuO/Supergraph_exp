import itertools
import math
from itertools import count, islice

def is_prime(a):
    return all(a % i for i in xrange(2, a))

#from math import sqrt; from itertools import count, islice

def isPrime(n):
    #return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
    if n<2:
    	return False

    for i in range(2,int(n**0.5)+1):
    	if n%1==0:
    		return False

    return True

def convert(b,r):
	i=0
	number=0
	t=len(b)-1
	while t>=0:
		number+=b[t]*(r**i)
		i+=1
		t-=1
	return number

def factors(x):
   #print("The factors of",x,"are:")
   for i in range(2, int(x*0.5) + 1):
       if x % i == 0:
           #print i
           return i

def factors1(n):    
    x= sorted(list(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0)))))
    #print x
    return x[1]

def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, 100):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

for i in range(input()):
	n,j=map(int,raw_input().split())
	#a=[1]*n
	count=0
	print "Case #"+str(i+1)+":"
	#li = []
	#nos=[]
	#while count<j:
	for i in itertools.product([0,1], repeat=n-2):
	    x='1'+''.join(map(str, i))+'1'
	    #print "x: ",x
	    flag=0
	    facs=[]
	    d=map(int,x)
	    for q in xrange(2,11):
			e=convert(d,q)
			if len(list(divisorGenerator(e)))<3:
				flag=0
				break
			else:
				flag=1
				facs.append(list(divisorGenerator(e))[1])
	    

	    if flag==1 and count<j:
		       	count+=1
			print x,
			for y in facs:
				print y,
			print ""

	    if count==j:
			break

	    
			

	


