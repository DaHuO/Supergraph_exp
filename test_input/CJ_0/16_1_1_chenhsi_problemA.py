def solve(instanceNumber):
	data = loadData(instanceNumber)
	outputFile = open('solutionA.txt', 'wb')

	t = int(data[0])
	for j in range(1, t + 1):
		outputFile.write('Case #' + str(j) + ': ' + solveSpecific(data[j].strip()) + '\n')

	outputFile.close()


def loadData(instanceNumber, problem = 'A'):
	fileName = problem + '-small-attempt' + str(instanceNumber) + '.in'
	if instanceNumber == -1:
		fileName = problem + '-large.in'
	with open(fileName, 'rb') as f:
		return [line for line in f]

def solveSpecific(s):
	if len(s) <= 1:
		return s
	highest = chr(max(map(ord, s)))
	split = s.split(highest)
	pre = highest * (len(split) - 1)
	post = ''.join(split[1:])
	return pre + solveSpecific(split[0]) + post
        
def check():
	with open('solutionA.txt', 'rb') as f:
		i = 0
		for line in f:
			print line[:-1]
			i += 1
			if i == 20:
				break
