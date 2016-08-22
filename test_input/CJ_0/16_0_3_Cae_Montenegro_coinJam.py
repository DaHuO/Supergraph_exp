
import math

def toIntTuple(str_input):
	split = str_input.split(" ")
	return (split[0],split[1])


zero = "{0:b}".format(0)
one = "{0:b}".format(1)
bases = range(2,11)


def getDivisor(number, divisorsInBases):
	found = False
	divisor = 2
	while not found and divisor < math.sqrt(number):
		if number % divisor == 0 and divisor not in divisorsInBases:
			return divisor
		divisor += 1
	return -1

def solveProblem(N, J):
	solutionsBinaries = []
	solutionsValues = []
	actualVal=int(math.pow(2,N-1)+1)
	binary="{0:b}".format(actualVal)
	while len(solutionsBinaries) < J:
		divisorsInBases = []
		for base in bases:
			divisor = getDivisor(int(binary,base), divisorsInBases)
			if divisor > 0:
				divisorsInBases.append(divisor)
		if len(divisorsInBases) == len(bases):
			solutionsBinaries.append(binary)
			solutionsValues.append(divisorsInBases)
		actualVal += 2
		binary="{0:b}".format(actualVal)
	return (solutionsBinaries, solutionsValues)


'''
def solveProblem(N, J):
	solutionsBinaries = []
	solutionsValues = []
	actualVal=int(math.pow(2,N-1))
	binary="{0:b}".format(actualVal)
	while len(solutionsBinaries) < J:
		divisorsInBases = []
		for base in bases:
			divisorsInBases.append(int(binary[:-1],base))
		if binary not in solutionsBinaries:
			solutionsBinaries.append(binary)
			solutionsValues.append(divisorsInBases)
		actualVal += 2
		binary="{0:b}".format(actualVal)
	return (solutionsBinaries, solutionsValues)
'''

#f = open('C-small-attempt0.in', 'r')
f = open('C-small-attempt1.in', 'r')
problems = f.read().splitlines()
problemList = []
for problem in problems[1:]:
	problemList.append(toIntTuple(problem))

outputFile = open("Output.txt", "w")
count=1
for pro in problemList:
	result = solveProblem(int(pro[0]), int(pro[1]))
	outputFile.write("Case #"+str(count)+":"+"\n")

	for it, sol in enumerate(result[0]):
		out = str(sol)
		for element in result[1][it]:
			sol += " "+str(element)
		outputFile.write(str(sol)+"\n")
		print(sol)
	count+=1
outputFile.close()
