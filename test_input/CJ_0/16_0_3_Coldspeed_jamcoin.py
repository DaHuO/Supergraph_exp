import math
def isPrime(n):
	global t1, t2
	#print("prime zdcz")
	#print("sqrt: ", math.sqrt(n))
	for i in range(2, int(math.sqrt(n))+1):

		if n%i == 0: 
			return (0, i)
		t2=time.time()
		#print(t1, t2)
		if(t2-t1>0.1): return (1, None)
	return (1, None)

L=[]
import time
t1, t2=None, None
def isJamcoin(num):
	global t1, t2
	for i in range(2, 11):
		#print("jam zdcz")
		temp = int(num, i)
		#print(temp)
		t1=time.time()
		R = isPrime(temp)
		#print(R)
		if R[0] == 1:
			L.clear()
			return False
		else:
			L.append(R[1])

	return True


input()

N, J = map(int, input().split())

num = int(math.pow(2, N-1)) + 1

index = -2

count = 0

print("Case #1:")

while True:
	#print("zdcz")
	if count == J: break
	if isJamcoin(str(bin(num))[2:]): 
		count+=1
		print(str(bin(num))[2:], ' '.join(list(map(str, L))))
		L.clear()

	num = num + 2


	#print(num)
	





