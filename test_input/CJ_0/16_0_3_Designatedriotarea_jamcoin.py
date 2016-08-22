import sys
def main():
	print "Case #1:"
	length = 16
	solutions = 50
	successes = 0
	upper_limit = (2**length)-1
	perm = 2**(length-1) + 1
	#n = int(raw_input("number"))
	while perm <= upper_limit + 1 and successes < solutions:
		factors = []
		for base in range(2,11):
			n = bin(perm)[2:]
			n = int(n, base)
			prime_check = isprime(n)
			if prime_check != True:
				factors += [prime_check]
			else: 
				break
		if len(factors) == 9:
			print bin(perm)[2:], 
			print ' '.join(map(str, factors))
			successes += 1
		perm += 2
			
				
				

def isprime(n):
	if n % 2 != 0:
		clock = 3
		while clock **2 <= n:
			if n % clock == 0:
				return clock
			clock += 2
		return True
	else:
		return 2
if __name__ == "__main__": main()
