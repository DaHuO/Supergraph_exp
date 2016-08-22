import sys
import math
import random

memPrimes=[]

def computeFirstMillionPrimes():
    testPrime = 2
    while(len(memPrimes) < 1000000):
        if prime(testPrime):
            memPrimes.append(testPrime)
        testPrime+=1

def convertFromBase(A, base):
    v = 0
    for i in xrange(len(A)-1,-1,-1):
        v+=(A[len(A)-1-i]*(base**i))
    return v

def prime(v):
    if(v==2 or v==3):
        return True
    val = math.ceil(math.sqrt(v))
    for i in xrange(0,len(memPrimes)):
        if v % memPrimes[i] == 0:
            return False
        if memPrimes[i] > val:
            break
    return True

def nextJamCoin(A):
    for i in xrange(len(A)-2,0,-1):
        if A[i]==0:
            A[i]=1
            break
        else:
            A[i]=0

def jamCoins(N,J):
    validJamCoins = []
    #initialize an array of size N as jam coin
    jamCoin = [0]*N
    jamCoin[0] = 1
    jamCoin[N-1] = 1
    isJamCoin = False
    while len(validJamCoins) < J:
        # get the number in the bases 2-10
        for i in xrange(2,11):
            val = convertFromBase(jamCoin,i)
            if(prime(val)):
                break
            if i==10:
                validJamCoins.append(list(jamCoin))
        # find next jam coin
        nextJamCoin(jamCoin)
    return validJamCoins

def computeDivisor(v):
    for i in xrange(2,100000000):
        if v%i == 0:
            return i

def printJamCoin(A):
    temp=[]
    for i in xrange(len(A)):
        temp.append(str(A[i]))
    print ''.join(temp),

if __name__ == "__main__":
    f = open(sys.argv[1], 'r')
    T = int(f.readline())
    computeFirstMillionPrimes()
    for i in xrange(1, T+1):
        [N, J] = f.readline().split()
        N = int(N)
        J = int(J)
        validJamCoins = jamCoins(N,J)
        print "Case #" + str(i) + ":"
        for jamCoin in validJamCoins:
            printJamCoin(jamCoin)
            for base in xrange(2,11):
                divisor = computeDivisor(convertFromBase(jamCoin,base))
                if base == 10:
                    print str(divisor)
                else:
                    print str(divisor),
    f.close()
