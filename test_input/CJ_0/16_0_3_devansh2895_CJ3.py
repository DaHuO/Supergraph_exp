from itertools import *;

t=input()
n,j=input().split(' ')
n=int(n);j=int(j)


l=list(product(range(2),repeat=(n-2)))
for i in range(len(l)):
	l[i]='1'+''.join(map(str, l[i]))+'1'

def isPrime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

bl=[]
for x in range(len(l)):
	bl.append([])
	for y in range(2,11):
		bl[x].append(int(l[x],y))

print('Case #1:')

npl=[]
c=-1
j2=j
for x in bl:
	c+=1;c2=0
	if j2 == 0: break;

	for y in x:
		if isPrime(y)==True :
			break;
		else : c2+=1
	if c2==9: 
		npl.append(c);j2-=1;


for p in npl:
	print(l[p], end=' ')
	for q in bl[p]:
		for r in range(2,q):
			if q%r==0:
				print(r, end=' ')
				break
	print()