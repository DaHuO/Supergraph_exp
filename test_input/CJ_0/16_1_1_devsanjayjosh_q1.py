def find(a):
	ans=a[0]
	for i in range(1,len(a)):
		if(a[i]>=ans[0]):
			ans=a[i]+ans
		else:
			ans=ans+a[i];	

	return ans;		





t=int(input())

for i in range(1,t+1):
	a=input()
	v=find(a)
	s="Case #"+str(i)+":"
	print(s,v);