def cal(s,s1):
	m=len(s)-1
	if(s.count(s1)==m+1):
		return 0
	while(m>=0):
		if(s[m]==s1):
			m-=1
		else:
			s2="+"
			if(s1=="+"):
				s2="-"
			return(1+cal(s[:m+1],s2))
			break
	return 0
data=open("B-large.in","r")
s1=data.read()
s1=s1.split("\n")
t=int(s1[0])
for i in range(1,t+1):
	n=s1[i]#input()
	if(n=="" or n.count("+")==len(n)):
		print("Case #{0}: 0".format(i))
	else:
		print("Case #{0}: {1}".format(i,cal(n,"+")))
