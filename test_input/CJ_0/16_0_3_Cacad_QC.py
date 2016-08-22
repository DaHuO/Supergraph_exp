#infile = open("input.txt", "r")
outfile = open("output.txt", "w")

def findBase(base, num, n):
    result = 0
    mult = 1
    for i in range (n):
        result += mult * num[n-1-i]
        mult *= base
    return result
        
def printResult(num, primeDiv, n):
    for i in range (n):
        print(str(num[i]), end='')
    for i in range (2, 11, 1):
        print(" ", end='')
        print(str(primeDiv[i]), end='')
    print('')

def printToFile(num, primveDiv, n):
    for i in range (n):
        outfile.write(str(num[i]))
    for i in range (2, 11, 1):
        outfile.write(" ")
        outfile.write(str(primeDiv[i]))
    outfile.write("\n")

def findPrime(num):
    maxDiv = min(num, 10000)
    for i in range (3, maxDiv, 2):
        if (num%i == 0):
            return i
        
    return -1
        
        
    
n = 32
j = 500

a = [0 for i in range (n)]
a[n-1] = 1
a[0] = 1

count = 0
numBase = 0

while(count < j):
    for i in range (2, n, 1):
        if(a[n-i] == 0):
            a[n-i] = 1
            break
        a[n-i] = 0
    isPrime = False
    primeDiv = [0 for i in range(11)]
    for i in range (2, 11, 1):
        numBase = findBase(i, a, n)
        primeDiv[i] = findPrime(numBase)
        if(primeDiv[i] == -1):
            isPrime = True
            break
    if (isPrime):
        continue
    #printResult(a, primeDiv, n)
    printToFile(a, primeDiv, n)
    print(str(count))
    count += 1

outfile.close()        
