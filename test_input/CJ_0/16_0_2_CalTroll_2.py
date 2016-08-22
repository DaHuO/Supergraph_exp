def reduce_stack(stack):
	new_stack = []
	curr = None
	for pancake in stack:
		if (pancake != curr):
			new_stack.append(pancake)
			curr = pancake
	return new_stack

#flips the stack
def solve(stack):
	rs = reduce_stack(stack)
	return (int(rs[0] == '+') ^ (len(rs) % 2)) + len(rs) - 1

T = input()
for i in range(T):
	N = raw_input()
	print 'Case #' + str(i + 1) + ': ' + str(solve(N))