#!/usr/bin/python2

f = open('A-small-attempt0.in', 'r')
t = int(f.readline().rstrip()) # Number of test cases.
test_cases = []
for i in range(t):
	test_cases.append(f.readline().rstrip())
f.close()

for i in range(0, len(test_cases)):
	words = []
	S = list(test_cases[i])
	for l in S:
		if len(words) == 0:
			words.append(l)
		elif len(words) > 0:
			newwords = []
			for word in words:
				newwords.append(l + word)
				newwords.append(word + l)
			words = newwords[:]
	words.sort()
	print "Case #%s: %s" % (i+1, words[-1])
