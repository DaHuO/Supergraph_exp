def flip(s):
	return ''.join('+' if c == '-' else '-' for c in s[::-1])

def naive(stack):
	stacks = set([stack])
	
	goal = '+'*len(stack)
	
	count = 0
	
	while not goal in stacks:
		count += 1
		new_stacks = set()
		
		for stack in stacks:
			for i in range(1,len(stack)+1):
				new_stack = flip(stack[:i]) + stack[i:]
				new_stacks.add(new_stack)
		
		stacks = new_stacks
	
	return count

def fast(stack):
	count = 0
	prev = '+'
	for c in stack[::-1]:
		if c != prev:
			count += 1
		prev = c
	return count
	

n_cases = input()

for case in range(1, n_cases+1):
	i = raw_input()
	print 'Case #%d:' % case,
	print fast(i)
