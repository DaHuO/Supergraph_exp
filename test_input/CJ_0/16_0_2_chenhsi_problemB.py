def solve(strFileInput, strFileOutput):
	fileInput = open(strFileInput, 'rb')
	fileOutput = open(strFileOutput, 'wb')
	t = int(fileInput.readline())
	for i in range(t):
		a = fileInput.readline().strip()
		b = int(''.join(['1' if c == '-' else '0' for c in a[::-1]]), 2)
		r = bfs(b)
		print a, b, r
		fileOutput.write('Case #' + str(i + 1) + ': ' + str(r) + '\n')
	fileInput.close()
	fileOutput.close()

def solveSingle(strInput):
	b = int(''.join(['1' if c == '-' else '0' for c in strInput[::-1]]), 2)
	r = bfs(b)
	print strInput, b, r
	return r

memo = dict()
memo[0] = 0
currentStack = []
def recursive(n):
	if n in memo:
		return memo[n]
	currentStack.append(n)
	
	best = None
	for next in getNextPossible(n):
		if next in currentStack:
			continue
		recur = recursive(next)
		if best is None or recur is not None and recur < best:
			best = recur
	if best is not None:
		best += 1

	shouldSet = True
	for next in getNextPossible(n):
		if next not in memo:
			shouldSet = False
	if shouldSet:
		memo[n] = best
	currentStack.pop()
	return best

def getNextPossible(n):
	possible = []
	s = bin(n)[2:]
	i = 1
	while i <= len(s):
		r = s[:-i]
		m = s[-i:]
		d = ''.join(['1' if c == '0' else '0' for c in m[::-1]])
		possible.append(int(r + d, 2))
		i += 1
	return possible

def bfs(start):
	if start == 0:
		return 0
	explored = set()
	frontier = set()
	frontier.add(start)
	i = 0
	while True:
#		print i, frontier
		nextFrontier = set()
		for val in frontier:
			if val in explored:
				continue
			for next in getNextPossible(val):
				if next == 0:
					return i + 1
				nextFrontier.add(next)
		frontier = frontier.union(explored)
		frontier = nextFrontier
		i += 1
