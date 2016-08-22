#!/usr/bin/env python3
# Coin Jam

# brute force, yes, but is there should be a better way?

# aa = str(bin(myInt))[2:] gives binary string literal
# alt: use itertools.product()

from sys import argv
from itertools import product

# global variables and constants
inData = []
TEST = False
N = 0

# basic components for I/O and testing

# probably better coding style
def altInit():
    global inData
    try:
        with open(argv[1], 'r') as f:
            inData = f.read()
    except OSError:
        # 'File not found' error message.
        print("Fichier non trouvé")

def init():
    if len(argv) > 0:
        # outFile = sys.argv[2]
        global inData
        with open(argv[1], "rt") as f: # should change to read filename
            inData = f.read()

# problem-specific defs

# or itertools.accumulate() !!!
# use built-in fcns for bases 2, 8, 10
def convertBase10(base, bstring): # bstring does *not* include '1's at ends
    if base == 2:
        return int('1' + bstring + '1', base = 2)
    if base == 8:
        return int('1' + bstring + '1', base = 8)
    if base == 10:
        return int('1' + bstring + '1', base = 10)

    # print("convertBase10 Test")
    bits = len(bstring) # ex. 4, so 6 bits total
    bsum = 1
    for ii in range(len(bstring)-1,-1,-1): # count down (3,2,1,0)
        # print(ii, bsum)
        if bstring[ii] == '1':
            bsum += (base ** (bits - ii))
    return bsum + base ** (bits+1)
    # check!

def minDivisor(number): # returns 1 if prime
    if number % 2 == 0:
        return 2
    if number % 3 == 0:
        return 3
    divisor = 5
    while divisor*divisor <= number:
        if number % divisor == 0:
            return divisor
        if number % (divisor + 2) == 0:
            return (divisor + 2)
        divisor += 6
    return 1

if TEST:
    print("Test:")
    
    teststring = '1100'
    divisorList = []

    for dd in range(2,11):
        base10 = convertBase10(dd, teststring)
        divisor = minDivisor(base10)
        print("base:", str(dd), "base10:", base10, "divisor:", divisor)
        if divisor > 1:
            divisorList.append(divisor)
        else:
            divisorList = []
            break
    if len(divisorList) > 0:
        # counter += 1
        pass
    print('1' + teststring + '1', *divisorList)

    ans = minDivisor(425)
    print(ans)
    print("end test")

# altInit()
init()            

dataset = inData.splitlines() # split on newlines

T = 1
[N, J] = [int(x) for x in dataset[1].split()]

# brute force...

counter = 0
innerBinary = product(range(2), repeat=N-2) # iterator
primeCounter = 0

print("Case #1:")

for bb in innerBinary:
    # bstring = '1' + ''.join([str(x) for x in bb]) + '1'
    bstring = ''.join([str(x) for x in bb])
    # print(bstring)
    divisorList = []

    for dd in range(2,11):
        divisor = minDivisor(convertBase10(dd, bstring))
        if divisor > 1:
            divisorList.append(divisor)
        else:
            divisorList = []
            break
    if len(divisorList) > 0:
        counter += 1
        print('1' + bstring + '1', *divisorList)
    if counter == J:
        break
