for x in xrange(0, int(raw_input())):
	s = raw_input()
	l = len(s)
	i = 1
	p = s[0]
	while i < l:
		if s[i] >= p[0]:
			p = s[i] + p
		else:
			p = p + s[i]
		i = i + 1
	print "Case #" + str(x+1) + ": " + p