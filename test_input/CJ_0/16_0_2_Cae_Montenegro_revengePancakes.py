import numpy as np

def toBoolArray(input_str):
	arr = np.ones(len(input_str))
	for x in range(len(input_str)):
		arr[x] = input_str[x]=="+"
	return arr

def resolveProblem(problem):
	count = 0
	while np.sum(problem) < problem.size or np.sum(problem) == 0:
		it = 1
		condition = problem[0] == problem[it]
		while condition and it<problem.size:
			it += 1
		problem[:it] = np.logical_not(problem[:it][::-1])
		count += 1

	if np.sum(problem) == 0:
		count = 1
	return count

def solveProblem(problem):
	lastVal = -1
	count = 0
	if np.sum(problem) == problem.size:
		return count
	elif np.sum(problem) == 0:
		return 1

	for x in range(problem.size):
		if problem[x] != lastVal:
			count += 1
			lastVal = problem[x]
	if problem[-1]:
		count -= 1
	return count



f = open('B-large.in', 'r')
problems = f.read().splitlines()
problemList = []
for problem in problems[1:]:
	problemList.append(toBoolArray(problem))

outputFile = open("Output.txt", "w")
count=1
for pro in problemList:
	result = solveProblem(pro)
	outputFile.write("Case #"+str(count)+": "+str(result)+"\n")
	count+=1
outputFile.close()

