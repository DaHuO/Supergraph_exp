#!/bin/python

t = int(raw_input())

def Construct(l, s):
	if s == "":
		return l
	elif l == "":
		return Construct(s[0],s[1:])
	else:
		if l[0] <= s[0]:
			return Construct(s[0]+l,s[1:])
		else:
			return Construct(l+s[0],s[1:])


def LastWord(s):
	l = s[0]
	s = s[1:]
	while s != "":
		if l[0] <= s[0]:
			l = s[0]+l
		else:
			l = l+s[0]
		s = s[1:]
	return l


for i in xrange(1, t + 1):
	s = raw_input()
	o = LastWord(s)
	print "Case #{}: {}".format(i, o)