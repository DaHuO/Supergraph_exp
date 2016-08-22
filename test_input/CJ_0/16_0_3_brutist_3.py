from random import randrange
def is_prime(n, k=10):

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for i in xrange(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

	if n%2==0 or n%3==0:
		return False

    s = 0
    d = n - 1

    while d % 2 == 0:
        d >>= 1
        s += 1

    for i in xrange(k):
        a = randrange(2, n - 1)
        if not check(a, s, d, n):
            return False
    return True

def getdivisor(n):
	i=3
	if n%2==0:
		return 2
	sq=n**0.5
	while i<=(sq):
		if n%i==0:
			return i
		i+=2
		if i>10**5:
			return -1
	return -1

maxi=10**7+1
isprime=[1]*(maxi+2)
for i in range(2,maxi):
	if isprime[i]:
		for j in range(i*i,maxi,i):
			isprime[j]=0
isprime[0]=0
isprime[1]=0
t=input()
n,mx=map(int,raw_input().split())
end=int("1"*n,2)
s="1"
s+="0"*(n-2)
s+="1"
start=int(s,2)
done=0
print "Case #1:"
i=end
while i>=start:
	if(done==mx):
		break
	curst=bin(i)[2:]
	failed=False
	for j in range(2,11):
		tocheck=int(curst,j)
		if tocheck<=10**7:
			if isprime[tocheck]:
				failed=True
				break
		else:
			if is_prime(tocheck):
				failed=True
				break
	if not failed:
		ans=[curst]
		for j in range(2,11):
			lol=getdivisor(int(curst,j))
			if lol==-1:
				break
			ans.append(str(lol))
		if len(ans)==10:
			print ' '.join(ans)
			done+=1
	if done>=20:
		i-=100
	else:
		i-=2