N = int(raw_input())
case = 1

for _ in xrange(N):
	
	s = raw_input()
	res = 0
	
	for i in xrange(1,len(s)):
		if s[i] != s[i-1]:
			res += 1
	
	if s[-1] == '-':
		res += 1
	
	print 'Case #' + str(case) + ':', res
	case += 1