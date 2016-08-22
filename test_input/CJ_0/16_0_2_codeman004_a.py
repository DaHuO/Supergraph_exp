t=input()
c=1
while t>0:
	s=raw_input()
	s=list(s)
	index=len(s)-1;
	result=0
	while(index>=0):
		if(s[index]=="-"):
			for i in range(index,-1,-1):
				if s[i]=="-":
					s[i]="+"
				else:
					s[i]="-"
			result+=1
		index-=1
	print "Case #"+str(c)+": "+str(result)
	c+=1
	t-=1
