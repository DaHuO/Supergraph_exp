filename = "in.01"
filename = "A-small-attempt1.in"
filename = "A-large.in"

test = 0
for line in open(filename).readlines()[1:]:
	test += 1
	print "Case #%d:" % test,
	l = ""
	r = ""
	s = line.strip()
	while len(s) > 0:
		c = max(s)
		pos = s.rfind(max(s))
		l += c
		r = s[pos+1:] + r
		s = s[:pos]
	print l + r
