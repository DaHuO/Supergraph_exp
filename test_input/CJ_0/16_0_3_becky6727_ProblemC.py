import os, sys, time
import numpy

#prime decomposition
def PrimeDecomp(n):
    i = 2
    table = []
    while(i* i <= n):
        while(n%i == 0):
            n /= i
            table.append(i)
            pass
        i += 1
        pass
    if(n > 1):
        table.append(n)
        pass
    return table

#prime number check
def isPrime(n):
    i = 2
    while(i* i <= n):
        if(n%i == 0):
            return False
        i += 1
        pass
    return True

FileIN = './Input/C-small-attempt0.in.txt'

N = 0

TestCase = []

for Lines in open(FileIN):

    #strip \n
    Line = Lines.rstrip('\n')

    #split Lines with space
    Line = Line.split(' ')

    #type conversion
    for i in range(len(Line)):
        Line[i] = int(Line[i])
        pass
    
    if(N != 0):
        TestCase.append(Line)
    else:
        NofCase = Line[0]
        pass

    N += 1
    pass

#JamCoin = 33 #100001, test case
#JamCoin = 32769 #1000000000000001
JamCoin = 2**(TestCase[0][0] - 1) + 1
LimitJamCoin = 2**(TestCase[0][0]) - 1

Count = 0
#NofJamCoins = 3 #test case
NofJamCoins = TestCase[0][1]

print 'Case #1:'

#while(JamCoin <= 63):
#while(JamCoin <= 65535):
while(JamCoin <= LimitJamCoin):
    
    tmp = bin(JamCoin)
    tmp = tmp.lstrip('0b')

    #initialize
    CaseLine = []
    PrimeLine = []
    
    for i in range(2, 11, 1):
        Num = int(tmp, i)
        CaseLine.append(Num)
        pass

    #do prime decomposition & prime number check
    for i in range(len(CaseLine)):

        if(isPrime(CaseLine[i])):
            break
        
        PrimeTable = PrimeDecomp(CaseLine[i])
        PrimeLine.append(PrimeTable[-1])
        pass

    if(len(PrimeLine) < 9):
        JamCoin += 2
        continue

    print tmp,
    for i in range(len(PrimeLine)):
        print PrimeLine[i],
        pass
    print ''
    
    Count += 1

    if(Count >= (NofJamCoins)):
        break
        
    JamCoin += 2

    pass
