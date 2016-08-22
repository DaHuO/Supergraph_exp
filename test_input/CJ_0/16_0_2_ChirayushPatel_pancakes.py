t=int(input())
ans=[]
for i in range(0,t):
	pan=input()
	stack=[]
	for i in pan: stack.append(i=='+')
	tries=0
	while(all(stack)==False):
		i=len(stack)-1
		while stack[i] and i!=0: i=i-1
		for j in range(0,i+1):
			stack[j]=(stack[j]==False)
		tries=tries+1
	ans.append(tries)
	stack=[]
for i in range(len(ans)):
	print("Case #"+str(i+1)+": "+str(ans[i]))
