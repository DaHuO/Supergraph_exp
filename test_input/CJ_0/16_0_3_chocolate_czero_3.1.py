N,J = 32,500
S='1'+30*'0'+'1'

import time

def factors(n):
	t1=time.time()
	if n%2 == 0:
		return 2
	i = 3
	while i <= (int(n**0.5) + 3):
		t2=time.time()
		if t2-t1>1.0:
			return 1.5
		if n%i == 0:
			return i
		# else:
		# 	n //= i
		i+=2
	return n

    # return sorted(set(reduce(list.__add__, 
    #             ([i, n//i] for i in xrange(1, int(n**0.5) + 1) if n % i == 0))))[1]

outf = open("primes.txt", "w")

for i in xrange(pow(2,(N-2))):
	S_2 = int(S, 2)
	S_3 = int(S, 3)
	S_4 = int(S, 4)
	# print S_4
	S_5 = int(S, 5)
	S_6 = int(S, 6)
	S_7 = int(S, 7)
	S_8 = int(S, 8)
	S_9 = int(S, 9)
	S_10 = int(S)
	# S = str(S_10)
	S = str(bin(S_2+2)[2:])

	fS_2 = factors(S_2)
	fS_3 = factors(S_3) 
	fS_4 = factors(S_4) 
	fS_5 = factors(S_5) 
	fS_6 = factors(S_6) 
	fS_7 = factors(S_7) 
	fS_8 = factors(S_8) 
	fS_9 = factors(S_9) 
	fS_10 = factors(S_10)

	if 	(S_2 ==fS_2 or S_3 ==fS_3 or S_4 ==fS_4 or S_5 ==fS_5 or \
		S_6 ==fS_6 or S_7 ==fS_7 or S_8 ==fS_8 or S_9 ==fS_9 or \
		S_10 ==fS_10 or \
		fS_2 ==1.5 or fS_3 ==1.5 or fS_4 ==1.5 or fS_5 ==1.5 or \
		fS_6 ==1.5 or fS_7 ==1.5 or fS_8 ==1.5 or fS_9 ==1.5 or \
		fS_10 ==1.5):
		continue
	else:
		outf.write("%d %d %d %d %d %d %d %d %d %d\n"%(S_10, fS_2, fS_3, fS_4, fS_5, fS_6, fS_7, fS_8, fS_9, fS_10))
		print S_10, fS_2, fS_3, fS_4, fS_5, fS_6, fS_7, fS_8, fS_9, fS_10
		J = J-1
		if J == 0:
			break
	
outf.close()
print 'done'