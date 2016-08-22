import sys
import math

inputFileName = ""
lines = []
outputFileName = ""

def parse_args():
	global inputFileName

	if len(sys.argv) == 2:
		inputFileName = sys.argv[1]
	else:
		raise ValueError('Incorrect number of arguments (%i) found.' % len(sys.argv))

def parse_file():
	global inputFileName
	global lines

	file = open(inputFileName)

	first = True
	numOfLines = 0

	for line in file:
		if first:
			numOfLines = int(line)
			first = False
		else:
			lines.append(line.strip())

	if len(lines) != numOfLines:
		raise ValueError('Incorrect number of lines (%i) found, when expected %i' % (len(lines), numOfLines))

def writeToFile():
	global outputFileName

	if inputFileName[len(inputFileName) - 3:] == '.in':
		outputFileName = inputFileName[0:len(inputFileName) - 3] + '.out'
	else:
		outputFileName = inputFileName + '.out'

	outputFile = open(outputFileName, 'w')

	for i in range(len(lines)):
		numbers = lines[i]
		words = numbers.split()
		jamCoinLength = int(words[0])
		numOfJamCoins = int(words[1])

		try:
			outputFile.write('Case #%i:' % (i + 1))
			outputFile.write('\n')

			numberOfSubmissions = 0

			for j in range(2 ** (jamCoinLength - 1) + 1, 2 ** jamCoinLength):
				if numberOfSubmissions < numOfJamCoins:
					toCheck = bin(j)[2:]

					if toCheck[len(toCheck) - 1:] == '0':
						continue

					toAdd = checkIndividual(toCheck)

					if toAdd == False:
						continue
					else:
						outputFile.write(str(toCheck) + toAdd)
						outputFile.write('\n')

						numberOfSubmissions = numberOfSubmissions + 1
		except:
			raise ValueError('The line %s is not an int' % i)

	outputFile.close()

def checkIndividual(number):
	toReturn = ""

	for base in range(2, 11):
		numberConverted = convertFromBase(number, base)
		factor = checkIfPrime(numberConverted)

		if factor == 0:
			return False
		else:
			toReturn = toReturn + ' ' + str(factor)

	return toReturn

def convertFromBase(number, base):
	numberToString = str(number)

	lengthOfNumber = len(numberToString)

	finalNumber = 0

	for ch in numberToString:
		finalNumber = finalNumber + int(ch) * (base ** (lengthOfNumber - 1))
		lengthOfNumber = lengthOfNumber - 1

	return finalNumber

def checkIfPrime(number):
	isPrime = True

	factor = 0

	for i in range(2, int(math.sqrt(number)) + 1):
		if number % i == 0:
			isPrime = False
			factor = i
			break

	if isPrime:
		return 0
	else:
		return factor

def main():
	parse_args()
	parse_file()

	checkIndividual(10101)

	writeToFile()

if __name__ == '__main__':
	main()

