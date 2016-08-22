import math
def isCoinJam(jamNum, primes):
	if(len(jamNum)<2):
		return False

	if(jamNum[0] != 1 or jamNum[-1] != 1):
		return False

	#generate numbers
	result = ''
	for base in range(2,11):
		count = len(jamNum)-1
		number = 0
		for x in jamNum:
			number += x*int(math.pow(base, count))
			count -= 1
		#check if prime
		isPrime = True
		for x in primes:
			if(x >= number):
				break
			if(number%x == 0):
				result += ' ' + str(x)
				isPrime = False
				break
		if(isPrime):
			return ''
	return result

def listOfPrimes(N):
	primeList = [2]
	for i in range(3,int(math.pow(2,N))):
		for x in primeList:
			if(i%x == 0):
				break
		primeList.append(i)
	return primeList


fileout = open('output.out', 'w')
filein = open('C-small-attempt0.in', 'r')

T = int(filein.readline()) #Number of cases
for i in range(T):
	temp = filein.readline().split(' ')
	N = int(temp[0])
	J = int(temp[1])
	primes = listOfPrimes(N)
	fileout.write('Case #'+str(i+1)+':\n')
	count = 0;
	while(J>0):
		temp = str(bin(count))
		temp = (temp[2::]).strip()
		temp = temp.zfill(N-2)
		Num = list(temp)
		for h in range(len(Num)):
			Num[h] = int(Num[h])
		print(Num)

		jamNum = [1]+Num+[1];
		x = isCoinJam(jamNum, primes)
		if(x):
			J -= 1
			for y in range(len(jamNum)):
				jamNum[y] = str(jamNum[y])
			z = ''.join(jamNum)
			fileout.write(z+str(x)+'\n')
		count += 1


