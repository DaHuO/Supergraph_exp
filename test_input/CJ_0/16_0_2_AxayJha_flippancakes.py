
t=int(input())
for t0 in range(t):
	s=str(input())
	n=len(s)
	c=0
	while True:
		state=True
		
		for i in s:
			if i!='+':
				state=False
				break
		if state==True:
			break
		else:
			l=[x for x in s]
			for a in range(len(l)):
				
				if l[a] == '-':
					n=a
					
			for j in range(n):
				
				if l[j] == '+':
					l[j]='-'
				elif l[j] == '-':
					l[j]='+'
			s=""
			for j in range(n):
				s+=l[j]	
						

		
		c+=1	

	print("Case #"+str(t0+1)+": "+str(c))

			


