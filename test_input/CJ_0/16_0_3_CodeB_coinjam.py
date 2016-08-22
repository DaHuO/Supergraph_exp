import fileinput
import numpy as np
from math import sqrt
from itertools import count, islice

def isPrime(n):
    if n < 2: return False
    for number in islice(count(2), int(sqrt(n)-1)):
        if not n%number:
            return False
    return True

def random_jamcoin(ln):
	res = np.random.randint(2, size=16)
	res[-1] = '1'
	res[0] = '1'
	return res.tolist()

def basearray(jamcoin):
	bases = [0] * 9
	i = 0
	j = 2
	stjc = ''.join(str(x) for x in jamcoin)
	while (j <= 10):
		bases[i] = int(stjc, j)
		i += 1
		j += 1
	return bases

def is_valid(jamcoin):
	bases = basearray(jamcoin)
	primes = [0] * 9
	i = 0
	while (i < 9):
		primes[i] = isPrime(bases[i])
		i += 1
	return not True in primes

def divs (numstr):
	num = int(numstr)
	list_divisor = []
	for i in [2,3,4,5,6,7,8,9] : 
	    z = 0
	    for index in range(len(str(num))) :
	        z += (i**(len(str(num))-index-1))*(int(str(num)[index]))       
	       
	    for j in range(1, int(z ** 0.5) + 1):
	        div, mod = divmod(z, j)
	        if mod == 0 and div != z and div != 1 :
	            list_divisor.append(div)
	            break   
	for k in range(1, int(num ** 0.5) + 1):
	    div, mod = divmod(num, k)
	    if mod == 0 and div != num and div != 1 :
	        list_divisor.append(div)
	        break  
	return " ".join(str(x) for x in list_divisor)

if __name__ == "__main__":
	i = 0
	for line in fileinput.input():
	    line = line.strip()
	    if i == 0:
	        testcases = int(line)
	    else:
	      numbers = map(int,line.split())
	      n = numbers[0]
	      j = numbers[1]
	      jamcoin_set = set()
	      while (len(jamcoin_set) < 50):
	      	jc = random_jamcoin(n)
	      	if(is_valid(jc)):
	      		jamcoin_set.add(''.join(str(x) for x in jc))
	      print ("Case #%d: " % i) 
	      for j in list(jamcoin_set):
	      	print j + " " + divs(j)	      
	    i += 1