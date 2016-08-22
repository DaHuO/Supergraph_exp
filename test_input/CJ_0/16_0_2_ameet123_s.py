t=int(input())
k=1
while (k<=t):
	#l=list()
	l=input()
	count=0
	if(len(l)==1):
		if l[0]=='-':
			count+=1
		else:
			count=0
	else:
		for i in range(len(l)-1):
			if l[i]!=l[i+1]:
				count+=1
		if(l[len(l)-1]=='-'):
			count+=1
	print("Case #{0}: {1}".format(k,count))
	k+=1