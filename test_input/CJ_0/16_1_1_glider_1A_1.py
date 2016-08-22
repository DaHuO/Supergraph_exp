from random import *

T = input()


j = 1
while(T):
	S = raw_input()
	s = S[0]
	for i in S[1:]:
		if(i < s[0]):
			s = s + i
		else:
			s = i + s


	print 'Case #'+str(j)+": "+s
	j += 1
	T -= 1