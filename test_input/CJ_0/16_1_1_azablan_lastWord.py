import sys

def findLast(s):
	finished = []
	buildWord(list(s), [], finished)
	finished.sort()
	return finished[-1]

def buildWord(s, current, finished):
	if not s:
		finished.append(''.join(current))
		return
	newS = s[:]
	l = newS.pop(0)
	before = current[:]
	before.insert(0, l)
	after = current[:]
	after.append(l)
	buildWord(newS, before, finished)
	buildWord(newS, after, finished)

with open(sys.argv[2]) as inf:
	lines = inf.readlines()
	lines = [l.strip('\n') for l in lines]

outName = sys.argv[1] + "Output.txt"
ouf = open(outName, 'w')
for i in range(1, int(lines[0]) + 1):
	ouf.write("Case" + " #" + str(i) + ": " + str(findLast(lines[i])) + "\n")