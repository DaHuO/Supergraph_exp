import logging
import sys
import math

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

def getDivisor(n):
    for i in range(2,int(math.sqrt(n))):
        if n % i ==0:
            return i
        
    return None

def baseConvert(binStr, base):
    p = 1
    s = 0
    for i in binStr[::-1]:
        s += p * int(i)
        p *= base
    return s

def checkJamCode(binStr):
    resultList = [0] * 10
    resultList[0] = binStr

    for i in range(2,11):
        n = baseConvert(binStr, i)
        d = getDivisor(n) 
        if d  == None:
            return None
        resultList[i-1] = d
        
    #return None
    return resultList

def solve(n,j):
    num = int(math.pow(2,n-1)) + 1
    jamCount = 0
    
    while jamCount < j:
        binStr = bin(num)[2:]
        re = checkJamCode(binStr)
        
        if re != None:
            jamCount += 1
            
            print(" ".join(str(x) for x in re))
            
        num += 2 
    
    
def main():
    t = int(input())

    line = input().split()
    line = list(map(int, line))
    n,j = line[0], line[1]
    
    print("Case #1:")
    solve(n,j)
    
        
def log(*message):
    logging.debug(*message)
    #print(*message)
    
if __name__ == "__main__":
    main()
