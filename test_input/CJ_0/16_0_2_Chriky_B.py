import codejam as gcj
gcj.load_input('B-large.in')

T = gcj.read_input('i')
for t in range(T):
	S = gcj.read_input('s')

	c, parts = '', []
	for s in S:
		if c != s:
			parts += [s]
			c = s

	if parts[-1] == '+':
		parts.pop()

	print 'Case #%i:' % (t + 1), len(parts)

