import math
import fractions

inFilePath =  'C:\\Users\\Orr\\Desktop\\CodeJam\\1A\\A-large.in'
outFilePath = 'C:\\Users\\Orr\\Desktop\\CodeJam\\1A\\A-large.out'
seperator = ' '

def parseFile(inFileName):
    inFile = open(inFileName)
    T = parseNum(inFile.readline())
    ProblemArr = []
    for k in range(T):
        S = inFile.readline()[:-1]
        ProblemArr.append(ProblemSet(S))
    inFile.close()
    return ProblemArr


class ProblemSet():
    def __init__(self,S):
        self.S = S

def solvePS(ps):
    s = ps.S
    n = ''
    for i in range(len(s)):
        if len(n) == 0 or n[0] > s[i]:
            n = n + s[i]
        else:
            n = s[i] +n
    return n
    
   
def parseNum(line):
    return int(line)

def parseVec(line):
    vecValues = line.split(seperator)
    return [int(value) for value in vecValues]

def psOutFormat(iterNum,res):
    return 'Case #{0}: {1}\n'.format(iterNum+1,res)
        
def writeToFile(results,outFileStr):
    outFile = open(outFileStr,'w')
    try:
        resultArr = [psOutFormat(i,results[i]) for i in range(len(results))]
        outFile.writelines(resultArr)
    finally:
        outFile.close()
    
def solveProblemSet():
    ps = parseFile(inFilePath)
    results = []
    for i in range(len(ps)):
        results.append(solvePS(ps[i]))
    writeToFile(results,outFilePath)
    print('done!')


solveProblemSet()
#ps = ProblemSet([24,97,2])
#print(solvePS(ps))
