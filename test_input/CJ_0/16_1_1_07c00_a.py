#!/usr/bin/env python


N = int(raw_input())
for j in range(N):
	s = raw_input()
	h = s[0]
	r = h
	for c in s[1:]:
		i = 0
		for d in r:
			if d != c:
				h = d
				break
			i += 1
		if i == len(r):
			r = c + r
		else:
			if ord(c) < ord(h):
				r = r + c
			else:
				r = c + r
		h = r[0]
	print "Case #%d: %s" % (j+1, r)
