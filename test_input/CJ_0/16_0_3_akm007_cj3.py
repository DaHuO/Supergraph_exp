count = 0
maxcount = 0

def prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(n/2 + 1), 2):
        if n % i == 0:
            return False
    return True

def getFactor(n,factors):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n



def checkbase(num):
	global count

	numrev = str(num)[::-1]
	primeflg = False
	factors = []

	for i in range(2,11):

		value = 0

		for j in range(0,len(num)):
			digit = int(numrev[j])
			value = value+(i**j)*digit

		if prime(value):
			primeflg = True
			break

		else:
			factors.append(getFactor(value,factors[:]))

	if primeflg == False:
		print num,

		for fct in factors:
			print fct,
		print ""	

		count = count + 1


def makebinary(leng):
	global count
	global maxcount
	leng = leng - 2
	flg = False

	arr = []

	for i in range(0,leng):
		arr.append(0)

	while True:

		if flg:
			break;

		i = len(arr) - 1

		while True:
			if arr[i] == 0:
				arr[i] = 1;
				break;
	
			else:
				arr[i] = 0
				i = i - 1
				if i == -1:
					flg = True
					break;

		
		s = "1"
 
		for i in arr:
			s = s + str(i)
		s = s + "1"
		# print s	
		checkbase(s)

		if count == maxcount:
			break





t = int(raw_input())

for i in xrange(1, t + 1): 
	n, maxcount = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case

	print "Case #{}:".format(i)
	makebinary(n)

