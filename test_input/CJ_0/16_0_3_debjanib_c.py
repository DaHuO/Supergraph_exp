import string
digs = string.digits + string.letters


def isprime(n):
	n = int(n)
	if n == 2:
	    return -1
	if n == 3:
	    return -1
	if n % 2 == 0:
	    return 2
	if n % 3 == 0:
	    return 3

	i = 5
	w = 2

	count = 500
	while i * i <= n and count > 0:
	    if n % i == 0:
	        return i
	    i += w
	    w = 6 - w
	    count -=1
	return -1

def bin(n):
	l = []
	while n > 0:
		l+=[n % 2]
		n/=2
	return "".join(str(x) for x in l[::-1])

T = int(raw_input())
for t in range(T):
	N, J =map(int, raw_input().split())
	print ("Case #%d:" % (t+1))
	
	start, end = 1<<(N-1), 1<<(N) 
	for num in xrange(start+1, end, 2):
		num2 = bin(num)
		if num2[-1] == "1":
			r, f = [], True
			for i in range(2, 11):
				p = isprime(str(int(num2, base=i)))
				r+=[p]
				if p == -1:
					f= False
					break
			if f:
				print num2, " ".join(str(x) for x in r)
				J-=1
			if J == 0:
				break

