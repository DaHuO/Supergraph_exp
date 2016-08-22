def changebase(n):
	c = 0
	n = n+"+"
	for i in range(0,len(n)-1):
		if n[i]!=n[i+1]:
			c = c+1
	return(c)

f = open('B-large.in', 'r')
f2 = open('B-large.out', 'w')

b = f.readline()
for i in range(0,int(b)):
	f2.write("Case #"+str(i+1)+": "+str(changebase((f.readline()[:-1])))+"\n")
