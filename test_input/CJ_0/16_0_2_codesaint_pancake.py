import sys

def flip(stack):
	stack = reverse(stack)
	stack = inverse(stack)
	return stack

def reverse(stack):
	return stack[::-1]

def inverse(stack):
	return "".join(map(lambda x: "-" if x =="+" else "+", stack))

def partition(stack):
	l = len(stack)
	initial = stack[0]
	p = 0
	for i in xrange(1, l):
		if stack[i] is not initial:
			p = i
			break
	return stack[:p], stack[p:]


def do_flip(stack, i = 0):
	if '-' not in stack:
		return i
	l = len(stack)
	if stack[0] == '-' and stack[l-1] == '-':
		stack = flip(stack)
		i+=1
	else:
		top, bottom = partition(stack)
		top = inverse(top)
		stack = top + bottom
		i+=1
	return do_flip(stack, i)

cases = 0
for i, line in enumerate(sys.stdin):
	if i == 0:
		cases = int(line.strip())
	elif i <= cases:
		case = line.strip()
		print "Case #%d: %d"  % (i, do_flip(case))
