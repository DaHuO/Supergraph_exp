def lastWord(inputStr):
	resultWord = inputStr[0]
	inputLen = len(inputStr)
	for i in range(1, inputLen):
		if inputStr[i] >= resultWord[0]:
			resultWord = inputStr[i] + resultWord
		else:
			resultWord = resultWord + inputStr[i]


	return resultWord








if __name__ == "__main__":
	inputfile = open('A-large.in').read().split('\n')
	filehandler = open('large.out', 'w')

	inputLen = len(inputfile)

	currentLine = 1
	currentRound = 1
	casesNum = int(inputfile[0])
	while currentLine <= inputLen - 1:
		if len(inputfile[currentLine]) == 0:
			break
		#print len(inputfile[currentLine])
		inputStr = inputfile[currentLine]
		outputStr = lastWord(inputStr)

		print 'Case #%s: %s' % (currentRound, outputStr)
		filehandler.write('Case #%s: %s\n' % (currentRound, outputStr))
		currentRound += 1
		currentLine += 1
	filehandler.close()






	# filehandler = open('A-big-practice.out', 'w')
	# casesNum = int(raw_input())
	# for i in range(casesNum):
	# 	valueSum = int(raw_input())
	# 	itemNum = int(raw_input())

	# 	itemList = raw_input()
	# 	itemList = itemList.split()
	# 	itemList = map(int, itemList)
	# 	# for j in range(itemNum):
	# 	# 	tmpValue = int(raw_input())
	# 	# 	itemList.append(tmpValue)
	# 	index1, index2 = findTwo(valueSum, itemList)
	# 	print 'Case #%s: %s %s' % (i+1, index1, index2)
	# 	filehandler.write('Case #%s: %s %s\n' % (i+1, index1, index2))
	# filehandler.close()

