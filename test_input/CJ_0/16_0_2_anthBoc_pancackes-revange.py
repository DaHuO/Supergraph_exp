#Look over every pancake and check ther are all equal to char
def allSame(pancakes, char):
    for pancake in pancakes:
        if pancake != char:
            return False
    return True


#Gets string like "-+-+" in parameter that represents
#pancakes, and returns the index (exclude) to flip
#In --+ it will return 2, the index of first different pancake
#returns -1 if there is no flip needed
def getIndexToFlip(pancakes):
    i = 0
    firstChar = pancakes[0]
    pancakesSize = len(pancakes)

    if allSame(pancakes, '+'):
        return -1
    elif allSame(pancakes, '-'):
        return pancakesSize


    #Look over every pancake
    for pancake in pancakes:
        #If current char is not the last char and next char is different from
        #the current char, we have to flip
        if (i + 1 < pancakesSize and pancakes[i+1] != firstChar):
            return i+1
        i += 1
    return -1

#Does one flip with the pancakes,
def flip(pancakes, index):
    #If there is no need to flip, return pancakes
    if index == -1:
        return pancakes


    #Take substring to reverse, and reverse it
    subString = pancakes[:index]
    reversedSubString = subString[::-1]
    #Look over every char in the reversed substring, and turn + to - and - to +
    i = 0
    for char in reversedSubString:
        if char == '+':
            reversedSubString = reversedSubString[0:i] + '-' + (reversedSubString[i+1:] if i+1 < len(reversedSubString) else "")
        else:
            reversedSubString = reversedSubString[0:i] + '+' + (reversedSubString[i+1:] if i+1 < len(reversedSubString) else "")
        i += 1
    return reversedSubString + (pancakes[index:] if index < len(pancakes) else "")

#Count the necessary flips
def countFlips(pancakes):
    flipNumber = 0
    pancakesCopy = pancakes
    #While there is at least one flip to execute
    while getIndexToFlip(pancakesCopy) != -1:
        #Do the flip
        pancakesCopy = flip(pancakesCopy, getIndexToFlip(pancakesCopy))
        flipNumber += 1

    return flipNumber



def main():
    result = ""
    i = 1
    #Open the input file
    with open("B-large.in", 'r') as inputFile:
        testCasesNumber = inputFile.readline()
        #Read every case
        for pancakes in inputFile:
            pancakes = pancakes.replace("\n", "")
            result += "Case #" + str(i) + ": "  + str(countFlips(pancakes)) + '\n'
            i += 1
    #Write result
    with open("output.txt", 'w') as outputFile:
        outputFile.write(result)
main()
