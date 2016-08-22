import math

def gen(l,a):
	ar=[]
	L=a-1
	for i in range(2,11):
		ans=1+pow(i,L);
		for j in range(1,L):
			if l[j] == 1:
				ans=ans+pow(i,L-j)
			#print(ans)
		#print('Over');	
		K=math.floor(math.sqrt(ans))+1
		x=2
		#for i in range(2,K):
		while x < K and ans%x!=0:
			x=x+1
		if (x==K):
			#print('False.........................................')
			return False
		ar.append(x)
		#print(ar)				
	return ar;


def next(l,a):
	i=a-2
	#if(l[a-2]==0):
	#	l[a-2]
	while i > 0 and l[i] == 1 :
		i=i-1;
	if i!= 0:
		l[i]=1;
		for j in range(i+1,a-1):
			l[j]=0
	return l;		



def find(a,b):

	#a=int(a)
	l=[1] +[0]*(a-2)+[1]
	#print(l)
	c=0
	while c != b:
		l1=gen(l,a);
		if type(l1) == list :
			#print(c,b,'Woah')
			for j in l:
				print(j,end="")
			print(' ',end="")	
			for j in l1:	
				print(j,end=" ")
			print()	
			c=c+1;
		#else :
			#print(l1)	




		l=next(l,a);
		#print(l)




t=int(input())

for i in range(1,t+1):
	a=input()
	#print(a)
	b=list(map(int,a.split()))
	s="Case #"+str(i)+":"
	print(s);
	find(b[0],b[1])
	