t = int(input())
for i in range(t):
	t -= 1
	
	s = input() + '+'
	p = s[0]
	ans = 0
	for c in s:
		ans += c != p
		p = c
	
	print('Case #%d: %d' % (i + 1, ans))
