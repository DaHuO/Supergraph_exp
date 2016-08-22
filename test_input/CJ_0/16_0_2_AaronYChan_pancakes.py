
with open("B-large.in.txt") as f:
	lines = f.readlines()

numTests = int(lines[0])

output = ""

def flip (s, n):
	l = list(s)
	for i in range(0, n+1):
		l[i] = "+" if l[i] == "-" else "-"
	return "".join(l)

for t in range(0, numTests):
	s = lines[t + 1].strip()
	flips = 0
	for i in range(len(s) -1, -1, -1):
		if s[i] == "-":
			s = flip(s, i)
			flips += 1

	output += "Case #" + str(t + 1) + ": " + str(flips) + "\n"

print output
with open("pancakes-out-big.out", "w") as f:
	f.write(output)