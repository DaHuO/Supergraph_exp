prime  = []

def sieve():
	tmp = [0] * 70000
	tmp[0] = 1
	tmp[1] = 1
	for i in range(2,300):
		if(tmp[i] == 0):
			j = i*i
			while(j<70000):
				tmp[j] = 1
				j+=i

	for i in range(70000):
		if tmp[i] == 0:
			prime.append(i)

def f(n):
	for i in prime:
		if n%i == 0:
			return i
	return 0;

def conv(n,b):
	tmp = bin(n)[2:]
	ret = 0
	for i in range(0,len(tmp)):
		ret += (n%2*pow(b,i))
		n = n/2
	return f(ret)
t = int(raw_input())

print "Case #1: "
sieve()
n,k = map(int, raw_input().split())
st = 2**(n-1)+1
stp = 2**n
cnt = 0
i = st
while(i <stp):
	
	flag = 1
	if i%2 == 0:
		i+=1
		continue
	for j in range(2,11):
		if(conv(i,j)== 0):
			flag = 0

	if(flag):
		temp = [str(conv(i,j)) for j in range(2,11)]
		print bin(i)[2:] + " " + " ".join(temp)
		cnt+=1
		if(cnt ==k):
			break
	i+=1
