import sys
NUM_OF_ATTEMPTS = 1000
DIGITS_REQUIRED = 10
#sys.setrecursionlimit(100)
DEBUG = 0
def getDigits(num):
    return list(map(int,str(num)))

def simplify(states):
    newStates = [states[0]]
    lastState = states[0]
    for state in states:
        if state == lastState:
            continue
        lastState = state
        newStates.append(state)
    return newStates

cacheDict = {}
def solveCase(states, depth = 0):
    states = trimFalse(simplify(states))
    tag = len(states) * (1 if states[0] else -1)
    if tag in cacheDict:
        return cacheDict[tag]
    DEBUG and print(depth*" " + "Working on: " + repr(states))
    if len(states) == 0:
        return 0
    if all(states):
        return 0
    if not any(states):
        return 1
    if len(states) == 1:
        return 0 if states[0] else 1

    tries = []
    for i in range(1, len(states)):
        DEBUG and print(depth*" " + "Flipping %d" % i)
        if i % 2 == 0:
            continue
        tries.append(solveCase(flip(states[:i]) + states[i:], depth + 1))
    bestRes = min(tries) + 1
    cacheDict[tag] = min(tries) + 1
    return bestRes

def findFirstTrue(states):
    for (i, state) in enumerate(reversed(states)):
        if state:
            return i
    return False

def trimFalse(states):
    for (i, state) in enumerate(reversed(states)):
        if not state:
            break
    return states[:-i] if i > 0 else states

def toggle(boolVal):
    return not boolVal

def flip(boolArr):
    return list(reversed(list(map(toggle, boolArr))))


def parseInput(text):
    cases = []
    for i, line in enumerate(text.splitlines()):
        if i == 0:
            continue
        line = line.strip()
        isHappy =  lambda x: x == "+"
        num = list(map(isHappy,str(line)))
        cases.append(num)
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
    print(output)
    with open(outFile, "w") as h:
        h.write(output)
    
