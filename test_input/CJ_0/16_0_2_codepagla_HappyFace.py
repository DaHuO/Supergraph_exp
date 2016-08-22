def flip(s) :
	s=list(s)
#	print "s as list",s
	l=len(s)
	for i in xrange(l) :
		if s[i]=='+' :
			s[i]='-'
		else :
			s[i]='+'
	return ''.join(s)


t=int(input())

for i in xrange(1,t+1) :
	s=raw_input()
	s=s.rstrip('+')
	ans=0
	while len(s) :
		if s[0]=='-' :
			s=flip(s)[::-1]
		else :
			indx=s.rfind('+')
			s=flip(s[:indx+1])[::-1]+s[indx+1:]
		ans+=1
#		print "s before strip",s
		s=s.rstrip('+')
#		print "s after strip",s
	print ("Case #%d: %d")%(i,ans)



