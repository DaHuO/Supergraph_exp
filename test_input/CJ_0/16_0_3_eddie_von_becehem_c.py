from math import sqrt, pow, log, ceil, log10
from sys import stdin
import random

T = int(stdin.readline())

alreadytested = []

def randomcoin(N):
    while True:
        ans = [1]

        for i in range(1,N-1):
            ans.append(random.randint(0,1))

        ans.append(1)

        if ans not in alreadytested:
            alreadytested.append(ans)
            return ans

def isprime(x):
    # if prime, return true, []
    # else, return false, divisor
    if x in primeList:
        return (True, [])
    else:
        for y in primeList:
            if x % y == 0:
                return (False, y)        

        return (True, [])


def isjamcoin(s):

    l = len(s)
    sbaselist = []

    for base in range(2,11):
        sbase = 0
        power = 1
        for d in range(l):
            sbase += power * s[l - 1 - d]
            power *= base

        # print "Testing", sbase, s, base
        ans, proof = isprime(sbase)
        # print "Res", ans, proof

        if ans:
            return (False, [])

        sbaselist.append(proof)

    return (True, sbaselist)

def sol(N, J):
    found = 0

    while found < J:
        s = randomcoin(N)
        ans, proof = isjamcoin(s)
        if ans:
            rep = ""
            for x in s:
                rep += str(x)

            for x in proof:
                rep += " " + str(x)

            print rep
            found += 1

    return

# Prepare
primeList = [2]
Composite = {}
maxPrime = 1000

for n in range(3,maxPrime):
    isPrime = True
    for x in range(2, n - 1):
        if n % x == 0:
            Composite[n] = x
            isPrime = False
            break

    if isPrime:
        primeList.append(n)

# print primeList
# print Composite

N, J = map(int, stdin.readline().split())

print "Case #1:"
sol(N, J)

