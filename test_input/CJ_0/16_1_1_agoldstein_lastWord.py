import string

inputString = string.split(open("words.in", "r").read(),"\n")
outputFile = open("words.out", "w")
numTests = int(inputString.pop(0))

def recursiveTry(lettersLeft,word):
	if lettersLeft == "":
		return word
	else:
		before = recursiveTry(lettersLeft[1:], lettersLeft[0] + word)
		after  = recursiveTry(lettersLeft[1:], word + lettersLeft[0])
		return max(before, after)


for testNum in range(1,numTests+1):

	bestWord = recursiveTry(inputString.pop(0),"")
	outputFile.write("case #" + str(testNum) + ": " + bestWord + "\n")
