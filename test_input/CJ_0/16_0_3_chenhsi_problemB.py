import os
os.chdir('C:\Users\chenhsi\Downloads')

def findJamcoins(n, j, outputFile):
	outputFile.write('Case #1:\n')
	i = int('1' + ('0' * (n - 2)) + '1', 2)
	numFound = 0
	while True:
		string = bin(i)[2:]
		result = []
		for k in range(2, 11):
			guess = int(string, k)
			factor = findFactor(guess)
#			print string, guess, k, factor
			if factor == None:
				break
			result.append(str(factor))
		if len(result) == 9:
			print string + ' ' + ' '.join(result)
			numFound += 1
			outputFile.write(string + ' ' + ' '.join(result) + '\n')
			if numFound == j:
				return
		i += 2

def findFactor(n):
	if n % 2 == 0:
		return 2
	for i in range(3, int(n ** 0.5 + 2)):
		if n % i == 0:
			return i
	return None
