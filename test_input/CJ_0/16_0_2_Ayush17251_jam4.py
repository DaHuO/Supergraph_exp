def check(m):
	k=-1
	i=0
	while(k<0):
		if m[i]=="+":
			m.remove(m[i])
			m.insert(i,'-')
			i=i+1
		else:
			k=1
	return
	
	
def check1(m):
	k=-1
	i=0
	while(k<0 and i<len(m)):
		if m[i]=="-":
			m.remove(m[i])
			m.insert(i,'+')
			i=i+1
		else:
			k=1
	return





m1=input()
for z in range(m1):
	m=raw_input()
	m=list(m)
	b=len(m)
	v=[]
	for i in range(b):
		v.append("+")
	a=1						
	count=0
	while(a>0):
		x=cmp(v,m)
		if x==0:
			a=0
		else:
			if m[0]=="+":
				check(m)
				count=count+1
			elif m[0]=="-":
				check1(m)
				count=count+1
	print("Case #"+str(z+1)+": "+str(count))
