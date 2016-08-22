t=int(input())
i=0
while(t>0):
	s=input()
	str=s[0]
	for i in range (len(s)-1):
		if(s[i+1]>=str[0]):
			str=s[i+1]+str
		else:
			str+=s[i+1]
	print("Case #{}: {}".format(i,str))
	i+=1
	t-=1