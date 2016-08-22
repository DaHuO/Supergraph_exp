
def getMinimumFlips(stack):
	currentChar = stack[0]
	flips = 0
	for char in stack:
		if currentChar != char:
			currentChar = char
			flips += 1
	if currentChar == '-':
		flips += 1
	return flips

def main():
	inputFile = open('B-large.in', 'r')
	outputFile = open('pancakeOutput.txt', 'w')
	testCases = int(inputFile.readline().strip())
	for i in range(testCases):
		stack = inputFile.readline().strip()
		minimumFlips = getMinimumFlips(stack)
		outputFile.write('Case #' + str(i + 1) + ': ' + str(minimumFlips) + '\n')

main()