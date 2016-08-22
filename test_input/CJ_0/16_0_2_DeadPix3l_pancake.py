def removeDups(x):
	out=[]
	lc = ''
	for i in x:
		if i!=lc: out.append(i)
		lc=i
	return out

with open("pancakes.in",'r') as f:
	T = int(f.readline()) #tetcases
	for i in range(1,T+1):
		count=0
		stack = list(f.readline().rstrip())
		stack=removeDups(stack)
		while(len(stack)>1): # some pancakes face the other direction
			if stack[0]=='+': x = '-'
			else: x = '+'
			stack[0]=x
			stack=removeDups(stack)
			count+=1
		if stack==['-']: count +=1 # make sure you face them all upwards
		print "Case #{}: {}".format(i,count)
				

