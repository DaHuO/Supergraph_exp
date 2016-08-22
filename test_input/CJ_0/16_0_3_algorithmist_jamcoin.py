import itertools

#@param number - int type
#@return -1 if prime, trivial divisor if not prime
def isPrime(number):
	squareFloor = int(number ** 0.5)
	retVal = -1
	for divisor in range(2, squareFloor + 1):
		if number % divisor == 0:
			retVal = divisor
			break
	return retVal

def convertToBase(value, base):
	retValSum = 0
	power = 0
	for i in range(len(value) - 1, -1, -1):
		retValSum += (base ** power) * value[i]
		power += 1
	return retValSum

def main():
	inputFile = open('C-small-attempt0.in', 'r')
	outputFile = open('jcOutput.txt', 'w')
	cases = inputFile.readline().strip()
	params = [int(x) for x in inputFile.readline().strip().split()]
	N = params[0]
	J = params[1]
	
	NStripped = N - 2
	iterator = itertools.product([0, 1], repeat=NStripped)
	validJamcoins = {}
	numValidJamcoins = 0
	for value in iterator:
		value = [1] + list(value) + [1]
		divisors = []
		for base in range(2, 11):
			convertedValue = convertToBase(value, base)
			trivialDivisor = isPrime(convertedValue)
			if trivialDivisor == -1:
				break
			else:
				divisors.append(trivialDivisor)
		if len(divisors) < 9:
			continue #this permutation failed, get the next potential jamcoin permutation
		validJamcoins[''.join([str(x) for x in value])] = divisors
		print('Jamcoin saved!')
		numValidJamcoins += 1
		if numValidJamcoins == J:
			break
	outputFile.write('Case #1: \n')
	for jamcoin in validJamcoins:
		outputFile.write(jamcoin + ' ')
		for divisor in validJamcoins[jamcoin]:
			outputFile.write(str(divisor) + ' ')
		outputFile.write('\n')

main()