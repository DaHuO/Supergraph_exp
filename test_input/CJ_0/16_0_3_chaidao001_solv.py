def findDivisor(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    return None
	


def solve(digits, number):

	lower = int("0b1" + "0" * (digits - 2) + "1", 2)
	upper = int("0b" + "1"*digits, 2) + 1

	output = []
	primeDict = dict()

	for i in range(lower, upper, 2):
		n = bin(i)[2:]

		b = 2
		divisors = []
		notPrime = True

		while notPrime and b <= 10:
			value = int(n, b)

			if value not in primeDict:
				divisor = findDivisor(value)
				primeDict[value] = divisor
			else:
				divisor = primeDict[value]
				print(123)

			divisors.append(divisor)
			notPrime = (divisor != None)
			b += 1

		if notPrime:
			output.append([bin(i)[2:], divisors])

		if len(output) == number:
			return output



input_file_name = "input.in"
output_file_name = "output.out"


with open(input_file_name, "r") as input:
	number_cases = int(input.readline())

	with open(output_file_name, "w") as output:

		for i in range(number_cases):

			line = input.readline().split()

			result = solve(int(line[0]), int(line[1]))

			if result is None:
				print("NOOOOOOOO")
			else:
				output.write("Case #" + str(i + 1) + ":" + "\n")
				for j in range(int(line[1])):
					output.write(result[j][0] + " " + " ".join(str(k) for k in result[j][1]) + "\n")

