i=open("b.in","r");
o=open("b.out","w");
n=0;
t=int(i.readline());
for z in range(t):
	s=list(i.readline());
	s=s[::-1];
	l=len(s);
	for x in range(l):
		if s[x]=="-":
			for y in range(x,l):
				if s[y]=="-":
					s[y]="+";
				else:
					s[y]="-";
			n=n+1;
	o.write("Case #"+str(z+1)+": "+str(n)+"\n");
	n=0;
