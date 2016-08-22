T = int(raw_input())

def solve():
	s = str(raw_input())
	cnt = 1
	t = s[0]
	for i in range(1, len(s)):
		if(s[i] >= t[0]):
			t = s[i] + t
		else:
			t = t + s[i]
	return t

for case in range(T):
	print 'Case #' + str(case + 1) + ':', solve()
