NUM_OF_ATTEMPTS = 1000
DIGITS_REQUIRED = 10

def getDigits(num):
    return list(map(int,str(num)))

solved = {}

def cSolveCase(letters):
    if tuple(letters) in solved:
        return solved[letters]
    
def solveCase(letters):
    #print("Got: %s" % (''.join(letters),))
    word = letters[0]
    for letter in letters[1:]:
        if letter >= word[0]:
            word = letter + word
        else:
            word = word + letter
    return word
    #if not found:
    #    print("### Num %d with %d steps, ### CAN'T FIND ###" % (num, i))





def parseInput(text):
    cases = []
    for i, line in enumerate(text.splitlines()):
        if i == 0:
            continue
        line = line.strip()
        letters = list(line)
        cases.append(letters)
    return cases


def getCases(filename):
    with open(filename) as h:
        data = h.read()
    return parseInput(data)


def getOutput(solved):
    lines = []
    for i, solvedCase in enumerate(solved):
        lines.append("Case #%d: %s" % (i + 1, solvedCase))
    return '\n'.join(lines)

def generateOutput(filename, outFile = None):
    cases = getCases(filename)
    solvedCases = [solveCase(case) for case in cases]
    output = getOutput(solvedCases)
    if outFile == None:
        outFile = filename[:-2] + "out"
    with open(outFile, "w") as h:
        h.write(output)
    
