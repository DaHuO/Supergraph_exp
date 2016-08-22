#!/usr/bin/python


f = open('B-large.in', 'r')
o = open('output', 'w')

T = f.readline()

for x in range(1, int(T)+1):
	S = f.next()
	print S
	changes = 0
	out = 0
	pancakes = []
	for i in xrange(0, len(S)):
		pancakes.append(S[i])
		if (i > 0 and S [i] == '-' and S[i-1] == '+'):
			print i-1, ": ", S [i-1], ", ", i, ": ", S [i]
			changes += 1

	out = changes * 2


	if (pancakes[0] == '-'):
		out += 1
	print out
	o.write("Case #" + str(x) + ": " + str(out) + '\n')
