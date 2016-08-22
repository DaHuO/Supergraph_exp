import sys

def answer(s):
	stack = s + '+'
	flips = 0
	for i in range(len(s)):
		if stack[i] != stack[i+1]:
			flips += 1
	return flips

if __name__ == '__main__':
	f = sys.stdin
	fn = sys.argv[1]
	f = open(fn)
	if len(sys.argv) == 3:
		output = open(sys.argv[2], 'w')
	t = int(f.readline())
	for _t in xrange(t):
		s = f.readline().strip()
		ans = answer(s)
		if len(sys.argv) == 3:
			output.write('Case #%d: %s' % (_t+1, ans) + '\n')
		print 'Case #%d: %s' % (_t+1, ans)
