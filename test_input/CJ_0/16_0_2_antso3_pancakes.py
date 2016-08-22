f = file("in", "r")
lines = f.readlines()
lines = map(lambda x: x[:-1], lines)
n = int(lines[0])
f.close()

def flip(c):
	if c == '+':
		return '-'
	else:
		return '+'

def getres(stack):
	count = 0
	stack = list(stack)
	for i in range(len(stack)-1, -1, -1):
		if stack[i] == "-":
			count+=1
			for j in range(0, i+1):
				stack[j] = flip(stack[j])
	return str(count)

g = file("out", "w")

for i in range(1, n+1):
	g.write("Case #" + str(i) + ": " + getres(lines[i]) + "\n")

g.close()	
