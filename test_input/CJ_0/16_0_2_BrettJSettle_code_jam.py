lines = open('A-small-attempt0.in', 'r').readlines()
cases = int(lines[0])
if cases < 1 or cases > 100:
	print("Cases out of range")
	exit(0)

s = ''

def flip(stack, num):
	if num >= 0:
		return ('-' if stack[0] == '+' else '+') + flip(stack[1:], num-1)
	return stack

for case in range(1, cases+1):
	stack = lines[case].strip()
	if len(stack) == 0 or len(stack) > 100:
		s += ("Stack size out of range\n")
		continue
	flips = 0
	while '-' in stack:
		ind = stack.rfind('-')
		stack = flip(stack, ind)
		flips += 1
	s += "Case #%s: %s\n" % (case, flips)


with open("out.txt", "w") as outf:
	outf.write(s)


