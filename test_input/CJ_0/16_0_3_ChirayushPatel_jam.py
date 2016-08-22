from math import sqrt; from itertools import count, islice

def is_prime(n):
	return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
    
def factof(x):
	for i in range(2, x + 1):
		if x % i == 0:
			return i

t=int(input())
ans=[]
for i in range(t):
	n,j=list(map(int,input().split(' ')))

	nos=[x for x in range(int('1'+'0'*(n-2)+'1',2),int('1'*n,2),2)]
	prime=[]

	for i in nos:
		if is_prime(i) : prime.append(i)
	for i in prime:
		nos.remove(i)

	nosbin = [bin(x)[2:] for x in nos]
	loops=j
	jam=[]
	for k in nosbin:
		if loops==0:
			#break
			pass
		else:
			noinbase=[]
			for l in range(2,11):
				noinbase.append(int(k,l))
			if all([is_prime(l)==False for l in noinbase]):
				loops=loops-1
				jam.append(k)
				answerline=str(k)
				for m in noinbase:
					answerline=answerline+' '+str(factof(m))
				ans.append(answerline)

print("Case #1:")
for i in range(len(ans)):
	print(str(ans[i]))
