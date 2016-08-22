tests = int(input())


def solve(s):
	i = 1
	r = s[0]
	while i < len(s):
		if s[i] >= r[0]:
			r = s[i] + r
		else:
			r = r + s[i]
		i += 1
	return r

test = 1
while test <= tests:
	s = input()
	print('Case #%d: %s' % (test, solve(s)))
	test += 1