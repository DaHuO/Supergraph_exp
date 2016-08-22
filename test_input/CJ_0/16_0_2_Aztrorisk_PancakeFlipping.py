from Library import *
import math

def solve(n):
	lastc = n[0];
	count = 1;
	for c in n:
		if (lastc != c):
			lastc = c;
			count += 1;
	if lastc == '+':
		count -= 1
	return count



lines = getLines("B-large.in")
out = []

for i in range(int(lines[0])):
	value = list(lines[i + 1].replace("\n", ""))
	res = solve(value)
	out.append("Case #%d: %s"%(i + 1, res))

writeOutLines("out.txt", out)