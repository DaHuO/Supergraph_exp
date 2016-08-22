#!/usr/bin/env python3

import itertools
import sys
import math

def next_candidate(larger_than):
    """ The next candidate number after larger_than """
    n = int(larger_than,2) + 1
    s = bin(n)[2:]
    while((s[0] != "1") or (s[-1] != "1")):
        n = int(s,2) + 1
        s = bin(n)[2:]
    return s

def get_factor(n):
    limit = int(math.sqrt(n))
    for p in primes:
        if p > limit:
            # smallest prime factor of n is <= sqrt(n)
            break
        if n%p == 0:
            return str(p)
    return None

def load_primes(limit):
    global primes
    with open("primes","r") as f:
        for prime in f.readlines():
            if int(prime) > limit:
                break
            primes.append(int(prime))

primes = []

if __name__ == "__main__":
    N = int(sys.argv[1])
    J = int(sys.argv[2])

    # we only need to test with prime numbers up to sqrt of the largest possible number
    # for the large case, we don't have enough primes for that - that's ok
    # we'll miss some numbers that aren't prime (they have a large smallest prime factor)
    # but who cares - there's no completeness constrain, we just have to find J numbers
    # that meet the criteria
    load_primes(math.sqrt(int("1"*N, 10))) 
    #print("Loaded {} primes".format(len(primes)))

    print("Case #1:")

    # Start testing candidate numbers for primality
    answers = 0
    s = bin(2**(N-1))[2:]
    while((answers < J)):
        s = next_candidate(s)
        if len(s) > N:
            raise(Exception("Ran out of numbers to test"))

        prime = False
        factors = []
        for base in range(2,11):
            factors.append(get_factor(int(s,base)))
            if factors[-1] == None:
                prime = True
                break

        if not prime:
            answers += 1
            print("{} {}".format(s, " ".join(factors)))

