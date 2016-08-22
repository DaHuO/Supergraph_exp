import queue
from math import ceil

inputs = []
with open("B-large.in") as f:
    lines = f.readlines()
    inputs = [w[:-1] for w in lines[1:]]

for i in range(len(inputs)):
	s = inputs[i]
	print("Case #" + str(i + 1) + ": ", end="")
	switches = 1
	for i in range(1, len(s)):
		if s[i - 1] != s[i]:
			switches += 1
	print(switches - 1 if s[len(s) - 1] == "+" else switches)