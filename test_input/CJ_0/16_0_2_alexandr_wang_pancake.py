import sys

lines = sys.stdin.readlines()
lines = map(str.strip, lines)

INF = 1e8

def change(state):
	new = ""
	for c in state:
		new += "+" if c == "-" else "-"
	return new

def flip(state, i):
	return change(state[:i][::-1]) + state[i:]

def bfs(memo, state, ans, queue):
	if state in memo:
		return memo[state]
	# print "state: " + state

	memo[state] = ans

	for i in xrange(1, len(state) + 1):
		# print "this"
		newstate = flip(state, i)
		# print newstate
		queue.append((newstate, ans+1))
	return ans


T = int(lines[0])

for i in xrange(1, T+1):
	ck = lines[i]

	start = '+' * len(ck)
	memo = {}
	queue = []
	bfs(memo, start, 0, queue)
	while queue:
		front = queue.pop(0)
		bfs(memo, front[0], front[1], queue)
	print "Case #" + str(i) + ": " + str(memo[ck])