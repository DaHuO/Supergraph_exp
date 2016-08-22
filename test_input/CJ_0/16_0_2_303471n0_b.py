f = open('B-large.in', 'r')
o = open('ob.txt', 'w')
f = f.readlines()[1:]
	
def flip(ind, stack):
	temp = stack[:ind+1]
	temp = temp[::-1]
	for i, x in enumerate(temp):
		if x == '-':
			stack[i] = '+'
		else:
			stack[i] = '-'
	return stack
	

for c,stack in enumerate(f):
	stack = list(stack)
	if stack[len(stack) - 1] == "\n":
		stack = stack[:len(stack)-1]
	
	count = 0
	while True:
		ix = 0
		if stack[0] == '-':
			while ix+1 < len(stack) and stack[ix+1] == "-":
				ix += 1
			flip(ix, stack)
			count += 1
		elif stack[0] == '+':
			while ix+1 < len(stack) and stack[ix+1] == "+":
				ix += 1
			if ix+1 == len(stack):
				o.write("Case #" + str(c+1) + ": " + str(count) + "\n")
				print count
				break
			else:
				flip(ix, stack)
				count += 1