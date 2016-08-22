# Problem C for Code Jam 2016
# Dan Elliott
# Run with Python 2.7

#Remember to set these flags to False before submitting
IoDebug = False #Check file input on sample file
solveDebug = False#True #Run hard-coded test cases
debug = True #print debug lines


runMain = True #turn to False when developing solution
primes = {}
if False:
    for line in open('primes1.txt'):
        p = line.split()
        for e in p:
            primes[int(e)] = True

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

def coin_tobase_k(jcoin,k,N):
    total = 0
    for i in range(0,N+1):
        if 1<<i&jcoin > 0:
            total+= k**i
    return total

def findFactor(p, limit):
    candidate = 3
    while candidate <= limit:
        if p%candidate == 0:
            return (True, candidate)
        else:
            candidate+=2
    return (False, 0)



# N = Length of jamcoin string
# J = Number of required minimum instances to prove
def solve(N,J):
    jcoin = (1 << (N-1)) + 1
    # populate prime dictionary
    successes, attempts = 0,0
    lim = 2**(N-1) # in case we screw up and don't find enough
    #sLim = (2**N)**0.5
    finalResults = []
    #print 'start solve'
    #print 'initial jcoin: ',jcoin
    while successes < J and attempts < lim:
        tobases = [coin_tobase_k(jcoin,k,N) for k in range(2,11)]
        proofs = []
        # if none of tobases is prime ..., find factor of each element
        i = 2
        failed = False
        #while i<=10 and not failed: #check primes
        #    if tobases[i-2] in primes:
        #               print '*********found prime',tobases[i-2]
        #               failed = True
        #    i+=1
        i = 2
        while i<=10 and not failed: #find factors
            res = findFactor(tobases[i-2],int(tobases[i-2]**0.5)+1)
            if res[0] == True:
                proofs.append(res[1])
            else:
                failed = True
            i+=1
        if not failed:
            #print 'jcoin',jcoin
            #print 'tobases: ',tobases
            #print 'proofs: ',proofs
            finalResults.append([jcoin,proofs])
            successes +=1
        jcoin += 2
        attempts += 1
    #if attempts == lim: print 'you have a bug'
    return finalResults

def jcoinToStr(jcoin,N):
    s = []
    for i in range(0,N):
        if (1<<i & jcoin) > 0:
            s.append('1')
        else:
            s.append('0')
    st = ''.join(list(reversed(s)))
    return st

def resultLineToStr(resultList,N):
    jcoin = jcoinToStr(resultList[0],N)
    r = str(jcoin) + ' '
    for e in resultList[1]:
        r += str(e) + ' '
    return r

def main():
    filename = 'C-small-attempt0.in'
    linesPerTestCase = 1
    testCases = readInputFile(filename,linesPerTestCase)
    fout = open('out.txt','w')
    curTestCase = 1
    ins = testCases[0][0].split()
    N = int(ins[0])
    J = int(ins[1])
    resultRaw = solve(N,J)
    print 'Case #'+str(curTestCase)+':'
    printToFile(fout,'Case #'+str(curTestCase)+':')
    for res in resultRaw:
        result = resultLineToStr(res,N)
        print result
        printToFile(fout,result)
    fout.close()


## RUN FULL SOLUTION ##
if runMain:
    #if debug: print 'run main'
    main()

## TEST EXAMPLE CASES ##
if solveDebug:
    result = solve(6,3)
    for res in result:
        print 'Case #'+str(0)+': '+resultLineToStr(res,6)
    #result = solve(16,50)
    #if debug: print 'solve examples'
    #print solve(['-']) #
    #print solve(['-','+']) #
    #print solve(['+','-']) #
    #print solve(list('+++')) #
    #print solve(list('--+-')) #
    #for i in range(0,101):
    #    print solve(list('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+'))

## TEST AREA ##
if IoDebug:
    testCases = readInputFile('sample.txt',2)
    print testCases

