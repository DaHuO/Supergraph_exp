from math import sqrt; from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def arrFromBase(arr, base):
    num = 0
    size = len(arr)
    for i in range(size):
        power = size - 1 - i
        num += arr[i]*base**(power)
    #print(arr)
    #print("base is: {}, num is: {}".format(base, num))
    return num
    
def getFactor(arr, x):
    global Prime
    for i in range(len(Prime)):
        if arrFromBase(arr, x) % Prime[i] == 0:
            return Prime[i]

def getDistinctFactor(arr, x):
    global Prime
    global factor
    for i in range(len(Prime)):
        if arrFromBase(arr, x) % Prime[i] == 0:
            if not (Prime[i] in factor):         
                factor.append(Prime[i])            
                return Prime[i]
            
def processCoin(arr):
    global factor
    factor = []
    result = ''.join(str(x) for x in arr)
    for x in range(2, 11):
        result += " " + str(getFactor(arr, x))
    return result
    
def nextCoin(arr, index):
    if arr[index] == 0:
        arr[index] = 1
    else:
        arr[index] = 0
        nextCoin(arr, index - 1)
        
def preCoin(arr, index):
    if index > 0:
        if arr[index] == 1:
            arr[index] = 0
        else:
            arr[index] = 1
            preCoin(arr, index - 1)

def inPrimeRecursive(n, left, right, mid):
    global Prime
    if left > right:
        return False
    if Prime[mid] == n:
        return True
    elif Prime[mid] > n:
        return inPrime(n, left, mid, (left+mid)//2)
    else:
        return inPrime(n, mid, right, (mid+right)//2)
        
def inPrime(n, left, right, mid):
    global Prime
    while left <= right:
        if Prime[mid] == n:
            return True
        if Prime[mid] > n:
            right = mid - 1
        else:
            left = mid + 1
        mid = (left+right)//2

def prime(n):
    global Prime
    left = 0
    right = len(Prime) - 1
    mid = (left + right) // 2
    return inPrime(n, left, right, mid)
    
#true if this is a jamCoin
def coinCheck(arr):
    for i in range(2, 11):
        if isPrime(arrFromBase(arr, i)):
            return False
    return True

def jamCoin(n ,j):
    #initialize an array representation of n-digit coin
    arr = [0 for i in range(n)]
    arr [0] = 1
    arr [len(arr) - 1] = 1
    #print (arr)
    count = 0
    while count < j:
        #if this coin is a jamCoin
        if coinCheck(arr):
            curNum = processCoin(arr)
            if "None" not in curNum:
                print(curNum)
                count += 1
        nextCoin(arr, len(arr) - 2)
    return

def getPrimeList():
    global Prime
    f = open('primesCoin.txt', 'r')
    for line in f:
        num = [int(s) for s in line.split()]
        Prime.append(num[0])

def main():
    global Prime
    Prime = []
    getPrimeList()
    t = int(input())
    for i in range(1, t+1):
        n, j = [int(s) for s in input().split(" ")]
        print("Case #{}:".format(i))
        jamCoin(n, j)

if __name__ == "__main__":
    main()