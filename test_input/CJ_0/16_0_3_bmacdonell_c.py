import math

import sys


def divisor_base2(n):
    for i in xrange(3, int(math.sqrt(n) + 1), 2):
        if n % i == 0:
            return i


def divisor_baseb(n, b):
    n = int(bin(n)[2:], b)
    for i in xrange(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i


if __name__ == '__main__':
    _ = sys.stdin.readline()  # skip test case count
    n, j = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    print 'Case #1:'
    lower = int('1' + '0' * (n - 2) + '1', 2)
    upper = int('1' + '0' * n, 2)
    emitted = 0
    for n in xrange(lower, upper, 2):
        divisors = []
        divisor_2 = divisor_base2(n)
        if divisor_2 is None:
            continue
        divisors.append(divisor_2)
        for b in xrange(3, 11):
            divisor = divisor_baseb(n, b)
            if divisor is None:
                break
            divisors.append(divisor)
        if len(divisors) == 9:
            print bin(n)[2:], ' '.join([str(d) for d in divisors])
            emitted += 1
            if emitted == j:
                exit(0)
