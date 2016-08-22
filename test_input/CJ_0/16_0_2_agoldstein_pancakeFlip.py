import string

inputString = string.split(open("pancakes.in", "r").read(),"\n")

outputFile = open("pancakes.out", "w")

numTests = int(inputString.pop(0))

def printStack(pancakeList):
	printString = ""
	for pancake in pancakeList:
		if pancake:
			printString += "+"
		else:
			printString +=  "-"
	print printString



def recursivePancaking(pancakeList):
	if sum(pancakeList) == len(pancakeList):
		return 0
	elif sum(pancakeList) == 0:
		return 1

	else:
		bestFlips = 100000

		for i in range(1,len(pancakeList)):

			# rules for flipping
				# flips can only help if they line up more consecutive pancakes than previous
					# flipped pancake must be different side as one after, and same side as one above 

			if pancakeList[i-1] == pancakeList[0] and pancakeList[i-1] != pancakeList[i]:
				flippedCakes = flip(pancakeList,i)
				# printStack(flippedCakes)
				numFlips = recursivePancaking(flippedCakes)
				if numFlips < bestFlips:
					bestFlips = numFlips
	return bestFlips + 1



def realFastPancaking(pancakeList):

	switchCount = 0

	prevPancake = pancakeList[0]

	for pancake in pancakeList:
		if pancake != prevPancake:
			switchCount += 1
		prevPancake = pancake

	if switchCount == 0:
		return 1 - pancakeList[0]

	if pancakeList[-1] == 1:
		switchCount -= 1

	return switchCount + 1


def flip(pancakeList,toFlip):
	counter = 0
	flippedList = []

	for counter in range(len(pancakeList)):
		if counter < toFlip:
			flippedList.append(not pancakeList[toFlip-counter-1])
		else:		
			flippedList.append(pancakeList[counter])

	return flippedList



for testNum in range(1,numTests+1):

	pancakeList = [(pancake == "+") for pancake in inputString.pop(0)]

	printStack(pancakeList)
	numFlips =  realFastPancaking(pancakeList)


	outputFile.write("case #" + str(testNum) + ": " + str(numFlips) + "\n")




