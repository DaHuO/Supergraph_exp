def pancakes(sequence):
    count = 0
    sequenceLen = len(sequence)
    for i in range(0, sequenceLen - 1):
        if cmp(sequence[i], sequence[i + 1]):
            count += 1

    if sequence[sequenceLen - 1] == '-':
        count += 1

    return count


def execute(testCase):
    for i in range(0, testCase.__len__()):
        result = pancakes(testCase[i])
        print "Case #" + str(i + 1) + ": " + str(result) + "\n"


if __name__ == '__main__':
    import sys

    inputFile = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            inputFile = open(fn)
    testCount = int(inputFile.readline())
    testCase = []
    for i in range(0, testCount):
        inputLine = inputFile.readline()
        if inputLine[-1:] == '\n':
            testCase.append(inputLine[:-1])
        else:
            testCase.append(inputLine)
    inputFile.close()
    execute(testCase)
