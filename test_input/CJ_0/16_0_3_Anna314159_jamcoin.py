#!/usr/bin/python

import numpy as np
import math
import sympy as sp

def findSmallestFactor(x):
    found = False
    p = 2
    fact = 1
    for i in xrange(1000):
        if x % p == 0:
            return p
        else:
            p = sp.nextprime(p)
    return -1

#write all jamcoins to the output file
#test for all number 0 - 2^(N-2) if 1number1 (binary) is prime for any base 2 .. 10 (prime --> no jamcoin)
def produceJamCoins(J, N, outFile): 
    outFile.write("Case #1:\n")
    nrJamCoins=0
    for i in xrange(int(math.pow(2,(N-2)))):
        if nrJamCoins==J:
            break
        coin = '1' + np.binary_repr(i, width=N-2) + '1'
        witnesses = []
        for k in range(2,11):
            x = int(coin, base=k)
            if sp.isprime(x):
                break
            
            #factors = sp.factorint(x).keys()
            #factors.sort()
            w = findSmallestFactor(x)
            if w == -1:
                break
            witnesses.append(w)
        if len(witnesses) == 9:
            nrJamCoins += 1
            outFile.write(coin + " " + " ".join(map(str, witnesses)) + "\n")
            outFile.flush()


inFile=open('jamInput.txt', 'r')
outFile=open('jamOutput.txt', 'w')

nrLines = int(inFile.readline())

for i, line in enumerate(inFile):
    numbers=map(int, line.split())
    N=numbers[0] # length
    J=numbers[1] # nr of jamcoins
    produceJamCoins(J, N, outFile)

inFile.close()
outFile.close()
