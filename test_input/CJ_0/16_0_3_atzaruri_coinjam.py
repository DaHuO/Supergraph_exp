import sys
import math

def interpret(bits, base):
    multiplier = 1
    result = 0

    for it in xrange(16):
        if bits & 1:
            result += multiplier
        multiplier *= base
        bits = bits >> 1

    return result

def isPrime(number):
    for d in xrange(2, int(math.sqrt(number))):
        if number % d == 0:
            return d

    return -1

def printBinary(number, positions):
    digits = []

    for it in xrange(positions):
        if number & 1:
            digits += ["1"]
        else:
            digits += ["0"]
        number = number >> 1

    print "".join(reversed(digits)),

LIMIT = 2 ** 14

n = int(sys.stdin.readline())
print "Case #1:"

for it in xrange(0, LIMIT):
    it = it << 1 | 32769
    divs = []

    for base in xrange(2, 11):
        divs += [isPrime(interpret(it, base))]
        if divs[-1] == -1:
            break

    if divs[-1] != -1:
        printBinary(it, 16)
        print " ".join([str(x) for x in divs])
        n -= 1
        if n == 0:
            break
