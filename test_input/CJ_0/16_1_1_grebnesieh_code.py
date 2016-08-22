for case in xrange(1, input() + 1):
	S = raw_input()
	ans = S[0]
	for x in S[1:]:
		if x >= ans[0]:
			ans = x + ans
		else:
			ans = ans + x
	print "Case #" + str(case) + ": " + ans