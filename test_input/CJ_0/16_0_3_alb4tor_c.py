#!/usr/bin/python

import math

nb = int(raw_input())

def find_primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

primes = find_primes(2**16)

def divisors(num):
    limit = math.sqrt(num) + 3
    for i in primes:
        if i > limit:
            return 0

        if num % i == 0:
            return i

# new primes


for n in xrange(1, nb+1):
    res = []
    N, J = [ int(i) for i in raw_input().split() ]

    fixe = 2**(N-1)+1

    found = 0
    for i in xrange(2**(N-2)):
        jamcoin=fixe+(i<<1)

        fmt = "{:b}"
        jamcoin_s = fmt.format(jamcoin)

        proofs=[]
        for i in xrange(2, 11):
            jam_base = int(jamcoin_s, i)
            proof = divisors(jam_base)
#            print ">>", jamcoin_s, jam_base, proof
            if not proof:
                break
            proofs.append(str(proof))
        else:
            res.append(jamcoin_s + " " + " ".join(proofs))
            found+=1

        if found == J:
            break

    print "Case #%i:" % (n)
    print "\n".join(res)
