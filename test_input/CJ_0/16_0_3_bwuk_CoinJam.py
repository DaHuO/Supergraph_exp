#Crazy primes

import math

def toDecimal(num, base):
    power = 0
    result = 0
    while num > 0:
        result += (num%10) * (base ** power)
        num = num // 10
        power += 1
        
    return result 

def firstFactor(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return i
        if i > 10000:
            return -1
        
    return -1

def isCoinJam(n):
    result = ''
    for i in range(2, 11):
        decValue = n
        if i < 10:
            decValue = toDecimal(n, i)
        factor = firstFactor(decValue)
        if factor == -1:
            return ''
        result += str(factor) + ' '
    return result.strip()

def main():
    f = open('CoinJam.in', 'r')
    numCases = int(f.readline())

    for i in range(1, numCases+1):
        print('Case #1:')
        line = f.readline().split(' ')
        numDigits = int(line[0].strip())
        numCoinJams = int(line[1].strip())

        start = 2**(numDigits - 1) + 1
        stop = 2**numDigits
        numFound = 0

        for cur in range(start, stop, 2):
            binaryValue = bin(cur)[2:]
            result = isCoinJam(int(binaryValue))
            if result != '':
                print(binaryValue, result)
                numFound += 1
            if numFound >= numCoinJams:
                break

main()
        
