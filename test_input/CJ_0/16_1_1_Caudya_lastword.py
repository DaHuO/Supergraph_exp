def boucle(n):
	a = n[0]
	for i in range(1,len(n)):
		if n[i]>a[len(a)-1] and n[i]<a[0]:
			a = a+n[i]
		else:
			if n[i]>a[len(a)-1]:
				a = n[i]+a
			else: 
				a = a+n[i]
	return(a)

f = open('A-large.in', 'r')
f2 = open('A-large.out', 'w')

b = f.readline()
for i in range(0,int(b)):
	f2.write("Case #"+str(i+1)+": "+str(boucle(f.readline())))
