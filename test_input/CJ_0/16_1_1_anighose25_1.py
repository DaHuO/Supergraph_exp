t=raw_input()
caseno=1
for i in range(0,int(t)):
	s=raw_input()
	answer=s[0]
	for k in range(1,len(s)):
		if answer[0]<=s[k]:
			answer=s[k]+answer
		else:
			answer=answer+s[k]
	print "Case #"+str(caseno)+": "+answer
	caseno = caseno +1

