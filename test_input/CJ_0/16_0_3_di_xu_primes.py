
primes = set()    

def eratosthenes(upper):
	D = {}  # map composite integers to primes witnessing their compositeness
	q = 2   # first integer to test for primality
	while q < upper:
		if q not in D:
			primes.add(q)        # not marked composite, must be prime
			D[q*q] = [q]   # first multiple of q not already marked
		else:
			for p in D[q]: # move each witness to its next multiple
				D.setdefault(p+q,[]).append(p)
			del D[q]       # no longer need D[q], free memory
		q += 1

eratosthenes(1000)

def divisible(num):
    if num in primes: 
        return [False,0]
    for divisor in primes:
        if num % divisor == 0:
            return [True,divisor]
    return [False,0]

def process(l,n):
    lower = int("1"+"0"*(l-2)+"1",2)
    upper = int("1"*l,2)
    res = []
    count = 0
    while count < n and lower <= upper:
        rep = bin(lower)[2:]
        line = rep
        for base in range(2,11):
            converted = int(rep,base)
            flag,div = divisible(converted)
            if not flag:
                break
            line += " "+str(div)
            if base == 10:
                res.append(line)
                count += 1
        lower += 2
    return res

def verify(nums):
    for line in nums:
        temp = line.split(" ")
        val = temp[0]
        d = temp[1:]
        d = map(int,d)
        for base in range(2,11):
            numerator = int(val,base)
            if numerator % d[base-2] !=0:
                print "ERROR"
    
                
import sys
fin = sys.stdin
cases = int(fin.readline())
for case in range(1,1+cases):
    print "Case #1:"
    length,n = map(int,fin.readline().split(" "))
    ans = process(length,n)
    #verify(ans)
    for i in range(n):
        print ans[i]
