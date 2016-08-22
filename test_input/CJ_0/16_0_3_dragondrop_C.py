#!/usr/bin/python
import sys
import math

def main( argv ):
	infile = open(argv[1], 'r')
	outfile = open('output.txt', 'w')
	cases = int(infile.readline())
	for case in range(1, cases+1):
		int_list = [int(i) for i in infile.readline().split(" ")]
		length = int_list[0]
		numCoins = int_list[1]
		coins = getCoins(numCoins, length)
		print("Case #" + str(case) + ":\n" + coins, file=outfile)


def getCoins(numCoins, length):
	output = []
	coinsList = getPossibleCoins(length)
	for coin in coinsList:
		coinFound = 1
		coinProof = coin
		bases = baseList(int(coin))
		for base in bases:
			divisor = getDivisor(base)
			if (divisor == -1):
				coinFound = False
				break
			else:
				coinProof = coinProof + " " + str(divisor)
		if coinFound:
			numCoins -= 1
			output.append(coinProof)
			if numCoins == 0:
				break
	return '\n'.join(output)

def getPossibleCoins(length):
	coinList = []
	coin = '1'
	coinList.append(coin)
	for i in range(length-2):
		newList = []
		for c in coinList:
			newList.append(c + '0')
			newList.append(c + '1')
		coinList = newList
	coinList = [x + '1' for x in coinList]
	return coinList

def generateNextCoin(jamCoin):
	for i in range(0, len(jamCoin)-1):
		if jamCoin[i] == 0:
			jamCoin[i] = 1
			break
	return jamCoin

def baseList(num):
	numString = str(num)
	result = []
	for base in range(2, 11):
		result.append(int(numString, base))
	return result

def getDivisor(num):
	if (num % 2 == 0):
		return 2
	for divisor in range (3, int(math.sqrt(num)) + 1, 2):
		if (num % divisor == 0):
			return divisor
	return -1

if __name__ == "__main__":
    main(sys.argv)