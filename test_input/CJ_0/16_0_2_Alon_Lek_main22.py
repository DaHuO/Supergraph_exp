
def getLines(filename):
    with open(filename) as f:
        return f.readlines()


def appendToFile(filename, text):
    with open(filename,'a') as f:
        f.write(text + '\n')


def checkLine(line, size):
    for i in xrange(0,size):
        if line[i] == '-':
            return False
    return True

def getNumWithSuchSize(size):
    s = ""
    for i in xrange(0,size):
        s+= '1'

    return int(s,2)

def getAppropriateNum(start1s, size):
    s = ""
    for i in xrange(0,size):
        if i <= start1s:
            s += '1'
        else:
            s += '0'

    return int(s,2)

def getNumOfStarting1s(num):
    counter = 0
    while num != 0:
        if num%2 == 0:
            return counter
        counter += 1
        num /= 2
    return counter

def findTimes(num, size):
    possibleNums = [(num,0)]
    while True:
        curNumTuple = possibleNums[0]
        possibleNums.remove(curNumTuple)
        if curNumTuple[0] == getNumWithSuchSize(size):
            return curNumTuple[1]

        numOfStarting1s = getNumOfStarting1s(curNumTuple[0])
        for i in xrange(0,size - numOfStarting1s):
            num2 = curNumTuple[0] ^ getAppropriateNum(i, size)
            possibleNums.append((num2,curNumTuple[1]+1 ))


def convertToBinary(line):
    s = ""
    for i in xrange(0,len(line)):

        if line[i] == '+':
            s+= '1'
        if line[i] == '-':
            s+= '0'
    return s


def removeHeading1s(binString):
    s = ""
    flag = 0
    for i in xrange(len(binString)-1, -1, -1):
        if flag == 0 and binString[i] == '1':
            continue
        flag = 1
        s+= binString[i]

    return s[::-1]

lines = getLines('B-large.in')
testsNum = int(lines[0])

for lineNum in xrange(1,testsNum + 1):
    line = lines[lineNum]
    line = line.replace('\n','')
    size = len(line)

    cur = line[0]
    counter = 0
    for i in xrange(0,size):
        if line[i] != cur:
            cur = line[i]
            counter += 1

    if line[i] == '-':
        counter += 1
    appendToFile('output4.txt', "Case #"+str(lineNum) + ": " + str(counter))



