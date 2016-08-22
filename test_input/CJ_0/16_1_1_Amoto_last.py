from sys import stdin
def Booth(S):
	S+=S
	f= [-1]*len(S)
	k=0
	for j in range(1,len(S)):
		i=f[j-k-1]
		while i!= -1 and S[j]!=S[k+i+1]:
			if S[j]<S[k+i+1]:
				k=j-i-1
			i=f[i]
		if i==-1 and S[j]!=S[k+i+1]:
			if S[j]<S[k+i+1]:
				k=j
			f[j-k]=-1
		else:
			f[j-k]=i+1
	return k
def main():
	n=int(stdin.readline().strip())
	for i in range(1,n+1):
		s=stdin.readline().strip()
		a=[s[0]]
		for j in range(1,len(s)):
			tmp=[]
			while(len(a)>0 and len(a[-1])<len(s)):
				z=a.pop()
				#print(z,s[j],z+s[j],s[j]+z)
				tmp.append(z+s[j])
				tmp.append(s[j]+z)
			a=tmp
		a.sort()
		print('Case #'+str(i)+': '+a[-1])
main()