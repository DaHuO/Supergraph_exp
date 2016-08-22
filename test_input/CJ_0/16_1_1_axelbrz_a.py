f = open("a.in")
d = f.read().strip().split("\n")[1:]
f.close()

o = open("a.out", "w")
for i in xrange(len(d)):
	s = d[i][0]
	for c in d[i][1:]:
		if s[0] <= c: s = c + s
		else: s += c
	ln = "Case #%d: %s" % (i + 1, s)
	print ln
	o.write(ln + "\n")
o.close()
