import random

def powmod(a,b,m):
	x,p = a,1
	while b>0:
		if b%2 == 1: p = ((p%m)*(x%m))%m
		b/=2
		x=((x%m)*(x%m))%m
	return p

def miller(n,k):
	d,r=n,0
	while d%2==0:
		d/=2
		r+=1
	while(k>0):
		a = random.randrange(2,n-1)
		x = powmod(a,d,n)
		if x==1 or x==n-1:
			k-=1
			continue
		pprime = False
		for pow in range(r-1):
			x = (x*x)%n
			if x==1:
				return True
			if x==n-1:
				pprime=True
		if not pprime: return True
		k-=1
	return False

def ld(n):
	i = 2
	while i*i <= n:
		if n % i == 0:
			return i
		i+=1
	return 0


N = 16
J = 50

print "Case #1:"

FINAL = []

while True:
	num = 0
	l = range(1,15)
	random.shuffle(l)
	for i in range(6):
		num = num | (1<<l[i])
	num = num | 1
	num = num | (1<<(N-1))
	
	CO = []
	flag = True
	for b in range(2,11):
		n = num
		res,p = 0,1
		while n>0:
			res += (n%2)*p
			p*=b
			n/=2
		flag = flag and miller(res,100)
		if flag:
			co = ld(res)
			flag = flag and co>0
			CO.append(co)
	if flag and not num in FINAL and J:
		print "{0:b} {1}".format(num,' '.join(map(str,CO)))
		J-=1
		FINAL.append(num)
	if J==0: break




