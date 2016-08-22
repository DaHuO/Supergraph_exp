count = 0
need = 50

def isprime(number):
	k = int(number**(0.5)+1)
	if number == 2:
		return False
	if number%2 == 0:
		return 2
	for i in range(3, k+1, 2):
		if number%i == 0:
			return i
	return False

def base(n, b):
	return sum([int(str(n)[i])*b**(len(str(n))-i-1) for i in range(len(str(n)))])

for r1 in range(32769, 65536, 2):
	x = int(bin(r1)[2:])
	bools = str(x)
	c = True
	for q in range(2, 11):
		num = base(x, q)
		if isprime(num) == False:
			c = False
			break
		bools += " "+str(isprime(num))
	if c:
		print bools
		count += 1
		if count == need:
			break