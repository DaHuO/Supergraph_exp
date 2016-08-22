import sys
import random

def base(binary, i):
    return sum([binary[j]*(i**(len(binary)-j-1)) for j in range(len(binary))])
    
def isPrime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return i
    return -1

def notPrime(binary):
    theFactors = []
    for i in range(2,11):
        num = base(binary, i)
        divisor = isPrime(num)
        if divisor==-1:
            return []
        else:
            theFactors += [divisor]
    return theFactors

inFileName = sys.argv[1]
outFileName = sys.argv[2]

inFile = open(inFileName,'r')
outFile = open(outFileName,'w')


caseNums = int(inFile.readline().strip("\n"))
case = 0
for line in inFile:
    case += 1
    N, J = [int(i) for i in line.strip('\n').split(' ')]
    outFile.write("Case #{}:\n".format(case))
    valid = []
    binary = [1]+[int(random.random() > 0.5) for i in range(N-2)]+[1]
    factors = notPrime(binary)

    while (len(valid)<J):

        if ( not (binary in valid) and len(factors)==9):
            num = ''.join([str(i) for i in binary]) + " "
            for i in factors:
                num += str(i)+" "
            num = num.strip(' ')+'\n'
            outFile.write(num)
            valid += [binary]
        
        binary = [1]+[int(random.random() > 0.5) for i in range(N-2)]+[1]
        factors = notPrime(binary)

        
            

    

inFile.close()
outFile.close()
            
