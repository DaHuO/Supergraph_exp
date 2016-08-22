import sys

def lastWord ( inputString ):
    results = []
    outputString = inputString[0]

    for i in range(1, len(inputString)):
        intermediateString = sorted([outputString + inputString[i], inputString[i] + outputString ])
        outputString = intermediateString[1]

    return outputString

numTests = input()

for i in range (0, int(numTests)):
    print ("Case #" + str(i+1) +": " + str(lastWord(input())))
