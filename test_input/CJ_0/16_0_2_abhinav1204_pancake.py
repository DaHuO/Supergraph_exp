for z in range(int(input())):
	s=input();
	prev=s[0]
	ans=0
	for i in range(1,len(s)):
		if s[i]!=prev:
			ans+=1
			prev=s[i]
	if s[len(s)-1]=='-':
		print("Case #{}: {}".format(z+1,ans+1))
	else:
		print("Case #{}: {}".format(z+1,ans))

