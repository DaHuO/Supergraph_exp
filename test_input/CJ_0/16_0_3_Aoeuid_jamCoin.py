import sys
from math import pow, sqrt

inFile = sys.argv[1]



def getMin(numDigits):
	return pow(2, int(numDigits) - 1) + 1

divDict = {}

def getDiviser(n):
	if n in divDict:
		return divDict[n]
	if n % 2 == 0:
		divDict[n] = 2
		return 2
	d = 3
	while n % d != 0:
		d = d + 2
		if (d >= sqrt(n)):
			divDict[n] = -1
			return -1
	divDict[n] = d
	return d

def getSolution(pair):
	numTested = 0
	length = pair.split(' ')[0]
	numToGenerate = pair.split(' ')[1]

	possibleSolAsInt = int(getMin(length))
	numSolsFound = 0
	sol = ""

	while (1 == 1):
		solAsString = "{0:b}".format(possibleSolAsInt)
		# print(solAsString + "\n")
		allPass = True
		thisSol = solAsString + " "
		for i in range(2,11):
			diviser = getDiviser(int(solAsString, i))
			if diviser is -1:
				# print(">>>" + str(diviser) + " " + solAsString + " " + str(i))
				allPass = False
				break
			else:
				thisSol = thisSol + str(diviser) + " "
		if (allPass is True):
			numSolsFound = numSolsFound + 1
			sol = sol + thisSol[:-1] + "\n"
			print thisSol[:-1]
			if numSolsFound >= int(numToGenerate):
				return sol
		possibleSolAsInt = possibleSolAsInt + 2
		numTested = numTested + 1


with open (sys.argv[1], 'r') as myInput:
	with open ("output.txt", 'w') as myOutput:
		for idx, line in enumerate(myInput):
			if (idx == 0):
				continue;
			sol = getSolution(line[:-1])
			
			myOutput.write("Case #" + str(idx) + ":\n" + str(sol) + "\n")
