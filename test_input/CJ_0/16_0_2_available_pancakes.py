
t = int(input())
for tc in range(t):
	s = input()
	l = [[0, 0]] * len(s)
	if s[0] == '-': l[0][0] = 1 # to +
	if s[0] == '+': l[0][1] = 1 # to -
	for i in range(1, len(s)):
		if s[i] == '+':
			l[i][0] = min(l[i - 1][0], 1 + l[i - 1][1])
			l[i][1] = min(1 + l[i - 1][0], 3 + l[i - 1][1])
		else:
			l[i][0] = min(3 + l[i - 1][0], l[i - 1][1] + 1)
			l[i][1] = min(1 + l[i - 1][0], l[i - 1][1])
	print ('Case #' + str(tc + 1) + ': ' + str(l[-1][0]))