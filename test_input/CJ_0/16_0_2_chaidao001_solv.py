def flip(pancakes, n):

	top = pancakes[:n]

	output = ""

	for pancake in top[::-1]:
		output += reverse(pancake)

	output += pancakes[n:]

	return output


def reverse(pancake):
	if pancake == "+":
		return "-"
	return "+"


def solve(pancakes):

	n = len(pancakes)
	outcome = "+" * n

	if pancakes == outcome:
		return 0

	states = [[] for i in range(n)]
	states[0] = [pancakes]

	pancakeType = list()

	for i in range(1, n + 1):
		state = states[i - 1]

		for p in state:

			for j in range(n):
				j += 1
				flipped = flip(p, j)

				if flipped == outcome:
					return i

				if flipped not in pancakeType:
					pancakeType.append(flipped)

					states[i].append(flipped)


input_file_name = "input.in"
output_file_name = "output.out"


with open(input_file_name, "r") as input:
	number_cases = int(input.readline())

	with open(output_file_name, "w") as output:

		for i in range(number_cases):

			result = solve(input.readline().strip())

			if result is None:
				print("NOOOOOOOO")
			else:
				output.write("Case #" + str(i + 1) + ": " + str(result) + "\n")

