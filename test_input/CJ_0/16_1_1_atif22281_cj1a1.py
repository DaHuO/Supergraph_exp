for t in range(1,int(input())+1):
	s=input()
	f=s[0]
	so=f
	for i in range(1,len(s)):
		if s[i]<f:
			so=so+s[i]
		else:
			so=s[i]+so
			f=s[i]
	print("Case #{}: {}".format(t,so))