from sys import stdin
def main():
	n=int(stdin.readline().strip())
	for i in range(1,n+1):
		s=stdin.readline().strip()
		#print(s)
		arr=transform(s)
		#print(arr)
		c=count(arr)
		print('Case #'+str(i)+': '+str(c))
def transform(s):
	a=[]
	for i in range(len(s)):
		if(s[i]=='-'):
			a.append(0)
		else:
			a.append(1)
	return a
def count(a):
	c=0
	while(sum(a)!=len(a)):
		c+=1
		a=flip(a,a[0])
	return c
def flip(a,char):
	i=0
	while(i<len(a) and a[i]==char):
		a[i]=1-a[i]
		i+=1
	b=a[:i]
	b.reverse()
	return b+a[i:]
main()