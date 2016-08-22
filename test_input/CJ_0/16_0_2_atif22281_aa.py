for t in range(1,int(input())+1):
	s=input()
	c=0
	for i in range(1,len(s)):
		if s[i-1]!=s[i]:
			c+=1
	if s[len(s)-1]=='-':
		c+=1
	print("{0}{1}{2}{3}".format('Case #',t,': ',c))