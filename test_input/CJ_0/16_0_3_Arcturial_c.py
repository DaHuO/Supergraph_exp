import random
import math
import sys

primes = []

def checkPrime(number):
    if (number == 2): return True
    if (number % 2 == 0): return False
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if (number % i == 0): return False

    return True

def generatePrimes():
    with open('primes.txt', 'w') as file_:
        number = 2
        while True:
            if checkPrime(number):
                file_.write(str(number) + '\n')

                # Up until 10000000
                if number > 10000000:
                    break
            number += 1

def findDivisors(binaryString):
    stack = []
    global primes

    for i in range(2, 11):
        val = int(binaryString, i)
        found = False

        for j in primes:
            if val % j == 0:
                stack.append(str(j))
                found = True
                break

        if not found:
            raise Exception('Could not find matching prime.')

    return stack

def hasTried(coinSet, value):
    inSet = value in coinSet
    coinSet.add(value)
    return inSet

def isPrime(n):
    global primes

    for j in primes:
        if j == n: return True

    return False

def isJamCoin(value):
    valueString = str(value)

    if valueString[-1:] != '1' or valueString[:1] != '1':
        return False

    for i in range(2, 11):
        inBase = int(value, i)
        if isPrime(inBase):
            return False

    return True

def randomAttempt(length):
    pad = ['0'] * length
    arrStack = ['1'] * length
    rand = math.ceil((random.random() * int(''.join(arrStack), 2)))
    rand = '{0:b}'.format(rand)
    return rand.zfill(length)

def program(value, caseKey):
    parts   = value.split(" ")
    length  = parts[0]
    coins   = parts[1]
    tried   = set()

    print("Case #%d:" % caseKey)


    for i in range(0, int(coins)):
        realLength  = int(length) - 2;
        coin        = None;

        while True:

            coin = "1%s1" % randomAttempt(realLength)

            if not hasTried(tried, coin) and isJamCoin(coin):
                try:
                    divisors = findDivisors(coin)
                    print(str(coin) + " " + ' '.join(divisors))
                    break
                except Exception as error:
                    pass



# Preload primes
def preload():
    with open('primes.txt', 'r') as file_:
        for line in file_:
            primes.append(int(line))

#generatePrimes()
preload()

with open(sys.argv[1], 'r') as file_:
    limit = file_.readline()

    for i in range(0, int(limit)):
        program(file_.readline(), i + 1)
