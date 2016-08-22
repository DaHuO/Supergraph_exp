def solve(S):
	res = S[0]
	for i in range(1, len(S)):
		if S[i] >= res[0]:
			res = S[i] + res
		else:
			res = res + S[i]
	return res

t = int(raw_input())
for i in xrange(1, t + 1):
  S = raw_input()
  print "Case #{}: {}".format(i, solve(S))
