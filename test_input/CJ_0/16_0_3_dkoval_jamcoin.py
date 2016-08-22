from itertools import product
from sys import stdin

import math


def non_prime_f(n):
    for f in xrange(2, math.trunc(math.sqrt(n)) + 1):
        if n % f == 0:
            return f
    return 0


def convert(bits, base):
    m = 1
    number = 0
    for bit in reversed(bits):
        number += m * bit
        m *= base
    return number


def solve(n, count):
    for bits in product((0, 1), repeat=n):
        if not bits[0] or not bits[-1]:
            continue

        divisors = []
        for base in xrange(2, 11):
            number = convert(bits, base)
            divisor = non_prime_f(number)
            if not divisor:
                break
            divisors.append(divisor)

        if len(divisors) == 9:
            print ''.join(map(str, bits)) + ' ' + ' '.join(map(str, divisors))
            count -= 1

        if not count:
            break


if __name__ == '__main__':
    stdin.readline()
    n, j = map(int, stdin.readline().split(' '))
    print 'Case #1:'
    solve(n, j)
