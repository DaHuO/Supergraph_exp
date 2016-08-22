from math import sqrt
from itertools import count,islice
def isPrime(n):
	if n<2:
		return False;
	for number in islice(count(2),int(sqrt(n)-1)):
		if not n%number:
			return False;
	return True;

def factors(n):
	for i in range(2,int(sqrt(n))+1):
		if n%i==0:
			return i;

c=0;d=[];n=0;
for i in range(33001 ,65536,2):
	b=bin(i)[2:];
	for j in range(2,11):
		t=int(b,j);
		d.append(t);
		if isPrime(t):
			c=1;
	if c==0:
		print(b+" "+str(factors(d[0]))+" "+str(factors(d[1]))+" "+str(factors(d[2]))+" "+str(factors(d[3]))+" "+str(factors(d[4]))+" "+str(factors(d[5]))+" "+str(factors(d[6]))+" "+str(factors(d[7]))+" "+str(factors(d[8])));
	c=0;d=[];n=n+1;
	if n==52:
		break;
