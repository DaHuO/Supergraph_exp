import sys
import math

input_ = open("input")
output = open("output", 'w')

infile = input_.read().split('\n')

output.write("Case #1:\n")

jamsize, jamnum = infile[1].split()
coins = 0

binlen = int(jamsize) - 2
binnum = pow(2, binlen) - 1
inc = 0

while coins < int(jamnum):
	divisors = []
	failed = 0
	success = 0
	coin = bin(inc)[2:].rjust(binlen, '0')
	coin = "1" + coin + "1"

	for i in range(2, 11):
		base = int(coin, i)
		success = 0
		j = 2

		while j < 30:

			if(base % j == 0):
				success = 1
				divisors.append(j)
				break
			j = j + 1

		if(success == 0):
			failed = 1
			break

	if(failed == 0):
		coins = coins + 1
		output.write(coin)
		for d in divisors:
			output.write(" " + str(d))
		output.write("\n")

	inc = inc + 1
	sys.stdout.write(str(coins)+"\r")
	if(inc > binnum):
		print("uh oh")
		break

output.close()