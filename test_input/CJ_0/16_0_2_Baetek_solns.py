def main(inputs):
	if baseCasePos(inputs):
		return 0
	if baseCaseNeg(inputs):
		return 1
	invert = {"+":"-","-":"+"}
	initVar = inputs
	flipCounter = 1
	while 1:
		initChar = initVar[0]
		fI = initVar[1:].index(invert[initChar]) + 1
		initVar = ((fI) * invert[initChar]) + initVar[fI:]
		if baseCasePos(initVar):
			return flipCounter
		if baseCaseNeg(initVar):
			return flipCounter + 1
		flipCounter += 1

def baseCasePos(inputs):
	if "-" not in inputs:
		return True

def baseCaseNeg(inputs):
	if "+" not in inputs:
		return True

def fileHandler(inName):
	returnString = ""
	f = open(inName,'r')
	i = 1
	init = True
	for line in f:
		if init == True:
			init = False
			continue
		returnString += "Case #" + str(i) + ": " + str(main(line[:-1])) + "\n"
		i += 1
	f.close()
	w = open('results.txt','w')
	w.write(returnString)
	w.close()

fileHandler("B-large.in")