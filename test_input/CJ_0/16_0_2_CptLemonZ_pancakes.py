infile = open('B-large.in', 'r')
outfile = open('pancakes.out', 'w')

T = int(infile.readline())
for t in xrange(T):
	S = infile.readline().strip()
	ans = 0
	for i in xrange(len(S) - 1):
		if S[i] != S[i+1]:
			ans += 1
	if S[-1] == '-':
		ans += 1
	outfile.write('Case #' + str(t+1) + ': ' + str(ans) + '\n')
