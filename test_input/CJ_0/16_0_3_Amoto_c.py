from sys import stdin
import math
def criba(n):
	primos=[]
	todos=[0 for i in range(n+1)]
	todos[0]=1;todos[1]=1
	for i in range(2,math.ceil(math.sqrt(n))+1):
		if(todos[i]==0):
			for j in range(i,n//i+1):
				todos[i*j]=1
	for i in range(0,len(todos)):
		if(todos[i]==0):
			primos.append(i)
	return primos
def main():
	primos=criba(10000000)
	t=int(stdin.readline().strip())
	for i in range(1,t+1):
		n,j=[int(x) for x in stdin.readline().strip().split()]
		c=0
		defi=[]
		start=(1<<(n-1))+1
		s=bin(start)
		s=s[2:]
		while c!=j and len(s)==n:
			s=bin(start)
			s=s[2:]
			tmp=[s]
			ban=False
			if(s[0]=='1' and s[-1]=='1'):
				for k in range(2,11):
					a=int(s,k)
					if(not(a in primos)):
						#print(s,a,k)
						for z in range(2,math.ceil(math.sqrt(a))+1):
							if(a%z==0):
								tmp.append(z)
								break
				if(len(tmp)==10):
					#print(s,tmp)
					defi.append(tmp)
					c+=1
			start+=1
		print('Case #'+str(i)+":")
		for a in range(len(defi)):
			s=''
			for b in range(len(defi[i])):
				s+=str(defi[a][b])+' '
			print(s.strip())
main()