import sys


with open(sys.argv[1]) as f:
	content = f .readlines()
cases = int(content[0])

for x in xrange(1,cases + 1):
	final = content[x][0]
	for y in xrange(1, len(content[x]) - 1):
		if content[x][y] >= final[0]:
			final = str(content[x][y]) + final
		else:
			final += str(content[x][y])
	print "Case #" + str(x) + ": " + final