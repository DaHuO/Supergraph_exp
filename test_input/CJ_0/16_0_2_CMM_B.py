

def solve(s):
	
	stack = [1 if i == "+" else -1 for i in s[::-1]]
	count = 0
		
	while True:
		if -1 not in stack:
			return count
		count += 1
		n = stack.index(-1)
		for j in range(n, len(stack)):
			stack[j] *= -1



for case in range(int(raw_input())):
	s = raw_input()
	print "Case #%d: %s" %(case+1, solve(s))
