from math import sqrt

__author__ = "Enric Florit <efz1005@gmail.com>"

def base_interpret(binary, base):
	output = 0
	base_factor = 1

	for i in xrange(len(binary) - 1, -1, -1):
		output += int(binary[i]) * base_factor
		base_factor *= base

	return output

def get_divisor(number):
	for i in xrange(2, int(sqrt(number)) + 1):
		if number % i == 0:
			return i
	return 1

# feed T. We don't need to save it, as it will always be 1
raw_input()

data = raw_input()
data = data.split(' ')

length = int(data[0])
num_jamcoins = int(data[1])

coins = []

min_value = 2 ** (length - 1) + 1
max_value = 2 ** length - 1

j = min_value

while min_value <= j <= max_value and len(coins) < num_jamcoins:
	binary = str(bin(j))[2:]
	divisors = []

	base = 2
	prime = False
	while base <= 10 and not prime:
		d = get_divisor(base_interpret(binary, base))
		if d > 1:
			divisors.append(str(d)) # convert to str to do a .join() later
		else:
			prime = True
		base += 1

	if not prime:
		coins.append([binary, divisors])
	j += 2

print "Case #1:"

for i in xrange(len(coins)):
	print coins[i][0], " ".join(coins[i][1])