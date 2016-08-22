import math


def solve(seq):
 seq = seq[::-1]
 count = 0
 old = "+"
 for i in range(0, len(seq)):
  if seq[i] != old:
   count += 1
  old = seq[i]

 return str(count)


name = "storage/emulated/0/codejam/B-large"
fi = open(name + ".in", "r")

fout = open(name + ".out", "w")

numTestCases = int(fi.readline())
print "#TestCases: ", numTestCases

for i in range(0, numTestCases):
	line = fi.readline().strip()
	#line = map(int, line)

	fout.write("Case #" + str(i + 1) + ": " + solve(line) + "\n")
	print "Case #" + str(i + 1) + ": " + solve(line)

fi.close()
fout.close()