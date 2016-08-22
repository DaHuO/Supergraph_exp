t=int(input())
for j in range(t):
	s=input()
	lns=len(s)
	c=0
	for i in range(0,lns-1):
		if (s[i]!=s[i+1]):
			c+=1
	if s[-1]=='-':
		c=c+1
	print("Case #" + str(j+1) +": "+str(c))
