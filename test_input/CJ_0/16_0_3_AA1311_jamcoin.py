import sys
import os

def input(inputfile):
	"""
	Returns a dictionary
	"""
	f = open(inputfile)
	T = f.readline()
	JC = []
	try:
		for i in range(int(T)):
			NJ = f.readline().split(" ")
			NJ[0] = int(NJ[0])
			NJ[1] = int(NJ[1])
			JC.append(NJ)
		f.close()
		return JC
	except Exception:
		return False

def output(jamcoins, filename):
	f = open(filename, 'w')
	count = 1
	for i in jamcoins:
		# each i is a test case result
		case = "Case #" + str(count) + ':\n'
		f.write(case)
		for j in range(1, i[0]+1):
			# i[1] is the jamcoins dictionary
			# i[1][key1] is a LIST having first jamcoin followed by proofs!
			for k in i[1][j]:
				f.write(str(k) + ' ')
			f.write("\n")
		count += 1
	f.close()


def main():
	"""
	result = [[J, list2], [J, list2], ...]

	"""
	
	# l = permute(16)
	# print l

	
	JC = input(sys.argv[1])
	# print JC
	result = []
	for i in range(len(JC)):
		result.append(findJamcoins(JC[i][0], JC[i][1]))

	# print result
	output(result, sys.argv[2])
	

def findJamcoins(N, J):
	"""
		Will be called for T times from main()
		dict: {1: [J1, p1, p2, p3, p4, p5, p6, p7, p8, p9],
				2: [J2, p1, p2, p3, p4, p5, p6, p7, p8, p9],	
				.... }
		Returns the result of the test case passed: [J, dict]
	"""

	returnList = []
	returnDict = {}

	permutes = permute(N)
	#permutes = [1001, 1011, 1101, 1111]
	# permute 1..1 => (N-2) P (2)
	# for loop for all permutes
	bases = [2,3,4,5,6,7,8,9,10]
	count = 1
	for i in permutes:
		is_jamcoin = True
		proofs = []
		for j in bases:
			# print 'base = ', j, '\n'
			# print 'calling convert base to decimal'
			decnum = convertbase_to_decimal(j, i)
			# print 'calling to check prime'
			checkPrime = isprime(decnum)
			# checkPrime = check_if_prime(decnum)
			if(checkPrime[0] == True):
				proofs.append(checkPrime[1])
				continue
			else:
				# failed as a jamcoin because for the present base it is a prime in decimal
				is_jamcoin = False
				break
		if(is_jamcoin):
			# add to return result
			tempList = [i] + proofs
			returnDict[count] = tempList
			if(count == J):
				return [J, returnDict]
			count += 1

def isprime(n):
    if n == 2:
        return [False, 0]
    if n == 3:
        return [False, 0]
    if n % 2 == 0:
        return [True, 2]
    if n % 3 == 0:
        return [True, 3]

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return [True, i]

        i += w
        w = 6 - w

    return [False, 0]

def convertbase_to_decimal(base, num):
	"""
	Takes in an numeric (int) value. This will be interpreted by base and returned its decimal value
	"""

	decEq = 0
	mult = 0
	y = str(num)
	for i in range(len(y)-1, -1, -1):
		decEq += (int(y[i])) * (base**mult)
		mult += 1
	return decEq

# def check_if_prime(decnum):
# 	"""
# 	Returns a list[True, proof] if NOT PRIME or [False, 0] if PRIME
# 	"""

# 	for i in range(2, decnum-1):
# 		if(decnum%i == 0):
# 			return [True, i]
#  	return [False, 0]

# def factorial(n):
# 	if(n==1):
# 		return 1
# 	else:
# 		return n*factorial(n-1)

def permute(n):
	"""
	Inputs the number of digits without the front and end 1's
	Returns a list of all permutations (with 1 in the front and end)
	"""

	na = n-2
	numbers = []
	num = bin(0)
	maxnum = '0b' + ('1' * na)
	
	# int vals
	num = int(num, 2)
	maxnum = int(maxnum, 2)

	while(True):
		if(num<=maxnum):
			numbers.append(bin(num))
			num += 1
		else:
			break;

	for i in range(len(numbers)):
		x = numbers[i]
		x = x.split('0b')
		y = x[1]
		# add leading zeroes
		diff = na - len(y)
		y = ('0' * diff) + y
		y = '1' + y + '1'
		numbers[i] = y

	return numbers


main()
