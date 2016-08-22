__author__ = 'drathier'

"""

1(0|1){N-2}1 interpreted in base 2->10 must not be prime

- we need all primes up to N
- J different strings of length N that are not primes in any base 2-10

parts:
- parse string in base b, possibly using int(str, b)
- calc all primes up to sqrt of base-10 interpretation of string, i.e. sqrt(10^16) or sqrt(10^32)
- precompute list of divisors when sieving; save first value that divides it
-


"""

from math import sqrt


# prime sieve up to n, return list
# - 0 if prime
# - lowest prime divisor otherwise
def ps(n):
    sqn = int(sqrt(n)) + 1
    r = [0] * n
    p = []
    for i in xrange(2, sqn):
        if r[i] == 0:
            p += [i]
            k = i * i
            while k < n:
                r[k] = i
                k += i
    return p


"""
most numbers are not prime, especially big ones
- randomly pick a jamcoin-string
- check if we can prove it's not prime
    -> use it

"""



def composit(a):
    for p in primes:
        if a % p == 0:
            return p
    return -1


def parse(a):
    res = []
    for i in range(2, 11):
        res += [int(a, i)]
    return res


import random


def jc(n):
    r = ""
    while len(r) < n-2:
        r += "01"[random.getrandbits(1)]
    return "1" + r + "1"

#for i in range(10):
#    print "jc", jc(10)

#print "parse", parse("1001"), [9, 28, 65, 126, 217, 344, 513, 730, 1001]

#print "ps", 10
primes = ps(10 ** 5)

def s(n, need):
    tries = 0
    res = set()
    resd = {}
    while len(res) < need:
        tries += 1
        jcs = jc(n)
        p = parse(jcs)
        c = map(composit, p)
        #print "s", n, jcs, p, c, res
        if all([x > 0 for x in c]):
            #print "parse", p, c, "tries", tries, "res", res
            res.add(jcs)
            resd[jcs] = c
    return resd

#sres = s(16, 50)
sres = s(32, 500)
#print "s", sres

print "Case #1:"
for k,v in sres.iteritems():
    print k, " ".join(map(str, v))