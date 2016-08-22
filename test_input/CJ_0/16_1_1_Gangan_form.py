
def perms(s,k,dir):
	if(s==""):
		return [k]
	else:
		c=s[0]
		s=s[1::]
		if(dir==1):
			k=k+c
		else:
			k=c+k
		return perms(s,k,0)+perms(s,k,1)
def getPerm(s):
	a=perms(s,"",0)+perms(s,"",1)
	a.sort()
	return sorted(a)[-1]

cases = int(input())
for i in range(cases):
	x=input()
	print("Case #"+str(i+1)+": "+getPerm(x))

