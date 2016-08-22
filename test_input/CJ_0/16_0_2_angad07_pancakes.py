#!/usr/bin/python

t = input()
op=[]
tmp=0
while(tmp<t):
	s = raw_input()
	x = list(s)
	count=0
	if(x[0]=='+'):
		if(len(x)==1):
			op.append(0)
			tmp+=1
			continue
		for i in range(len(x)-1):
			if(x[i]=='+' and x[i+1]=='-'):
				count+=1
			elif(x[i]=='-' and x[i+1]=='+'):
				if((i+1)!=len(x)):
					count+=1
		if(x[len(x)-1]=='-'):
			count+=1
		op.append(count)

	elif(x[0]=='-'):
		if(len(x)==1):
			op.append(1)
			tmp+=1
			continue
		for i in range(len(x)-1):
			if(x[i]=='+' and x[i+1]=='-'):
				count+=1
			elif(x[i]=='-' and x[i+1]=='+'):
				count+=1
		if(x[len(x)-1]=='-'):
			count+=1
		op.append(count)
	tmp+=1


for j in range(t):
	print "Case #"+str(j+1)+": "+str(op[j])
