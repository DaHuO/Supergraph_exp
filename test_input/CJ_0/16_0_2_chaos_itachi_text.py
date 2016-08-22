def flip(st):
	s = list(st)
	for c in xrange(0,len(s)):
		if s[c] == '+' :
			s[c] = '-'
		elif s[c] == '-':
			s[c] = '+'
	return  "".join(s)

tc = int(raw_input())
for tc in xrange(1,tc+1):
	count = 0
	ss = raw_input()
	while True:
		ss = ss.rstrip('+')
		if len(ss) == 0:
			break
		ss = flip(ss)
		count = count + 1
		
	print "Case #" + str(tc) + ":" + " " + str(count)