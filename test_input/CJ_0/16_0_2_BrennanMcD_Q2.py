#! /bin/bash/py

f = open("B-large.in")

h = f.read()
h = h.split('\n')

for i in range(int(h[0])):
	print("Case #" + str(i+1) + ": ", end= "")
	s = h[i+1]
	l = 0
	if s[-1] == "-":
		l += 1
	p = s[0]
	for j in range(len(s)):
		if s[j] != p:
			l += 1
		p = s[j]

	print(l)

