#!/usr/bin/python


f = open('A-large.in', 'r')
o = open('output', 'w')

T = f.readline()
S = ""
out = ""

def insertRight (letter):
	global out 
	out += letter

def insertLeft (letter):
	global out
	for x in range(len(S), 0):
		out[x+1] = out[x]
	out = letter + out[0:]

for x in range(1, int(T)+1):
	S = f.next()
	out = ""
	for i in xrange(0, len(S)):
		if (i > 0):
			if (S[i] >= out [0]):
				insertLeft(S[i])
			else:
				insertRight(S[i])

		else:
			out += S[i]

	o.write("Case #" + str(x) + ": " + out)
