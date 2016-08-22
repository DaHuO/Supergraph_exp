import sys

# Check if input n is prime. If it is, return 0, otherwise return a divisor.
def getDivisor(n):
	if n == 1: return 1
	if n == 2 or n == 3: return 0
	if (n % 2) == 0: return 2
	if n < 9: return 0
	if n%3 == 0: return 3
	r = int(n**0.5)
	f = 5
	while f <= r:
		if (n % f) == 0: return f
		if (n % (f + 2)) == 0: return (f + 2)
		f += 6
	return 0  


# Read data file into a list
lines = []
with open(sys.argv[1], "r", encoding="utf-8") as data_file:
	for line in data_file:
		lines.append(line.rstrip('\n'))


# Get total number of test cases
test_cases = int(lines[0])
del lines[0]


# Process each test case
case = 0
for line in lines:
	case += 1
	print("Case #" + str(case) + ":")

	# Get input numbers
	input = [x for x in line.split(" ")]
	jamcoin_length = int(input[0])
	num_jamcoins = int(input[1])

	jamcoin_counter = 0

	# Maximum binary number that can be represented with (jamcoin_length - 2) digits (remove bookends)
	max_interior = int("1" * (jamcoin_length - 2), 2)

	# Count from 0 to max_interior
	# With each, convert to binary then add bookend 1's to obtain candidate jamcoin
	for i in range(0, max_interior + 1):
		interior_padded_binary = bin(i)[2:].zfill(jamcoin_length - 2)
		jamcoin_candidate = "1" + interior_padded_binary + "1"

		# List of divisors to output
		divisors = []

		# Convert candidate jamcoin to number in each of base 2-10
		for base in range(2, 11):
			converted_number = int(jamcoin_candidate, base)

			# If resulting number is prime, move on to another jamcoin candidate
			result = getDivisor(converted_number)
			if result == 0:
				break

			# Otherwise, add resulting divisor to the list and then try the next base 
			else:
				divisors.append(result)

		# If we have divisors for all 9 bases, increment counter and output result
		if len(divisors) == 9:
			jamcoin_counter += 1
			output = jamcoin_candidate + " "
			output += " ".join(map(str, divisors))
			print(jamcoin_candidate + " " + " ".join(map(str, divisors)))


		# If we have enough jamcoins, test case is over, move on to next
		if jamcoin_counter == num_jamcoins:
			break







	# Output