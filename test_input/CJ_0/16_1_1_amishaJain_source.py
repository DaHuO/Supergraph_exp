t=int(input())
for _ in range(1,t+1):
	s=input()
	a=s[0]
	for i in range(1, len(s)):
		if s[i]>=a or s[i]==a[0]:
		    a=''.join(s[i])+a
		else:
			a=a+''.join(s[i])
			

	print("Case #",_, ": ",a,sep='')
    