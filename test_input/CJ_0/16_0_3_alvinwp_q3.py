from math import *

def is_prime(n):
	for i in xrange(2, int(ceil(sqrt(n)))):
		if n % i == 0:
			return (i, False)
	return (-1, True)


inp = map(lambda x: x.strip(), open("C-small-attempt0.in", "r").readlines()[1:])
n, j = map(int, inp[0].split())
start = 0
jamcoins = {} 
while len(jamcoins) != j:
	num = "1" + bin(start)[2:].zfill(n-2) + "1"

	divisor = []
	for base in xrange(2, 11):
		v = is_prime(int(num, base))
		if not v[1]:
			divisor.append(v[0])
		else:
			break
	if len(divisor) == 9:
		jamcoins[str(num)] = divisor

	start += 1

out = open("output3.out", "w")
out.write("Case #1:")
for jamcoin in jamcoins:
	out.write("\n")
	out.write(jamcoin + " " + " ".join(map(str, jamcoins[jamcoin])))
out.close()