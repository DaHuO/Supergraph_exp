from itertools import *;

t=input()
n,j=input().split(' ')
n=int(n);j=int(j)

#for x in range(pow(2,n-2)):
#	'1'+str(int(x,2))+'1'

def isPrime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


l=list(product(range(2),repeat=(n-2)))
for x in range(len(l)):
	l[x]='1'+''.join(map(str, l[x]))+'1'
#print(l)

l2=[]
for x in range(len(l)):
	l2.append([])
	for y in range(2,11):
		l2[x].append(int(l[x],y))
#print(l2) #list list int

l3=[]
c=-1
j2=j
for x in l2:
	c+=1;c2=0
	if j2 == 0: break;

	for y in x:
		if isPrime(y)==True :
			break;
		else : c2+=1
	if c2==9: 
		l3.append(c);j2-=1;

print('Case #1:')
for x in l3:
	print(l[x], end=' ')
	#print('#############', l2[x])
	for y in l2[x]:
		#print(y)
		for z in range(2,y):
			if y%z==0:
				print(z, end=' ')
				break
	print()

bin=input()
print(int(bin,2))
