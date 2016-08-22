M=""
for t in range(int(input())):
	s=input()
	n=len(s)
	a=s[0]
	for i in range(1,n):
		if s[i]>=a[0]:
			a=s[i]+a
		else:
			a=a+s[i]
	M+="Case #"+str(t+1)+": "+a+"\n"
print(M[:len(M)-1])

