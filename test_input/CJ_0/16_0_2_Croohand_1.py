t = int(input())
for test in range(t):
	print('Case #%s: ' % (test + 1), end = '')
	s = list(input())
	if not '-' in s:
		print(0)
	elif not '+' in s:
		print(1)
	else:
		ans = 0
		while '-' in s:
			if s[0] == '-':
				r = len(s) - s[::-1].index('-')
				s[0:r] = s[r - 1::-1]
				for i in range(r):
					s[i] = '-' if s[i] == '+' else '+'
				ans += 1
			else:
				r = s.index('-')
				s[0:r] = ['-' for i in range(r)]
				ans += 1

		print(ans)