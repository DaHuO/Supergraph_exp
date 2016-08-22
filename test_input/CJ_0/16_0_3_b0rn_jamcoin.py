#!/usr/bin/python3.4

import math
import itertools

def is_prime(n):
    	if n % 2 == 0 and n > 2: 
        	return False
    	return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def base2Dec(number,base):
	res = 0
	l = len(number)-1
	for i in range(0,l+1):
		res += int(number[i])*pow(base,l-i)
	return res
	
def testJamcoin(jamcoin):
	dividers = []
	for k in range(2,11):
		r = base2Dec(jamcoin,k)
		if is_prime(r):
			return dividers
			
		for a in range(2,r):
			if r%a == 0:
				dividers.append(str(a))
				break
	return dividers

with open("input.in","r") as file:
	with open("output.out","w") as out:
		i = 0
		for line in file:
			if i != 0:
				n = int((line.split())[0])
				j = int((line.split())[1])		
				
				jamcoins = []
				dividers = []

				possibleJamcoins = list(itertools.product('01',repeat=n-2))
				for jamcoin in possibleJamcoins:
					x = '1'+(''.join(jamcoin))+'1'
					d = testJamcoin(x)					
					if len(d) == 9:
						jamcoins.append(x)
						dividers.append(d)
					possibleJamcoins.remove(jamcoin)
					
					if len(jamcoins) == j:
						break
				
					
				
				sent = "Case #"+str(i)+":\n"
				for m in range(0,len(jamcoins)):
					sent += jamcoins[m]+" "+' '.join(dividers[m])+"\n"
				print(sent)
				out.write(sent)
				
			i+=1
