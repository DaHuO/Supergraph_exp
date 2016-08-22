def solve(inputString):
	previousLetter = "z"
	outputString = ""
	counter = 0
	for letter in inputString:
		if (counter == 0):
			outputString = letter

		else:
			tempString = ""
			tempString+=previousLetter
			tempString+=letter
			tempString+=str(outputString[0])
			tempString = sorted(tempString)
			print (tempString)
			print("\n")
			if (tempString[2] != letter):
				outputString+=letter

			else:
				outputString = letter+outputString

		print (outputString)

		previousLetter = letter

		counter+= 1

	return outputString

def main():
	outputFile = open("output.txt", "w")
	inputFile = open("input.in")

	line = inputFile.read().splitlines()
	for i in range(1, len(line)):
		answer = solve(str(line[i]))
		outputFile.write("Case #" + str(i) + ": " + str(answer) + "\n")

	
	outputFile.close()
	inputFile.close()



main()
