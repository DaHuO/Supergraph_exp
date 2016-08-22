f = open('input', 'r')
g = open('output', 'a')
T = int(f.readline())
for i in range(T):
	stack = list(f.readline().strip('\n')[::-1])
	maneuvers = 0
	while '-' in stack:
		lastOccurence = stack.index('-')
		stack = stack[0:lastOccurence] + ['-' if x == '+' else '+' for x in stack[lastOccurence:len(stack)]]
		maneuvers = maneuvers + 1

	g.write("Case #{0}: {1}\n".format(i+1, maneuvers))