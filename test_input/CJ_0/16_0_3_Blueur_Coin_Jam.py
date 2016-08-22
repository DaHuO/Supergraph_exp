import sys
import math
from functools import reduce

inputFile = sys.argv[1]

f = open(inputFile, 'r')

args = f.readline()
T = int(args)

def answer(N, J):
    j = J
    result = []
    for n in range(2**(N-2)):
        coin = '1' + format(n, "0" + str(N-2) + "b") + '1'
        bin = [int(c) for c in list(coin)]
        evi = getEvidence(bin)
        if len(evi) != 0:
            result.append(coin + " " + " ".join(evi))
            j = j - 1
            if j == 0:
                return "\n".join(result)

def getEvidence(bin):
    result = []
    for b in range(2, 11):
        tmp = getDivisor(computeBase(bin, b))
        if tmp == -1:
            return []
        else:
            result.append(str(tmp))
    return result

def computeBase(bin, base):
    tmp = enumerate(bin[::-1])
    return reduce(lambda x, y: x + y[1]*(base**y[0]), tmp, 0)

def getDivisor(n):
    for i in range(2, math.ceil(math.sqrt(n))):
        if n % i == 0:
            return i
    return -1

for t in range(T):
    args = f.readline().split(' ')
    N = int(args[0])
    J = int(args[1])
    print("Case #{0}: {1}".format(t + 1, answer(N, J)))
