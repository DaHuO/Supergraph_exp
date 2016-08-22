for t in xrange(1, int(raw_input()) + 1):
	s = [1 if i != '+' else 0 for i in raw_input()]
	out = 0
	for i in reversed(s):
		if (i + out) % 2:
			out += 1

	print 'Case #%s: %s' % (t, out)
