T = int(raw_input())
for i in range(1, T+1):
	S0 = raw_input()
	c0 = S0[0]
	S = [c0]
	for c in S0:
		if c != c0:
			S.append(c)
			c0 = c
	if S[-1] == '+':
		S.pop()

	print 'Case #' + str(i) + ': ' + str(len(S))
