from sys import stdin
from operator import add
import random
def isPrime(number):
    if (number > 1):
        for time in range(3):
            randomNumber = random.randint(2, number)-1
            if ( pow(randomNumber, number-1, number) != 1 ):
                return False
        
        return True
    else:
        ''' case number == 1 '''
        return False
def isValid(A):
	for number in A:
		if isPrime(number):
			return False
	return True
# A = [55, 337, 1301, 3781, 9115, 19265, 36937, 65701, 110111]
# B = [51, 328, 1285, 3756, 9079, 19216, 36873, 65620, 110011]
for _t in range(1,int(stdin.next().strip())+1):
	N,J = (int(x) for x in stdin.next().split())
	# print N,J
	coins = []
	#N = 4
	for i in xrange(pow(2,N-1),pow(2,N)):
		temp =  bin(i)[2:]
		if temp.endswith('1'):
			coins.append(temp)
	final = [];index = 0
	while len(final) < J:
	# for i in range(10):
		values = []
		for base in xrange(2,11):
			values.append(int(coins[index],base))
		if isValid(values):
			outL = []
			for num in values:
				for factor in xrange(2,num/2):
					if num % factor == 0:
						outL.append(factor)
						break
			final.append((coins[index],outL))
			index += 1
		index += 1
	print "Case #"+str(_t)+":"
	for i in final:
		print i[0],
		for j in i[1]:
			print j,
		print