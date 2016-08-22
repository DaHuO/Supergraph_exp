PROBLEM="a.";
i=open(PROBLEM+"in","r");
o=open(PROBLEM+"out","w");
t= int(i.readline());
for z in range(t):
	a=[]
	l=list(i.readline().rstrip())
	a.append(l[0])
	for x in range(len(l)-1):
		if l[x+1]>=a[0]:
			a.insert(0,l[x+1])
		else:
			a.append(l[x+1])
	a=''.join(a)
	o.write("Case #"+str(z+1)+": "+str(a)+"\n")
