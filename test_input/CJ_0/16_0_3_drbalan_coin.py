from sys import stdin

def eratosthene(n):
	P=[True]*n
	ans=[2]
	for i in range(3,n,2):
		if P[i]:
			ans.append(i)
			for j in range(2*i,n,i):
				P[j]=False
	return ans


def exp(a,b):
	p=0
	p2=1
	result=1
	ap2=a
	while b>0:
		if p2 & b>0:
			b -=p2
			result=(result*ap2)
		p +=1
		p2 *=2
		ap2=ap2*ap2
	return result


def base(chaine,b):
	n=len(chaine)
	r=0
	for i in range(n):
		r=r+int(chaine[i])*exp(b,n-i-1)
	return r

N=10**8
prime=eratosthene(N)

def convert(entier,base):
	L=[]
	n=entier
	a=entier %base
	L.append(a)
	n=(n-a)//base
	while n!=0:
		a=n%base
		L.append(a)
		n=(n-a)//base
	N=len(L)
	A=''
	for i in range(N):
		A=A+str(L[N-i-1])
	return A



def suivant(chaine):
	n=len(chaine)
	c=chaine[:n-1]
	n=base(c,2)
	return convert(n+1,2)+str(1)


#chaine='1000000000000001'
#print(suivant(chaine))
#

def divisor(n):
	i=0
	while i<len(prime) and n%(prime[i])!=0:
		i=i+1
	if i==len(prime) or prime[i]==n:
		return 'prime'
	else:
		return str(prime[i])

cp=0
print('Case #1:')
chaine=str(1)+str(0)*14+str(1)
while cp<50:
	b=2
	d=divisor(base(chaine,b))
	out=''
	while b<11 and d!='prime':
		b=b+1
		out=out+' '+d
		d=divisor(base(chaine,b))
	if b==11:
		print(chaine +out)
		cp=cp+1
	chaine=suivant(chaine)

