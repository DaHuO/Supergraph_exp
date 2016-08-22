t = int(raw_input())
for i in xrange(1,t+1):
	s = list(str(raw_input()))
	a = s[0]
	for j in s[1:]:
		if ord(j) < ord(a[0]):
			a = a + j
		else:
			a = j + a
	print "Case #{}: {}".format(i,''.join(a))
			