def solve(S):
	cur = S[0]
	for c in S[1:]:
		if (cur + c) > (c + cur):
			cur = (cur + c)
		else:
			cur = (c + cur)
	return cur

if __name__ == '__main__':
	T = int(raw_input())
	for t in xrange(T):
		S = raw_input().strip()
		print "case #%d: %s" % (t+1,solve(S))
