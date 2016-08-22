def cal(s):
	l1=[]
	for i in range(2,11):
		n=int(s,i)
		for j in range(3,int(n**0.5)+1,2):
			if(n%j==0):
				l1.append(j)
				break
	if(len(l1)==9):
		s1=s
		for j in l1:
			s1+=" "+str(j)
		print(s1)
		return 1
	return 0
l=[]
def check(n):
	for i in range(3,int(n**0.5) +1,2):
		if(n%i==0):
			l.append(n)
			break
for i in range(2**15+1,2**16 -1,2):
	check(i)
data=open("C-small-attempt0.in","r")
S=data.read()
S=S.split("\n")
t=int(S[0])#int(input())
for i in range(1,t+1):
	print("Case #{0}:".format(i))
	s=S[i]
	n,j=int(s.split()[0]), int(s.split()[1])
	l=[]
	for i in range(2**(n-1)+1,2**n -1):
		check(i)
	for i in l:
		s=bin(i)[2:]
		if(s[-1]=="0"):
			continue
		k=cal(s)
		j=j-k
		if(j==0):
			break