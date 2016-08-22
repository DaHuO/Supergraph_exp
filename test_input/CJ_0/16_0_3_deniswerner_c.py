from itertools import product
from math import ceil, sqrt

def description():
	print """
	Input

		The first line of the input gives the number of test cases, T. 
		T test cases follow; each consists of one line with two integers N and J.
	Output

		For each test case, output J+1 lines. 
		The first line must consist of only 
		Case #x:, 
		where x is the test case number (starting from 1). 

		Each of the last J lines must consist of a jamcoin of length N followed by nine integers. 
		The i-th of those nine integers (counting starting from 1) 
		must be a nontrivial divisor of the jamcoin when the jamcoin is interpreted in base i+1.

		All of these jamcoins must be different. 
		You cannot submit the same jamcoin in two different lines, even if you use a different set of divisors each time.
	
	Limits
		T = 1. (There will be only one test case.)
		It is guaranteed that at least J distinct jamcoins of length N exist. 
"""


def solve(n,j):

	jc = 0
	solutions = []

	for xm in product('01', repeat=(n-2)):
		if jc == j:
			break
		x = "1" + "".join(xm) + "1"
		no_prime = True
		divisors = []
		for base in range(2,11):
			xb = int(x,base)
			
			# better get the factors instantly
			divisor = is_prime(xb)
			if divisor == 0:
				no_prime = False
				break
			else:
				divisors.append(str(divisor))
		if no_prime:
			jc += 1
			solutions.append(x + " " + " ".join(divisors))


	return solutions

def is_prime(a):
	if (a%2) == 0:
		return 2
	sqrt_a = int(ceil(sqrt(a)))
	for i in range(3,sqrt_a + 1,2):
		if (a%i) == 0:
			return i
	return 0

filename = "C-small-attempt2"

with open(filename + ".in","r") as f:
	content = f.read().splitlines()

no_of_cases = int(content[0])


outputs = []
for c in content[1:]:
	n,j = c.split(" ")
	result = solve(int(n),int(j))
	outputs.append(result)

with open("" + filename +".out","w") as f:
	for o in range(len(outputs)):
		f.write("Case #"+ str(o+1) + ": " + "\n")
		for  oi in outputs[o]:
			print oi
			f.write(oi + "\n")
