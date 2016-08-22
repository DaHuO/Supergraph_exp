# Google Code Jam Qualification Round - Problem B
def getFiles(name):
    return open(name + '.in', 'r'), open(name + '.out', 'w')

name = 'example'
name = 'B-small-attempt0'
name = 'B-large'

inFile, outFile = getFiles(name)

def getValue(S):
    count = 0

    happyChar = '+'
    for symbol in reversed(S[:-1]):
        if symbol != happyChar:
            happyChar = symbol
            count += 1

    return str(count)

# Number of test cases
T = int(inFile.readline())

# Read in each row
for counter in range(T):
    line = inFile.readline()
    if line != '':
        outFile.write("Case #" + str(counter + 1) + ": " + getValue(line) + "\n")

inFile.close()
outFile.close()
