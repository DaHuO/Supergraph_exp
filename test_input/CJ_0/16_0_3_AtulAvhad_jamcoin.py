"""def isprime(n):
    #Returns True if n is prime.
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


def base(a , j):
	ans = 0
	for i in range(len(a)):
		ans += a[-1-i]*(j**i)

		

for _ in range(input()):
	m , n = map(int , raw_input().split())
	count = 0
	flag = 0
	arr = [0 for in range(2,11)]
	for i in xrange(2**(m-2)):
		
		a = bin(i)[2:]
		l = len(a)
		a = "0"*(m - 2 - l) + a 
		a = "1" + a + "1"
	
		for j in range(2 , 11):
			
			k = base(a,j)
			arr[j - 2] = k

			if(isprime(k)):
				flag = 1
				break"""
	
def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            if(len(primfac)>2):
            	return primfac
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac


for _i in xrange(int(raw_input())):
	n,j = map(int,raw_input().split())
	ini = 32769
	fin = 65535
	count = 0
	f = 1
	print "Case #1:"
	for i in xrange(ini,fin+1,2):
		b = bin(i)
		b = b[2:]
		base = []
		temp = []
		for jj in xrange(2,11):
			base.append(int(b,jj))

		for jj in base:
			x = primes(jj)
			temp.append(x[0])
		
		flag = 1
		for ii in xrange(len(base)):
			if(temp[ii]==base[ii]):
				flag = 0
				break
		if(flag!=0):
			print b,
			for ii in temp:
				print ii,
			print ""
			count+=1
			if(count==j):
				f = 0
				break
		if(f==0):
			break

		
	
	
		
		
		
