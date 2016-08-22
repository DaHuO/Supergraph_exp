import math

N = 16
J = 50

maxNumber = 2**N-1
primeLimits =  2**20
isPrime = [True] * primeLimits

def eratostenes(limit):
    limit = limit-1
    for i in range(2, limit):
        j = 2
        while i*j <= limit:
            isPrime[i*j] = False
            j+=1

def searchDivisor(n):
    if n%2 == 0 and n != 2:
        return 2
    i = 3
    while i*i <= n:
        if n%i == 0:
            return i
        i += 2

    return 0

eratostenes(primeLimits)
numbers = 0

print "Case #1:"

for i in xrange(2**(N-1), maxNumber):
    binary = str(bin(i))[2:]
    if binary[-1] == '0':
        continue
    baseChange = [0] * 11
    prime = False

    for j in range(2, 11):
        baseChange[j] = int(binary, j)
        if baseChange[j] < primeLimits and isPrime[baseChange[j]]:
            prime = True
            break

    if prime:
        continue

    divisors = [0] * 11
    for j in range(2, 11):
        divisors[j] = searchDivisor(baseChange[j])
        if divisors[j] == 0:
            prime = True
            break

    if prime:
        continue

    numbers+=1
    print binary, ' '.join(str(x) for x in divisors[2:])

    if numbers == J:
        break