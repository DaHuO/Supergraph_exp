#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

# Usage:
# ./coin_jams.py --primes
# ./coin_jams.py <test file>
#
# The first step is required to pre-compute the primes. We could technically do
# that at the same time (it takes ~43s) but the problem text says:
#
# > you can consider doing some computation before actually downloading an
# > input file and starting the clock.
#
# So it's ok to save some time here.

import sys
import math

BASES = range(2, 10+1)

# so ugly
PRIMES = {}

def compute_primes(max_n, targetfile):
    size = int(math.sqrt(max_n)+1)
    sieve = [True for _ in range(size)]

    # skip those
    sieve[0] = sieve[1] = False
    for i in range(size):
        if not sieve[i]:
            continue

        for j in range(i+1, size):
            if j%i == 0:
                sieve[j] = False

    with open(targetfile, "w") as f:
        for i in range(size):
            if sieve[i]:
                f.write("%d\n" % i)

def load_primes(sourcefile):
    with open(sourcefile) as f:
        PRIMES["p"] = list(map(int, f))

def is_maybe_prime(n):
    """
    We do multiple fermat primality tests so that if a number is likely to be
    prime we skip it. The issue here is that if we skip too many numbers we
    might find less jamcoins than asked for.
    """
    for a in (2, 3, 5, 7, 11, 13, 17):
        if pow(a, n-1, n) != 1:
            return False

    return True

def get_divisor(n):
    sq = int(1+math.sqrt(n))

    for d in PRIMES["p"]:
        if d > sq:
            break
        if n%d == 0:
            return d
    return 1

def check_jamcoin(jc):
    divisors = []

    for base in BASES:
        v = int(jc, base=base)
        if is_maybe_prime(v):
            return None

        divisor = get_divisor(v)
        if divisor == 1:
            return None
        divisors.append(divisor)

    return divisors

def next_jamcoin(s):
    s = list(s)
    for i in range(len(s)):
        idx = len(s)-2-i
        if s[idx] == "0":
            s[idx] = "1"
            for j in range(idx+1, len(s)):
                s[j] = "0"
            break

    s[-1] = "1"
    return "".join(s)

def gen_jamcoins(n):
    jc = "1%s1" % ("0" * (n-2))
    while True:
        divisors = check_jamcoin(jc)
        if divisors:
            yield (jc, divisors)
        jc = next_jamcoin(jc)

def solution(n, j):
    jamcoins = []

    for jc, divisors in gen_jamcoins(n):
        jamcoins.append((jc, divisors))
        if len(jamcoins) == j:
            break

    return jamcoins

def testcase(idx, n, j):
    print("Case #%d:" % idx)
    for jc, divisors in solution(n, j):
        print("%s %s" % (jc, " ".join(map(str, divisors))))

def main(sourcefile):
    with open(sourcefile) as f:
        skip_lines = 1
        test_idx = 0

        for line in f:
            if skip_lines > 0:
                skip_lines -= 1
                continue

            test_idx += 1
            n, j = map(int, line.strip().split(" "))
            testcase(test_idx, n, j)

if __name__ == "__main__":
    arg = sys.argv[1]

    if arg == "--primes":
        compute_primes(2**32, "primes")
    else:
        load_primes("primes")
        main(sys.argv[1])
