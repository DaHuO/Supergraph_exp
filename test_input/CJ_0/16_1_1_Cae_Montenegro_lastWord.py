

def solve(problem):
	lastWord=problem[0]
	for letter in problem[1:]:
		if  lastWord[0]<=letter:
			lastWord = letter+lastWord
		else:
			lastWord += letter
	return lastWord

f = open('A-large.in', 'r')
#f = open('test.txt', 'r')
problems = f.read().splitlines()
problemList = []
solutions = []
for problem in problems[1:]:
	solutions.append(solve(problem))

outputFile = open("Output.txt", "w")
count=1
for sol in solutions:
	print(sol)
	outputFile.write("Case #"+str(count)+": "+ str(sol)+"\n")
	count += 1
outputFile.close()
