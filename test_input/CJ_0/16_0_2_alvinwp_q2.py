
def flip(pancakes, n):
	i = 0
	while i < n:
		if pancakes[i] == "+":
			pancakes[i] = "-"
		else:
			pancakes[i] = "+"
		i += 1
	return pancakes

def solve(pancakes):
	i = 0;
	minTimes = 0
	curr = pancakes[0]
	while i < len(pancakes):
		if pancakes[i] != curr:
			pancakes = flip(pancakes, i)
			curr = pancakes[i]
			minTimes += 1
		i += 1
	if pancakes[0] == "-":
		minTimes += 1
	return minTimes



f = map(lambda x: x.strip(), open("B-large.in", "r").readlines()[1:])
o = open("out.txt", "w")
num = 1
for i in f:
	out = "Case #"+str(num)+": "+str(solve(list(i)))
	o.write(out)
	o.write("\n")
	num += 1
o.close()