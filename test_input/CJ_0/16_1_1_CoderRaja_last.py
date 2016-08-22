t=int(input())
p=1
while t>0:
	s=input()
	a=[]
	m=''
	a.append(s[0])
	for x in s[1:]:
		if x>=a[0]:
			a=[x]+a
		else:
			a=a+[x]
	for x in a:
		m+=x
	print("Case #%d: %s"%(p,m))
	t-=1
	p+=1 

