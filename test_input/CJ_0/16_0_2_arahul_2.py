t=int(raw_input())
case=0
for _ in range(t):
	case+=1
	s=raw_input()
	ans=0
	flag1=0
	flag2=0
	i=0
	while True:
		if(i>=len(s)):
			break
		if(s[i]=='+'):
			flag2=1
			i+=1
			if(flag1==0):
				continue
			else:
				flag1=0
				ans+=1
				continue
		if(flag1==1):
			i+=1
			continue
		if(flag2==1):
			ans+=1
		flag1=1
		i+=1
	if(flag1==1):
		ans+=1
	print("Case #"+str(case)+": "+str(ans))
