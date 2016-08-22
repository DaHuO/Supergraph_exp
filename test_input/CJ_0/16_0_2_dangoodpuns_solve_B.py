# Problem B for Code Jam 2016
# Dan Elliott
# Run with Python 2.7

#Remember to set these flags to False before submitting
IoDebug = False #Check file input on sample file
solveDebug = False #Run hard-coded test cases
debug = True #print debug lines


runMain = True #turn to False when developing solution

def printToFile(fout,line):
    #if debug: print line
    fout.write(line+'\n')

def readInputFile(filename, linesPerTestCase = 1):
    testCases = []
    fin = open(filename)
    lines = fin.read().splitlines()
    fin.close()
    numCases = int(lines[0])
    line = 1
    #if debug: print 'numCases',numCases
    for i in range(0,numCases):
        testCase = []
        for j in range(line,line+linesPerTestCase):
            testCase.append(lines[j])
        line += linesPerTestCase
        testCases.append(testCase)
    return testCases

def isSolved(pancakes):
    return pancakes.count('-') == 0

def opposite(pancake):
    return '+' if pancake == '-' else '-'

def highestIndexDash(pancakes):
    return len(pancakes)-1 - list(reversed(pancakes)).index('-')

def flip(pancakes,index):
    #pancakes[index] = opposite(pancakes[index])
    sublist = list(reversed(pancakes[0:index+1]))
    for i in range(0,index+1):
        pancakes[i] = opposite(sublist[i])

def solve(pancakes):
    #N = len(pancakes)
    flips = 0
    while not isSolved(pancakes):
        if pancakes[0] == '+':
            index = pancakes.index('-') - 1
            #pancakes[0] = opposite(pancakes[0])
            flip(pancakes,index)
            flips += 1
        else:
            index = highestIndexDash(pancakes)
            flip(pancakes,index)
            flips += 1
        #if debug: print pancakes
    return flips


def main():
    filename = 'B-large.in'
    linesPerTestCase = 1
    testCases = readInputFile(filename,linesPerTestCase)
    fout = open('out.txt','w')
    curTestCase = 1
    for testCase in testCases:
        #if debug:
        #    print 'curTestCase',curTestCase
        #parse testCase
        result = solve(list(testCase[0]))
        print 'Case #'+str(curTestCase)+': ',str(result)
        printToFile(fout,'Case #'+str(curTestCase)+': '+str(result))
##        if result == True:
##            printToFile(fout,'Case #'+str(curTestCase)+':'+str(result))
##            print 'Case #'+str(curTestCase)+':',str(result)
##        else:
##            printToFile(fout,'Case #'+str(curTestCase)+':'+str(result))
##            print 'Case #'+str(curTestCase)+':',str(result)
        curTestCase +=1
    fout.close()


## RUN FULL SOLUTION ##
if runMain:
    #if debug: print 'run main'
    main()

## TEST EXAMPLE CASES ##
if solveDebug:
    #if debug: print 'solve examples'
    #print solve(['-']) #
    #print solve(['-','+']) #
    #print solve(['+','-']) #
    #print solve(list('+++')) #
    #print solve(list('--+-')) #
    for i in range(0,101):
        print solve(list('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+'))

## TEST AREA ##
if IoDebug:
    testCases = readInputFile('sample.txt',2)
    print testCases

