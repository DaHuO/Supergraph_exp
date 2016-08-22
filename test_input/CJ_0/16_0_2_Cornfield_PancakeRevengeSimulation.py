def solve(inputList):

	numberOfTimesFlipped = 0
	allFaceUp = False

	if ("-" not in inputList):
		return str(0)

	elif ("+" not in inputList):
		return str(1)

	while(allFaceUp == False):
		if ("-" not in inputList):
			allFaceUp = True

		else:
			inputList = sort(inputList)
			numberOfTimesFlipped += 1

	return str(numberOfTimesFlipped)





def sort(inputList):
	tempCounter = 0
	tempInputList = [""]*len(inputList)
	numberPancakesToFlip = 0

	i = 0
	if (inputList[0] == "-"):
		if (inputList[i] != "+"):
			numberPancakesToFlip += 1

	elif (inputList[0] == "+"):
		if (inputList[i] != "-"):
			numberPancakesToFlip += 1


	if (inputList[0] == "+"):
		for i in range (0, len(inputList)):
			if (inputList[i] == "-"):
				break
			elif (inputList[i] == "+" and i != 0):
				numberPancakesToFlip += 1


	elif (inputList[0] == "-"):
		for i in range (0, len(inputList)):
			if (inputList[i] == "+"):
				break
			elif (inputList[i] == "-" and i != 0):
				numberPancakesToFlip += 1



	if (inputList[0] == "+"):
		for j in range(0, numberPancakesToFlip):
			tempInputList[j] = "-"

	elif (inputList[0] == "-"):
		for j in range(0, numberPancakesToFlip):
			tempInputList[j] = "+"

	for k in range(numberPancakesToFlip, len(inputList)):
		tempInputList[k] = inputList[k]

	inputList = tempInputList

	return inputList



def main():
	outputFile = open("output.txt", "w")
	inputFile = open("input.in")
	inputList = []

	line = inputFile.read().splitlines()
	for i in range(1, len(line)):
		inputList = list(line[i])
		answer = solve(inputList)
		outputFile.write("Case #" + str(i) + ": " + answer + "\n")

	
	outputFile.close()
	inputFile.close()



main()