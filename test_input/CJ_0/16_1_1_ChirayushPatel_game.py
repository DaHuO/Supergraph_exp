s=int(input())
ans=[]
for i in range(s):
	s=str(input())
	ansstr=s[0]
	for j in s[1:]:
		if(j>=ansstr[0]):
			ansstr=j+ansstr
		else: ansstr = ansstr+j
	ans.append(ansstr)
for i in range(len(ans)):
	print("Case #"+str(i+1)+": "+str(ans[i]))
