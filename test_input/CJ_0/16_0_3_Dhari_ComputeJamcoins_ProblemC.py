import sys
import os
import itertools
from math import pow

def IsDivisibleAsExpected(jamcoinStr):

    divisorBaseMap = {2:3,3:2,4:5,5:2,6:7,7:2,8:3,9:2,10:11}
    
    for base in range(2,11):
        currValue = 0
        for c in jamcoinStr:
            currValue = base*currValue + int(c)
        if currValue % divisorBaseMap[base] != 0:
            return False
    return True
    
#Produces jamcoins by the idea that any string with equal number of 1s and 0s in odd and even indices would be a legitimate jamcoin
def PrintJamCoins(N,J):

    evenIndicesSet = set(range(2,N-1,2))
    oddIndicesSet = set(range(1,N-1,2))

    if N%2 == 0:
        evenSubsetSize = 0
        oddSubsetSize = 0
    else:
        evenSubsetSize = 0
        oddSubsetSize = 2
    
    producedCoinCount = 0
    
    while producedCoinCount < J and evenSubsetSize <= len(evenIndicesSet):
        #evenSubsetIterator = itertools.combinations(evenIndicesSet,evenSubsetSize)
        #oddSubsetIterator = itertools.combinations(oddIndicesSet,oddSubsetSize)
        for evenSubset in itertools.combinations(evenIndicesSet,evenSubsetSize):
            for oddSubset in itertools.combinations(oddIndicesSet,oddSubsetSize):
                currSet = set(evenSubset).union(set(oddSubset).union(set([0,N-1])))
                currJamCoinAsList = ["0"]*N
                for index in currSet:
                    currJamCoinAsList[N-1-index] = "1"
                print "%s 3 2 5 2 7 2 3 2 11"%("".join(currJamCoinAsList))
                if not IsDivisibleAsExpected("".join(currJamCoinAsList)):
                    print "ERROR !! Jam coin not divisible as expected !! Exiting !"
                    sys.exit(-1)

                producedCoinCount += 1
                if producedCoinCount >= J:
                    break
            if producedCoinCount >= J:
                break
        evenSubsetSize += 1
        oddSubsetSize += 1
                    
def main():
    T = int(raw_input())
    for testno in xrange(1,T+1):
        N,J = [int(s) for s in raw_input().split(" ")]
        print "Case #%d:"%testno
        PrintJamCoins(N,J)

if __name__ == "__main__":
    main()
        
    
