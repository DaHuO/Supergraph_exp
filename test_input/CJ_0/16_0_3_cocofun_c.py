#!/usr/bin/python
import math

def is_prime(n):
    n = abs(n)
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True

N = 16 - 2
J = 50

print 'Case #1:'

FOUND = 0

for xx in xrange(1, 2 ** N):
    xx = str(bin(xx)[2:])
    qq = '1' + '0' * (N - len(xx)) + xx + '1'
    bases = []

    for base in range(2, 10 + 1):
        number = int(qq, base)

        if is_prime(number) == False:
            for xx in xrange(2, number):
                if number % xx == 0:
                    bases.append(xx)
                    break
        else:
            break

    if len(bases) == 9:
        print qq, str(bases)[1:-1].replace(',', '')
        FOUND += 1

    if FOUND == J:
        break
