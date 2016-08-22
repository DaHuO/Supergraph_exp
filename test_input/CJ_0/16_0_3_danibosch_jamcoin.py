from random import randint
from math import sqrt

def prime_list():
    primes = []
    for p in xrange(3, 1000, 2):
        for d in xrange(3, int(sqrt(p)) + 2):
            if p % d == 0:
                break
        else:
            primes.append(p)
    return primes

def divisor(base):
    for p in primes:
        if base % p == 0:
            return p

t = int(raw_input())
print "Case #{}:".format(t)
n, j = [int(s) for s in raw_input().split(" ")]

primes = prime_list()

jamcoins = []

x = 1
while x < j + 1: #for x in xrange(1, j + 1):
    jamcoin = 1

    for y in xrange(1, n - 1):
        digit = randint(0,1)
        jamcoin = jamcoin * 10 + digit
    jamcoin = jamcoin * 10 + 1

    divs = []
    for b in xrange(2, 11):
        base = int(str(jamcoin), b)
        div = divisor(base)
        if div and jamcoin != div:
            divs.append(div)
        else:
            break
    else:
        if jamcoin not in jamcoins:
            jamcoins.append(jamcoin)
            print "{} {}".format(jamcoin, " ".join(str(e) for e in divs))
            x += 1