""" Google Code Jam 2016 - Part C
"""

import time

def isPrimeNumber(number):
    """ Check in a number is a prime number of not """
    pos = 2
    start = time.time()
    while number != pos:
        if (number % pos) == 0:
            return False, pos
        pos += 1

        if time.time() - start > .1:
            break
    return True, number


N = 16
M = 50

startBin = int("1%s1" % "".join(['0' for i in range(N-2)]), 2)

STEP, countPrimes = 3, 0
path = r'C:\Users\HOME\Downloads\CodeJam'
outFile = open(r'%s\out\C_small_out_%s_%s_%s.dat' % (path, N, M, STEP), 'w')
outFile.write('Case #1:\n')
while countPrimes < M:
    res, divs = [], []
    binStr = str(bin(startBin))[2:]
    if binStr[0] != '1' or binStr[-1] != '1':
        startBin += STEP
        continue

    for base in range(2, 11):
        num = int(binStr, base)
        isPrime, div = isPrimeNumber(num)
        res.append(isPrime)
        divs.append(str(div))
    if not any(res):
        outFile.write('%s %s\n' % (binStr, ' '.join(divs)))
        countPrimes += 1
    startBin += STEP

outFile.close()