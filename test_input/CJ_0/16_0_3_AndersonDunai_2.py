#!/usr/bin/env python2

import sys
import math

count = int(sys.stdin.readline().strip())
case = 1


def find_divisors(coin):
    divisors = []

    for base in xrange(2, 11):
        found = False
        value = int(coin, base)
        for n in xrange(2, min(int(math.sqrt(value)) + 1, 1000000)):
            # Limit search to first 1kk possible divisors,
            # we still have a lot of other possible coins to select from,
            # and they are likely to be much easier to find.
            if value % n == 0:
                found = n
                break
        if found:
            divisors.append(n)
            sys.stderr.write('Got divisor for base {}\n'.format(base))
        else:
            if n == 1000000:
                sys.stderr.write('Found prime {}, stop\n'.format(value))
            else:
                sys.stderr.write('Threshold exceeded, stop\n'.format(value))
            return divisors

    return divisors


def solve(length, required):
    coins = []

    for i in xrange(0, pow(2, length - 2)):
        coin = '1' + bin(i)[2:].rjust(length - 2, '0') + '1'

        divisors = find_divisors(coin)
        
        if len(divisors) == 9:
            sys.stderr.write('Got {}/{} coins\n'.format(len(coins), required))
            coins.append('{} {}'.format(coin, ' '.join([str(x) for x in divisors])))

        if len(coins) == required:
            return coins


while case <= count:
    args = sys.stdin.readline().strip().split(' ')
    n, j = args
    print 'Case #{}:\n{}'.format(case, '\n'.join(solve(int(n), int(j))))
    case += 1





# from math import sqrt; from itertools import count, islice


# def isPrime(n):
#     return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

# for i in xrange(1000000, 2000000):
#     s = i, isPrime(i)
