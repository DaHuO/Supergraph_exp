def p(s):
	def flip(c):
		return '-' if c == '+' else '+'
	s = map(lambda x:x, s)	
	l = len(s)-1

	n = 0
	while True:
		while l>=0 and s[l] == '+':
			l -= 1

		if not l>=0:
			return n
		else:
			s[:l] = map(flip, s[:l])
			n += 1
			l -= 1

if __name__ == '__main__':
	f = open('in.txt', 'r')
	for i, line in enumerate(f.read().split('\n')):
		if line and i!=0:
			ans = p(line)
			print 'Case #%s: %s' % (i, ans)
	f.close()
