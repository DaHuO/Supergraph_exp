#!/usr/bin/env python
# Python 3

import random

small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
    61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139,
    149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227,
    229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311,
    313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401,
    409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491,
    499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
    601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683,
    691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
    809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887,
    907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997)

# Generate a random candidate of 1s and 0s. Convert it to the different bases.
# All you have to do is prove each result is not prime, not that each result is prime.
# Which means you can spend some fixed amount of time checking for not-primality, and if you cannot
# prove not-primality, then you just give up, generate a new candidate, and start fresh.
# You may wind up passing up a candidate that was in fact not prime, but who gives a hoot. There is
# absolutely no punishment for that.


def obviously_not_prime(n):
    # Checks for primality against all primes under 1000
    # If this function returns false, that DOES NOT MEAN THAT THE INPUT IS PRIME.
    # It only means that a quick check could not immediately confirm the input is not prime.
    # If the input is indeed not prime, this function returns a divisor.

    for p in small_primes:
        if n % p == 0:
            return p

    return False

def pc(n, j):
    jamcoins = set()
    reply = {}

    while len(jamcoins) < j:
        candidate = "1" + "".join([random.choice(['0', '1']) for x in range(n - 2)]) + "1"
        cand_rebased = [int(candidate, base) for base in range(2, 10 + 1)]

        prime_check = list(map(obviously_not_prime, cand_rebased))

        if False not in prime_check:
            jamcoins.add(candidate)
            reply[candidate] = prime_check

    answer = ""
    for (k, v) in reply.items():
        answer += k + " " + " ".join(map(str, v)) + "\n"

    return(answer)

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, j = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    print("Case #{}:".format(i))
    print(pc(n, j))
    # check out .format's specification for more formatting options
